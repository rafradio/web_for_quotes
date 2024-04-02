from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from main.models import TestUsers
# from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def getData(request):
    dictTest = {'name': 'Rafael', 'age':'50'}
    if request.method == 'POST':
        data = request.data
        testUser = TestUsers.objects.get(name=data['userList'][0])
        testUserList = list(map(lambda x: TestUsers.objects.get(name=x).id, data['userList']))
        print("request = ", data['userList'])
        print("user = ", testUser.id)
        print("user = ", testUserList)
        
    return Response(dictTest)