
from django.urls import path
from .views import RegistrationFormView, ProfileDetailView, ProfileEditView, ProfileUserView




urlpatterns = [

  
path('register/', RegistrationFormView.as_view(), name='user_register'),
path('profile/detail/', ProfileDetailView.as_view(), name='profile_detail',),
path('profile/create/', ProfileUserView.as_view(), name='profile_create'),
path('profile/update/', ProfileEditView.as_view(), name='profile_edit')

]
