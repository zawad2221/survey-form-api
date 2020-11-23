from rest_framework import serializers
from .models import FormData, Answer



class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['questionNumber','answer']

class FormSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    answers = AnswerSerializer(read_only=True,many=True)

    class Meta:
        model = FormData
        fields  = ['id', 'email', 'age', 'gender', 'height', 'weight', 'answers', 'mark']
    
    # def create(self, validated_data):
    #     answer = Answer.objects.get(pk=validated_data.pop('answers'))
    #     instance = FormData.objects.create(**validated_data)
    #     return instance

    depth = 2
    read_only_fields = ('answer')