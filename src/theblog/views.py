#from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView, UpdateView , DeleteView
from .models import Post ,category,Comment
from .forms import PostForm , EditForm,CatForm,CommentForm
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect

# def home (request):
#     return render(request,'home.html',{})





def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


    def get_context_data(self, *args, **kwargs):
        cat_menu = category.objects.all()
        context = super(HomeView,self).get_context_data()
        context['cat_menu'] = cat_menu
        return context



def CategoryView(request,cats):
    Category_Post = Post.objects.filter(category=cats.replace('-',' '))
    return render (request,'categories.html',{'cats':cats.title().replace('-',' ') , 'Category_Post':Category_Post})




class ArticleDetailView(DetailView):
    model = Post
    template_name = 'ArticleDetailView.html'
        
    def get_context_data(self, *args, **kwargs):
        cat_menu = category.objects.all()
        context = super(ArticleDetailView,self).get_context_data()
        
        stuff = get_object_or_404(Post , id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context





class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'



class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')




class AddCategoryView(CreateView):
    model = category
    form_class = CatForm
    template_name = 'add_category.html'
    
    


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super ().form_valid(form)

    success_url = reverse_lazy('home')

    
