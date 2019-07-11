from django.urls import path

from api.views.posts.post_CRUD_views import PostDetailsView, PostView
from api.views.posts.post_gallery_views import GalleryView
from api.views.users.authentication_views import SignInView, SignUpView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
    path('posts', PostView.as_view(), name='posts'),
    path('posts/<int:post_id>', PostDetailsView.as_view(), name='post-details'),
    path('gallery', GalleryView.as_view(), name='gallery')
]
