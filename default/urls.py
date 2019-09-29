from django.urls import path
from .views import index,user_register,cooker_register,Home,add_food
urlpatterns = [
    path('', Home,name='index'),
    path('user_register/', user_register,name='user_register'),
    path('cooker_register/', cooker_register,name='cooker_register'),
    path('add/', add_food, name="add-food"),

]

