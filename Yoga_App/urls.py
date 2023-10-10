from django.urls import path
from Yoga_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='handleLouout'),
    path('check-BMI/', views.checkBMI, name='checkBMI'),
    path('result-BMI/', views.resultBMI, name='BMIResult'),
    path('home/', views.home, name='home'),
    path('update/<int:num>/', views.updateRecord, name='update'),
    path('home/help/', views.help, name='help'),
    path('home/contact/', views.contact, name='contact'),
    path('home/yoga-poses/', views.yogaPoses, name='yogaPoses'),
    path('home/yoga-for-women/', views.yogaForWomen, name='yogaForWomen'),
    path('home/yoga-for-men/', views.yogaForMen, name='yogaForMen'),
    path('home/profile/', views.profile, name='profile'),
    path('home/about/', views.about, name='aboutus'),
    path('home/yoga-for-disease/<str:bimari>', views.yogaForDisease, name='yogaForDisease'),
    path('home/search/', views.search, name='search'),
    # path('saraju/', views.saraju)
]