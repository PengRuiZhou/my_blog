from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    # 注意<int:id>之间不能有空格，如果后续还有传入参数，在<int:id>/后面继续写
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_delete/<int:id>/', views.article_delete, name='article_delete'),
]
