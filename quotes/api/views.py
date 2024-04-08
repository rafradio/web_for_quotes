from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from main.models import TestUsers
from main.MyLogger import MyLogger
from .workWithDB import sqlRequest

@api_view(['GET', 'POST'])
def getData(request):
    clientip = f'{request.get_full_path()}; {request.headers["User-Agent"]}; {request.method};'
    d = {'clientip': clientip}
    MyLogger.logger.info('Api request', extra = d)
    dictTest = {'records': 0, 'fetched': 0, 'message': 0}
    if request.method == 'POST':
        data = request.data
        clientip = f'{data['link']}; {data['gizmo']};'
        d = {'clientip': clientip}
        MyLogger.logger.info('alchemer request details', extra = d)
        # testUser = TestUsers.objects.get(name=data['userList'][0])
        testUserList = list(map(lambda x: TestUsers.objects.get(name=x).id, data['userList']))
        data['userList'] = testUserList
        counter, fetched, message = sqlRequest(data)
        dictTest['records'] = counter
        dictTest['fetched'] = fetched
        dictTest['message'] = message
        
    return Response(dictTest)