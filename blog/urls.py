from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexListView.as_view(), name="index"),
    #path('about/<int:page>', views.about, name="about"),
    path('about/<int:page>/', views.AboutTemplateView.as_view(), name="about"),
    #path('post/<int:page>/', views.post, name="post"),
    path('contact/<int:page>/', views.contact, name="contact"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-post-delete'),
]
