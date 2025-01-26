# 引入重定向模块
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
# 引入表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User

from .models import ArticlePost

import markdown

def article_list(request):
    articles = ArticlePost.objects.all()
    context = {"articles": articles}
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html格式
    article.body = markdown.markdown(article.body, 
                                     extensions=[
                                        # 包含缩写、表格等常用扩展
                                        'markdown.extensions.extra',
                                        #  语法高亮扩展
                                        'markdown.extensions.codehilite',
                                     ])
    context = {"article": article}
    return render(request, 'article/detail.html', context)

def article_create(request):
    # 判断是否提交数据
    if request.method == 'POST':
        # 将提交数据赋值给表单实例
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断是否满足模型需求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交
            new_article = article_post_form.save(commit=False)
            # 指定id=1的用户作为作者
            new_article.author = User.objects.get(id=1)
            # 将新文章保存数据库
            new_article.save()
            # 完成后返回至文章列表
            return redirect('article:article_list')
        else:
            return HttpResponse("内容有误，请重新填写")
    # GET method
    else:
        # 用户请求获取数据
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {"article_post_form": article_post_form}
        return render(request, 'article/create.html', context)
    
def article_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")