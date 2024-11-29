from django.urls import path
from . import views


urlpatterns = [
    path('all_hashtags/', views.AllHashtagListView.as_view(), name='all_hashtags_class'),
    path('grand/', views.GrandHashtagListView.as_view(), name='grand_tags'),
    path('young/', views.YoungHashtagListView.as_view(), name='young_tags'),
    path('children/', views.ChildrenHashtagListView.as_view(), name='children_tags'),
]