from django.shortcuts import render
from post.models import Post

def home(request):
    post=Post.objects.all()
    # print(post)
    # for i in post:
    #     # print(i.category)
    #     for j in i.category.all():
    #         print(j)
    #     # print()
        
    return render(request,'home.html',{'post':post})