from rest_framework.decorators import api_view
from rest_framework.response import Response
from .open_ia_service import open_ia_response


@api_view(['GET'])
def hello_world(request):
    return Response("Hello world !!")

@api_view(['GET'])
def hello_epsi(request):
    return Response("Bonjour Epsi !!")

@api_view(['GET'])
def hello_person(request, name):
    return Response(f"Bonjour {name} !!")

@api_view(['POST'])
def addition(request):
    x = request.data.get('x')
    y = request.data.get('y')
    return Response(x + y)

@api_view(['POST'])
def chat_with_gpt(request):
    prompt = request.data.get('prompt')
    return Response(open_ia_response(prompt))

@api_view(['POST'])
def translate(request):
    message = request.data.get('message')
    language = request.data.get('language')
    prompt = f"traduit ce message : '{message}' en {language}"
    return Response(open_ia_response(prompt))




# New Fonctions 


@api_view(['POST'])
def analyze_health(request):
    symptoms = request.data.get('symptoms')
    prompt = f"Analysez vos symptomes : {symptoms}"
    return Response(open_ia_response(prompt))

@api_view(['POST'])
def recommend_medications(request):
    symptoms = request.data.get('symptoms')
    prompt = f"Recommander des médicaments pour vos symptomes : {symptoms}"
    return Response(open_ia_response(prompt))

@api_view(['POST'])
def find_nearest_hospital(request):
    location = request.data.get('location')
    prompt = f"Trouver le plus proche hôpital à votre position : {location}"
    return Response(open_ia_response(prompt))

@api_view(['GET'])
def tips(request, tip):
    prompt = f"Afficher les conseils : {tip}"
    return Response(open_ia_response(prompt))

@api_view(['POST'])
def sommeil(request):
    duree = request.data.get('duree')
    prompt = f"Es-ce un bon sommeil si on dort {duree} heure"
    return Response(open_ia_response(prompt))