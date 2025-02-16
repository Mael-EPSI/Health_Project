from django.urls import path
from .views import *

urlpatterns = [
    path ('hello-world', hello_world),
    path('hello-epsi', hello_epsi),
    path('hello/<name>', hello_person),
    path('addition', addition),
    path('chat-with-gpt', chat_with_gpt),
    path('translate', translate),
    path('analyze_health', analyze_health),
    path('recommend_medications', recommend_medications),
    path('find_nearest_hospital', find_nearest_hospital),
    path('tips/<tip>', tips),
    path('analyze_sleep', sommeil)
]