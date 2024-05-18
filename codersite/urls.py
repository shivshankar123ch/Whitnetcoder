
from django.urls import path
from  .import views


urlpatterns =[
    path('',views.index,name="index"),
    path('index',views.index,name="index"),

    path('about',views.about,name="about"),
    path('contact',views.contact_info,name="contact"),
    path('services',views.services,name="services"),
    
    path('java',views.java,name="java"),
    path('html',views.html,name="html"),
    path('css',views.css,name="css"),
    path('javas',views.javas,name="javas"),
    path('sql',views.sql,name="sql"),
    path('python',views.python,name="python"),
    path('php',views.php,name="php"),
    
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	

    path('fresher',views.fresher,name="fresher"),
    path('professional',views.professional,name="professional"),
    path('softskills',views.softskills,name="softskills"),

    path('incompany',views.incompany,name="incompany"),
    path('inplant',views.inplant,name="inplant"),
    path('internship',views.internship,name="internship"),
    path('virtual',views.virtual,name="virtual"),
    path('elearning',views.elearning,name="elearning"),
    path('overview',views.overview,name="overview"),
    path('hrservices',views.hrservices,name="hrservices")
]