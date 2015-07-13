from django.forms import widgets
from rest_framework import serializers
from fighters.models import Fighter, PracticeSession
from django.contrib.auth.models import User

class FighterMin(serializers.ModelSerializer):
	class Meta:
		model = Fighter
		fields = ('name', 'status')

class UserMin(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email')


class RegisterUserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		user = User(email=validated_data['email'], username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email',)

class FighterSerializer(serializers.ModelSerializer):
	userinfo = UserSerializer(required=False, allow_null=True, read_only=True)
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required = False)	
	class Meta:
		model = Fighter
		#fields = ( 'id', 'name', 'user', 'is_trainer', 'is_admin','is_fighter','is_archer','is_newbie', 'can_post_notifications', )


class PracticeSessionSerializer(serializers.ModelSerializer):
	half_attendance = serializers.PrimaryKeyRelatedField(
												many=True, 
												queryset=Fighter.objects.all(), 
												allow_null=True
	)
	full_attendance = serializers.PrimaryKeyRelatedField(
												many=True, 
												queryset=Fighter.objects.all(), 
												allow_null=True																				
	)

	class Meta:
		model = PracticeSession
		fields = ('id', 'date', 'session_type', 'description', 'half_attendance', 'full_attendance',)		

