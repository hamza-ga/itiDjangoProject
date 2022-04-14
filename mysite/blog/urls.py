from django.urls import path
#from . import views
from .views import HomeView, PostView , AddPostView, EditPostView, DeletPostView, AddCategoryView , category_view, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('addcategory/', AddCategoryView.as_view(), name='addcategory'),
    path('post/edit/<int:pk>/', EditPostView.as_view(), name='editpost'),
    path('post/delete/<int:pk>/', DeletPostView.as_view(), name='deletepost'),
    path('category/<str:category>/', category_view , name = 'category'),
    path('like/<int:pk>/', LikeView , name = 'like_post'),
]