from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from .serializers import UsersSerializer


class UsersAPIView(APIView):
    def get(self, request):
        ggg = Users.objects.all()
        return Response({'clients': UsersSerializer(ggg, many=True).data})

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


