from . import views
from django.urls import path


app_name= 'accounts'

urlpatterns = [
    
    path('login/', views.login_view , name='login'),
    path('logout', views.logout_view , name='logout'),
    path('signup/' , views.signup_view , name='signup'),
    path('password_reset', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),


    
    
]    