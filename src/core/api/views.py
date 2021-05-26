from rest_framework import serializers, viewsets

from core.api.serializers import ArticlesSerializer
from  core.models import Article
from .serializers import ArticlesSerializer




# here we using all view in one
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer










# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
#     )





# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer



# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer



# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer



# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer



# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer