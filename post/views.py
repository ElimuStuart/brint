from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views import View

from .models import Post
from .forms import PostForm

class PostList(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(FormView):
    template_name = 'post/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post:post_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('post:post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post_list')





