from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.conf import settings
from .models import Post,subscriber

from django.core.mail import send_mail
from django.contrib import messages
from .forms import  subscribeForm


def post_list_view(request):

    object_list = Post.published.all()    
    paginator = Paginator(object_list, 4) # 4 posts in each page   
    page = request.GET.get('page')
    try:      
        posts = paginator.page(page)
    except PageNotAnInteger:    # If page is not an integer deliver the first page
        posts = paginator.page(1)    
    except EmptyPage:        # If page is out of range deliver last page of results        
        posts = paginator.page(paginator.num_pages)

    
    if request.method == 'POST':
        form = subscribeForm(data=request.POST)

        if form.is_valid():
            message = form.save(commit=False)

            if subscriber.objects.filter(Email = message.Email).exists():
                messages.warning(request,  "Your Email already exists in our Databases")
            else:
                message.save()

                Name = request.POST.get( 'Name', '')
                Email = request.POST.get( 'Email', '') 
                Subject = 'Welcome to Patrick Blog'
                message = 'Dear %s \nWelcome to my blog, Thanks for Subscribing to our mail.\n By signing up you agree with our terms and Conditions where they apply. ' %(Name)
                emailFrom =  settings.EMAIL_HOST_USER 
                emailTo =  Email 
                
                
                send_mail(Subject,message,emailFrom,[emailTo],fail_silently=True)
                
                messages.success(request,  "You Successfully subscribed")

        return redirect('/blog')
    else:
        form = subscribeForm() 

    return render(request,'blog/list.html',{'page': page,'form':form,'posts': posts})

def post_detail_view(request, year, month, day, post):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # 4 posts in each page   
    page = request.GET.get('page')
    
    try:      
        posts = paginator.page(page)
    except PageNotAnInteger:    # If page is not an integer deliver the first page
        posts = paginator.page(1)    
    except EmptyPage:        # If page is out of range deliver last page of results        
        posts = paginator.page(paginator.num_pages)
        
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/detail.html', {'post': post,'posts': posts})

 
