from .TakeData import TakeData
from main.models import TestProjects

def sqlRequest(data):
    dt = TakeData()
    dt.createURL(data['gizmo'], data['link'])
    print(dt.url)
    if dt.sentRequest(): 
        # print(dt.data)
        linkId = TestProjects.objects.get(link=data['link'])
        print(linkId.id)
        dt.createData(linkId.id, data['userList'])
        print("Длина вставляемых данных - ", len(dt.insertingData))
        counter = dt.makeSQLInsert()
        return counter
    
