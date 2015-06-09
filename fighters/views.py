from django.db import IntegrityError
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


# models and serialization
from fighters.models import Fighter, PracticeSession
from django.contrib.auth.models import User
from fighters.serializers import FighterSerializer, PracticeSessionSerializer, UserSerializer
from django.db.models.base import ObjectDoesNotExist 

#authentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from fighters.permissions import IsTrainerOrReadOnly, IsTrainer, IsTrainerOrOwner

class ObtainAuthToken(APIView):	
	permission_classes = ()	
	serializer_class = AuthTokenSerializer
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		try:
			return Response({'token': token.key, 'name': user.fighter.name, 'status': user.fighter.status})
		except ObjectDoesNotExist:
			return Response({'token': token.key })


class GenerateTokens(APIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainer,)
	def get(self, request):
		from django.contrib.auth.models import User
		from rest_framework.authtoken.models import Token

		for user in User.objects.all():
			Token.objects.get_or_create(user=user)
		return Response("Success", status=status.HTTP_200_OK)

class FighterList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainerOrReadOnly,)
	queryset = Fighter.objects.all()
	serializer_class = FighterSerializer


class FighterDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainerOrOwner,)
	queryset = Fighter.objects.all()
	serializer_class = FighterSerializer

class UserList(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainer,)
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainer,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SessionList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainer,)
	queryset = PracticeSession.objects.all()
	serializer_class = PracticeSessionSerializer

	def post(self, request):
		#overwritten so post requests update practice session if it exists on a particular date
		serializer = PracticeSessionSerializer(data=request.data)
		if(serializer.is_valid()):
			#Check if date already exists	
			session_set = PracticeSession.objects.filter(date=serializer.validated_data.get('date'))
			if(session_set.count() > 0):
				session = session_set[0]				
				
				# add half attendance
				half_attendees = serializer.validated_data.get('half_attendance')
				session.half_attendance.add(*half_attendees)

				# add full attendance
				full_attendees = serializer.validated_data.get('full_attendance')
				session.full_attendance.add(*full_attendees)
				
				#make sure no-one is both in full and half attendance
				full = session.full_attendance.all()
				session.half_attendance.remove(*full)				

				return Response(PracticeSessionSerializer(session).data)
			else:
				serializer.save()
				return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, IsTrainer,)
	queryset = PracticeSession.objects.all()
	serializer_class = PracticeSessionSerializer