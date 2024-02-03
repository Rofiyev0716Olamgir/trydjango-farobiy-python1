import random
from django.shortcuts import HttpResponse
from article.models import Article


def hello(request):
    obj_id = random.randint(1, 5)
    print("hello functions is working..")
    print(obj_id)
    article = Article.objects.get(id=obj_id)
    title = f"<h1>{article.title} ({article.id})</h1>"
    content = f"<p>{article.content}</p>"
    html_str = title + content
    return HttpResponse(html_str)
