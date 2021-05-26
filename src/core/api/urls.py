from django import urls
from django.urls import path
from rest_framework.generics import UpdateAPIView


from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='core')
urlpatterns = router.urls




# from core.models import Article
# from .views import (
#     ArticleListView,
#     ArticleDetailView,
#     ArticleCreateView,
#     ArticleDeleteView,
#     ArticleUpdateView,
    
# )



# urlpatterns = [
#     path('',ArticleListView.as_view()),
#     path('create/',ArticleCreateView.as_view()),
#     path('<pk>/delete/',ArticleDeleteView.as_view()),
#     path('<pk>/update/',ArticleUpdateView.as_view()),
#     path('<pk>',ArticleDetailView.as_view()),
# ]