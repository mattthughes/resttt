from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id', 'created_at','owner', 'post',
        ]