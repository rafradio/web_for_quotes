from .TakeData import TakeData
from main.models import TestProjects
from main.MyLogger import MyLogger

def sqlRequest(data):
    dt = TakeData()
    dt.createURL(data['gizmo'], data['link'])

    if dt.sentRequest(): 
        if data['typeOfProject'] == "new": 
            record = TestProjects(
                link=data['link'],
                title=data['title'],
                ac_gizmo=data['gizmo']
            )
            record.save()
            TestProjects.objects.latest('id')
            clientip = f'Вставлен в БД новый проект; {data['link']}; Название; {data['title']};'
            d = {'clientip': clientip}
            MyLogger.logger.info('DB Work New project', extra = d)
            
        linkId = TestProjects.objects.get(link=data['link'])
        dt.createData(linkId.id, data['userList'])
        print("Длина вставляемых данных - ", len(dt.insertingData))
        clientip = f'Вставлено в БД записей; {len(dt.insertingData)}; Колличество из alchemer; {len(dt.data['quotas'])}; {data['gizmo']};'
        d = {'clientip': clientip}
        MyLogger.logger.info('DB Work', extra = d)
        counter, fetched = dt.makeSQLInsert()
        return counter, fetched, 1
    else:
        clientip = f'Данные не вставлены; {data['gizmo']};'
        d = {'clientip': clientip}
        MyLogger.logger.info('DB Work', extra = d)
        return 0, 0, 0
    
