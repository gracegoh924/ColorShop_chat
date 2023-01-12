from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    # print(articles)
    article = articles[0]
    # serializer =  ArticleSerializer(article)
    serializer =  ArticleSerializer(articles, many=True)
    return Response(serializer.data) # 어트리뷰트