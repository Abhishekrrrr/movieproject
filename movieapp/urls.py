from django.urls import path
from. import views
app_name='movieapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('movie/<int:movie_id>/',views.detli,name='detli'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]