from django.urls import path


from .  import views




urlpatterns = [
    path('store/',views.all_products,name='home'),
    
]



