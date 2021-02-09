from rest_framework import serializers
from .models import Member


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class MemberSerializerTop(serializers.ModelSerializer):
    username = serializers.CharField(source='customer')
    spent_money = serializers.CharField(source='total')
    gems = serializers.CharField(source='item_top_five')
    class Meta:
        model = Member
        fields = ('username', 'spent_money', 'gems',)
