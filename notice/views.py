from django.shortcuts import render
from .models import Notice
from account.models import User
from .serializers import NoticeSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from account.models import User
from post.models import Post
from rest_framework.decorators import action, api_view
# Create your views here.

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def create(self, request):
        serializer = NoticeSerializer(data=request.data)
        receiver = User.objects.get(username=request.data['username'])
        if serializer.is_valid():
            serializer.save(sender=request.user, receiver=receiver)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, list=True, methods=['GET'])
    def mynotice(self, request):
        user = request.user
        notice = Notice.objects.filter(receiver=user)
        serializer = NoticeSerializer(notice, many=True)
        return Response(serializer.data)

    @action(detail=False, list=True, methods=['GET'])
    def deleteall(self, request):
        user = request.user
        notice = Notice.objects.filter(receiver=user)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, list=True, methods=['POST'])
    def delete(self, request):
        notice = Notice.objects.get(pk=request.data['id'])
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


