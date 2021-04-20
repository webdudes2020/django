from django import forms
from rest_framework import serializers

from.models import Post


class PostSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner'
        )
