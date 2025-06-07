from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from . models import Blog
from django.contrib import messages
from django.views.generic import \
    (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
#def index(request):
  #  blogs = Blog.objects.all()
 #   content = {'title': 'Home Django Blog',
 #              'blogs': blogs}
 #   return render(request, 'blog/index.html', content)



class IndexListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'Ing. Pedro´s blog'}
    ordering = ["-post_created"]
    template_name = 'blog/index.html'
    paginate_by = 3


class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    extra_context = {'title': 'View Post'}



class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/blog_form.html'
    permission_denied_message = 'Restricted access!'
    extra_context = {'button_name': 'create',
                     'title': 'Create Post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = 'Post created successfully!!!'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)


#def about(request,page):
  #  content = {'title': 'Home Django About',
 #              'page': '2'}
 #   return render(request, 'blog/about.html', content)


class AboutTemplateView(TemplateView):
    extra_context = {'title': 'Home Django About',
               'page': '2'}
    template_name = 'blog/about.html'


#def post(request,page):
  #  content = {'title': 'Home Django Post',
  #             'page': '3'}
 #   return render(request, 'blog/post.html', content)


def contact(request,page):
    content = {'title': 'Home Django Contact',
               'page': '4'}
    return render(request, 'blog/contact.html', content)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/blog_form.html'
    permission_denied_message = 'Restricted access!'
    extra_context = {'button_name': 'update',
                     'title': 'Update Post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = 'Post updated successfully!!!'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('index')
    template_name = 'blog/blog_confirm_delete.html'
    context_object_name = 'object'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False