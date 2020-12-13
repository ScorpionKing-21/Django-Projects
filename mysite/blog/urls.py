from django.urls import path, include
from . import views

app_name='blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('about/',views.AboutView.as_view(), name="about"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post_remove"),
    path('drafts/', views.DraftPostView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name="comment"),
    path('comment/<int:pk>/approve/', views.comment_approve, name="comment_approve"),
    path('comment/<int:pk>/delete/', views.comment_remove, name="comment_remove"),
    path('post/<int:pk>/publish', views.post_publish, name="post_publish"),
]