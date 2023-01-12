from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    # print(articles)
    article = articles[0]
    article_dict = {
        "title":article.title,
        "content":article.content,
        "created_at":article.created_at,
        "updated_at":article.updated_at,
    }
    return Response(article_dict)