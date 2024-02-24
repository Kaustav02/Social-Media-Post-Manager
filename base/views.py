from django.shortcuts import render , redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic.edit import CreateView , UpdateView , DeleteView , FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from .serializer import OrderSerializer
from django.core import serializers

from django.urls import reverse_lazy


# Create your views here.


class Register(FormView):
    template_name='base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts')
    
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Register, self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super(Register,self).get(*args,**kwargs)
    
    
    
    




class CustomLogin(LoginView):
    template_name='base/login.html'
    fields ='__all__'
    redirect_authenticated_user=True
    
    
    def get_success_url(self):
        return reverse_lazy('posts')
    



class CreatePost(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','description','like_count','share_count']
    success_url = reverse_lazy('posts')
    
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'like_count', 'share_count']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdatePost, self).form_valid(form)

class DeltePost(LoginRequiredMixin,DeleteView):
    model=Post
    context_object_name='posts'
    success_url = reverse_lazy('posts')


class PostView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name='base/post.html'
    
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        return context
    

class PostDetail(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post_details'
    fields = '__all__'    


def pivot_data(request):
    dataset = Post.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})