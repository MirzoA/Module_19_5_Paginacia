from django.shortcuts import render

from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index1(request):
    posts=Post.objects.all().order_by('-created_at')

    paginator=Paginator(posts, 3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    print(page_number)
    print(page_obj.object_list.count())
    contex={
        'page_obj':page_obj,

    }
    return render(request, 'index1.html', contex)



def listing(request):

    posts=Post.objects.all().order_by('-created_at')
    page_num = request.GET.get('page', 1)
    pag_step = request.GET.get('pag_step', 3)

    len_post = posts.count()+1
    paginator = Paginator(posts, pag_step)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    context = {
        "page_obj": page_obj,
        'len_post': range(1, len_post),
        'pag_step': pag_step,
    }
    return render(request, 'index2.html', context)