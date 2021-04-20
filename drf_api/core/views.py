from django.http import JsonResponse
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from.serializers import PostSeriallizer
from.models import Post


class Test_View(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSeriallizer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
