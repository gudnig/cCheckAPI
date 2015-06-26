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

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email',)

class FighterSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required = False)	
	class Meta:
		model = Fighter
		fields = ( 'id', 'name', 'status', 'created', 'user', 'is_trainer', 'is_admin', 'can_post_notifications', )


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

