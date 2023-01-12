from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer): # 모델을 기반으로 작동하는 시리얼라이저
    class Meta:
        model = Article
        fields = '__all__'
