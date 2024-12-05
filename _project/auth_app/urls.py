from django.urls import path
from .views import signup, login_view, delete_account

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('delete-account/', delete_account, name='delete'),
]
