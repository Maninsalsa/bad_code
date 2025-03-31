from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    # instance class
    class Meta:

        model = User
        fields = ('id', 'username', 'email', 'password', 'password2') 
        extra_kwargs = {
            'password': {'write_only': True} 
        }
    # Validation method for passwords
    def validate(self, data):
        # verifies password must match
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match")
        return data
    
    # override create method to properly hash password
    def create(self, validated_data):
        #remove password2 from data since we don't save it
        validated_data.pop('password2')

        # create user with cleaned data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

# class variables

    # password2

        # Inherets from MS for automatic field gen
        # password2 is the conventional confirmation field during registration
        # password2 is a confirmation field that is write-only, meaning:
        # - It will be included in the input data during registration
        # - It will NOT be included in the serialized output (API responses)
        # - This is important for security to prevent password confirmation from being exposed
        # - The field uses CharField as it handles string/text data

#