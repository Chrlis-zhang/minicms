#conding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from news.models import Column,Article


def index(request):
    columns = Column.objects.all()
    return render(request,'index.html',{'columns': columns})


    #return HttpResponse(u'欢迎')


def column_detail(request,column_slug):
    cloumn = Column.objects.get(slug=column_slug)
    return render(request,'column.html',{'column':cloumn})


    #return HttpResponse('column_slug' + column_slug)


def article_detail(request,article_slug,pk):
    #articl = Article.objects.get(slug=article_slug)
    #articl = Article.objects.filter(slug=article_slug)[0]
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article,permanent=True)
    return render(request,'article.html',{'article':article})


    #return HttpResponse('article_slug' + article_slug)