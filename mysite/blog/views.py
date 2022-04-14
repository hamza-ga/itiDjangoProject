from pyexpat import model
from attr import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView , DetailView, CreateView, UpdateView , DeleteView
from .models import Posts , Category
from .forms import PostForm, EditForm

# Create your views here.

class HomeView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    ordering = ['-post_date']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context

class PostView(DetailView):
    model = Posts
    queryset = Posts.objects.all()
    template_name = 'blog/post.html'

    def get_context_data(self,*args, **kwargs):
        post_id = get_object_or_404(Posts, id = self.kwargs['pk'])
        total_likes = post_id.total_likes()
        context = super(PostView, self).get_context_data(*args,**kwargs)

        liked = False
        if post_id.likes.filter(id = self.request.user.id).exists():
            liked = True
            
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'

class EditPostView(UpdateView): 
    model = Posts
    form_class = EditForm
    template_name = 'blog/edit_post.html'
    #fields = ('title', 'category','photo','content')

class DeletPostView(DeleteView):
    model = Posts
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')#to return to the home page after deleting

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'blog/add_category.html'
    fields = '__all__'

def category_view(request, category):
    category_posts = Posts.objects.filter(category = category.replace('-',' '))
    context = {'category': category.title().replace('-',' ') , 'category_posts': category_posts}
    return render(request , 'blog/categories.html',context)

def LikeView(request, pk):
    post = get_object_or_404(Posts, id = request.POST.get('post_id') )
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('post', args = [str(pk)]))
