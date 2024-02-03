from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Article
from .forms import ArticleForm


def _index(request):
    articles = Article.objects.all()
    html_str = ''
    for article in articles:
        html_str += f"<h1>{article.title} ({article.id})</h1>"
    return HttpResponse(html_str)


def articles_list(request):
    query = request.GET.get('q')

    articles = Article.objects.search(query=query)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    page_qs = paginator.get_page(page_number)
    # try:
    #     int(query)
    # except:
    #     lookups = Q(title__icontains=query)
    # else:
    #     lookups = Q(title__icontains=query) | Q(id=query)
    # if query:
    #     # articles = Article.objects.filter(title__exact=query)
    #     articles = Article.objects.filter(lookups)
    context = {
        'object_list': page_qs,
    }
    return render(request, 'article/index.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'object': article
    }
    return render(request, 'article/detail.html', context)


def article_create(request):
    context = {
        'created': False
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        obj = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['object'] = obj
        messages.success(request, f'Article {obj.title} successfully created')
    return render(request, 'article/create.html', context)


def article_create_form(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'Article "{obj.title}" successfully created')
            reverse_url = reverse('article:detail', args=[obj.id])
            return redirect(reverse_url)
    context = {
        'form': form
    }
    return render(request, 'article/create_form.html', context)


def article_create_form_(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        obj = form.save()
        reverse_url = reverse('article:detail', args=[obj.id])
        return redirect(reverse_url)
    context = {
        'form': form
    }
    return render(request, 'article/create_form.html', context)


def article_change(request, pk):
    obj = Article.objects.get(id=pk)
    form = ArticleForm(instance=obj)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=obj, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Article "{obj.title}" successfully edited')
            reverse_url = reverse('article:change-form', kwargs={"pk": obj.id})
            return redirect(reverse_url)
    context = {
        'form': form,
        'object': obj,
    }
    return render(request, 'article/edit.html', context)

@login_required(login_url='auth:login')
@permission_required(perm="request.user.is_admin", login_url='/', raise_exception="You have no enough permission to delete")
def article_delete(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, f'Article "{obj.title}" successfully deleted')
        return redirect('article:list')
    context = {
        'object': obj
    }
    return render(request, 'article/delete.html', context)


"""
DRY - Dont Repeat Yourself
"""
