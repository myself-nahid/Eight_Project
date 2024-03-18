from django.urls import path
from . views import home, signup, user_login, user_logout, profile, pass_change, pass_change2
urlpatterns = [
    path('', home),
    path('signup/', signup, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('passchange/', pass_change, name="passchangee"),
    path('passchange2/', pass_change2, name="passchangee2"),
    path('profile/', profile, name="profile"),
]
