from django.shortcuts import render
from .models import FormData, Answer
from .serializers import FormSerializer, AnswerSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def getFormData(request):

    if request.method == "GET":
        formData = FormData.objects.all()
        formDataSerializer = FormSerializer(formData,many=True)
        return JsonResponse(formDataSerializer.data,safe=False,status=200)
    data={
        "response":"failed"
    }
    return JsonResponse(data,safe=False,status=400)   

@csrf_exempt
def saveResponse(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        print(data)
        responseSerializer = FormSerializer(data=data)
        if responseSerializer.is_valid():
            responseSerializer.save()
            responseId=responseSerializer.data['id']
            for answer in data['answers']:
                print("ans: ",answer['questionNumber'],answer['answer'])
                ans = Answer(questionNumber=answer['questionNumber'],answer=answer['answer'])
                ans.save()
                response = FormData.objects.get(id=responseId).answers.add(ans)
            return JsonResponse(responseSerializer.data,status=200)
        return JsonResponse(responseSerializer.errors,status=400)