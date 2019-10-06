from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.all_posts, name='all_posts'),
    #path('', views.PostListView, name="all_posts"),
    #path('tag/<slug:tag_slug>', ),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
]