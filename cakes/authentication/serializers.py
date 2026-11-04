from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile

        fields = ['username','first_name','password','role']

        write_only_fields = ['password']

        read_only_fields = ['email']