#Esta librería se encarga de obtener los datos de TheGuardian
#
#
#

from theguardian import theguardian_content
from datetime import datetime, timedelta

class TheGuardianNews:

    def __init__(self):
        self.content = []
        self.headers = []
        self.result = []
        self.newsData = []
        self.mainHeader = []

    def getData(self, fromDate, section):

        # create content
        self.content = theguardian_content.Content(api='test')


        # create content with filters
        # for more filters refer
        # http://open-platform.theguardian.com/documentation/search

        self.mainHeader = {
            "section": section,
            "from-date": fromDate,
            "order-by": "relevance",
            "page-size": 200,
            "show-fields": "sectionName,webTitle,webUrl,short-url",
        }
        headers = self.mainHeader
        self.content = theguardian_content.Content(api='test', **headers)

        #res = self.content.get_content_response()
        #self.result = self.content.get_results(res)

    def transforData(self):
        #STEP 1: Obtener el número de páginas
        auxContent = self.content.response_headers()
        totalPages = auxContent['pages']
        headers = self.mainHeader        
        anotherContent = theguardian_content.Content(api='test', **headers)

        #STEP 2: Barrer página por página
        for page in range(1, totalPages + 1):
            res = anotherContent.get_content_response(headers={'pages': page})
            self.result = anotherContent.get_results(res)
            pageData = []
            for i in range (0, len(self.result)):
                element = []
                refDate = self.result[i]['webPublicationDate']
                newString = ""  
                for x in refDate:
                    if x != 'T':
                        newString = newString + x
                    else:
                        break
            
                sectionName = self.result[i]['sectionName']
                webTitle = self.result[i]['webTitle']
                webUrl = self.result[i]['webUrl']
                element.insert(0, refDate)
                element.insert(1, sectionName)
                element.insert(2, webTitle)
                element.insert(3, webUrl)
                pageData.append(element)
            self.newsData.append(pageData)
            ###print(page)

    def transformDataByDate(self, fromDate, section):
        
        toDate = fromDate
        hoy = datetime.now().date()
        #print(hoy)
        endDate = datetime.strptime(fromDate,"%Y-%m-%d").date()

        ##Get the information day by day
        while endDate <= hoy:
            try:
                # create content
                self.content = theguardian_content.Content(api='test')
        
                # create content with filters
                # for more filters refer
                # http://open-platform.theguardian.com/documentation/search
            
                self.mainHeader = {
                    "section": section,
                    "from-date": toDate,
                    "to-date": toDate,
                    "order-by": "relevance",
                    "page-size": 20,
                    "show-fields": "sectionName,webTitle,webUrl,short-url",
                }
                headers = self.mainHeader
                self.content = theguardian_content.Content(api='test', **headers)
                res = self.content.get_content_response()
                self.result = self.content.get_results(res)
                try:
                    #Convert data from DataFrame to Vector of TUPLAS
                    for i in range (0, len(self.result)):
                        element = []
                        refDate = self.result[i]['webPublicationDate']
                        newString = ""  
                        for x in refDate:
                            if x != 'T':
                                newString = newString + x
                            else:
                                break
                        sectionName = self.result[i]['sectionName']
                        webTitle = self.result[i]['webTitle']
                        webUrl = self.result[i]['webUrl']
                        element.insert(0, newString)
                        element.insert(1, sectionName)
                        element.insert(2, webTitle)
                        element.insert(3, webUrl)
                        self.newsData.append(element)
                except:
                    print("Problemas con la carga de datos.")
                    print("Dato: ", i)
                    print("Último elemento en la matriz: ")
                    print(self.newsData[i-1])
            except:
               print("Problemas con la recepción de los datos.") 
            #Next day
            i = 0
            #endDate = datetime.strptime(fromDate,"%Y-%m-%d").date()
            endDate = endDate + timedelta(days=1)
            toDate = endDate.strftime("%Y-%m-%d")




    def __del__(self):
        self.content = []
        self.headers = []
        self.result = []
        self.newsData = []
