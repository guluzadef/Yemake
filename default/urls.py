from django.urls import path
from .views import user_login,verify_view,user_register,cooker_register,Home,add_food,DetailFood
urlpatterns = [
    path('', Home,name='index'),
    path('user_login/', user_login,name='login'),
    path('user_register/', user_register,name='user_register'),
    path('cooker_register/', cooker_register,name='cooker_register'),
    path('verify/<str:token>/<int:id>/', verify_view, name='verify_view'),
    path('user_register/', user_register,name='user_register'),
    path('cooker_register/', cooker_register,name='cooker_register'),
    path('add/', add_food, name="add-food"),
    path('detail/<int:pk>/',DetailFood.as_view(), name="detail-food"),

]

