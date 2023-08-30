from django.urls import path
from .views import ScoreCardViews,RegisterPage,ScoreCardList

urlpatterns = [
    #     path('login/',CustomLoginView.as_view(),name='login'),
    # path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
     path('register/',RegisterPage.as_view(),name='register'), 
     path('',ScoreCardList.as_view(),name="scorecards"),
     path('clients/<str:pk>/',ScoreCardViews.as_view() ,name='client'),
]
