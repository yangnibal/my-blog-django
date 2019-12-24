from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    receiver = serializers.CharField(source='receiver.username', read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Notice
        fields = ['receiver', 'sender', 'id', 'type', 'post']