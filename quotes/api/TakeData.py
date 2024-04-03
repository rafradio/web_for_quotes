import requests
from main.models import TestQuotas

class TakeData():
    def __init__(self) -> None:
        self.url = ""
        self.insertingData =[]
        self.data = None
        
    def createURL(self, *args):
        with open('api/data/data.txt') as f:
            data = [line.rstrip() for line in f]
        
        if args[0] == "sokolinskaya": self.url = data[0][:35] + args[1] + data[0][42:] 
        if args[0] == "korenev": self.url = data[1][:35] + args[1] + data[1][42:]
        
    def sentRequest(self):
        # return True
        r = requests.get(self.url)
        print(r.ok)
        if r.ok: 
            self.data = r.json()
            print("Длина данных из alchemy = ", len(self.data['quotas']))
            return True
        else: return False
        
    def createData(self, projectId, users):
        for user in users:
            for line in self.data['quotas']:
                # string = unicodedata.normalize("NFKD", line['name'])
                string = line['name'].replace(u'\xa0', u'')
                newLine = (line['id'], string, projectId, user)
                self.insertingData.append(newLine)
                
    def makeSQLInsert(self):
        last = TestQuotas.objects.latest('id')
        for line in self.insertingData:
            record = TestQuotas(
                link=line[0],
                title=line[1],
                prj_id=line[2],
                user_id=line[3])
            record.save()
        last1 = TestQuotas.objects.latest('id')
        return int(last1.id) - int(last.id)
            
                
    
        
        
    