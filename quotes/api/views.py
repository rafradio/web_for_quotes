from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from main.models import TestUsers
from .workWithDB import sqlRequest

@api_view(['GET', 'POST'])
def getData(request):
    dictTest = {'records': 0, 'fetched': 0}
    if request.method == 'POST':
        data = request.data
        testUser = TestUsers.objects.get(name=data['userList'][0])
        testUserList = list(map(lambda x: TestUsers.objects.get(name=x).id, data['userList']))
        data['userList'] = testUserList
        print("request = ", data['userList'])
        # print("user = ", testUser.id)
        # print("user = ", testUserList)
        print("user = ", data['gizmo'])
        counter, fetched = sqlRequest(data)
        print("Вставлено - ", counter)
        dictTest['records'] = counter
        dictTest['fetched'] = fetched
        
    return Response(dictTest)