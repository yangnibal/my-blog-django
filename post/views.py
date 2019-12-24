from django.shortcuts import render
from rest_framework.decorators import action, api_view
from .models import Post, Comment
from account.models import User
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
import random

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):  
        possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        key = ""
        for i in range(50):
            key += random.choice(possible)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            #import pdb; pdb.set_trace()
            serializer.save(author=request.user, post_key=key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, list=True, methods=['GET'])
    def mypost(self, request):
        post = Post.objects.filter(author=request.user)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    @action(detail=False, list=True, methods=['POST'])
    def otherpost(self, request):
        user = User.objects.get(username=request.data['username'])
        post = Post.objects.filter(author=user)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        #import pdb; pdb.set_trace()
        if serializer.is_valid():
            post = Post.objects.get(post_key=request.data['post'])
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail(request, postkey):
    try:
        post = Post.objects.get(post_key=postkey)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        comment = Comment.objects.filter(post=post)
        postser = PostSerializer(post)
        commentser = CommentSerializer(comment, many=True)
        return Response(
            {
                'post': postser.data, 
                'comment': commentser.data
            }    
        )

@api_view(['DELETE'])
def delete(request, postkey):
    try:
        post = Post.objects.get(post_key=postkey)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)