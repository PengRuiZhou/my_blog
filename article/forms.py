from django import forms  # 引入表单类
from .models import ArticlePost  # 引入文章模型

class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含字段
        fields = ('title', 'body')  # created, updated自动生成， author暂定为管理员