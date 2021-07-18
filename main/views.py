from django.shortcuts import render
from .apps import AisentimentanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializer import MessageSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


import pickle as pkl

file1 = "models.pkl"
fileobj1 = open(file1, 'rb')
data = pkl.load(fileobj1)
model = data['model']
vectorizer = data['vectorizer']


class call_model(APIView):

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            # text = 'the movie is good'
            text = request.data['message']

            vector = vectorizer.transform([text])
            predction = model.predict(vector)[0]

            response = {'text_sentiment': predction}
            return Response(response)
        return Response(serializer.errors)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer


def register(request):
    if request.method == 'POST':
        message = request.POST['message']


        vector = vectorizer.transform([message])
        predction = model.predict(vector)[0]

        response = {'text_sentiment': predction}
        #print(predction, message)
        #return HttpResponse(response)
        messages.info(request, predction)
        return redirect('register')


    else:
        return render(request, 'index.html')
