from django.contrib import admin
from django.urls import path,include
from blogapp.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', BlogListView, name='blogs'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
    # path('delete/',DeleteView,name='delete'),
]