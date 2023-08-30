from django.urls import path
from .views import ScoreCardViews,RegisterPage,ScoreCardList,CustomLoginView,ScoreCardCreate
from django.contrib.auth.views import LogoutView
urlpatterns = [
     path('login/',CustomLoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
     path('register/',RegisterPage.as_view(),name='register'), 



     path('',ScoreCardList.as_view(),name="scorecards"),
     path('scorecard-create',ScoreCardCreate.as_view(),name='scorecard-create'),
     path('clients/<int:pk>/',ScoreCardViews.as_view() ,name='client'),
]