
from django.urls import path
from .views import ProfileDetailView, ProfileEditView, ProfileUserView,UserLoginView, UserRegisterView, UserLogoutView





urlpatterns = [


# path('register/', RegistrationFormView.as_view(), name='user_register'),
path('profile/detail/', ProfileDetailView.as_view(), name='profile_detail',),
path('profile/create/', ProfileUserView.as_view(), name='profile_create'),
path('profile/update/', ProfileEditView.as_view(), name='profile_edit'),

# login & logout urls
path('login/', UserLoginView.as_view(), name='login'),
path('register/', UserRegisterView.as_view(), name='register'),
path('logout/', UserLogoutView.as_view(), name='logout'),



]
