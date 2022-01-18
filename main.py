
import os

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from gui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
import webbrowser
global icao
icao = "aaaa"
taxiing_map = f"1-ad2-rus-{icao}-031-031"
import sys
# global icao
# global taxiing_map
# global url
class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        global ui
        
        self.ui = Window()
        self.ui.setupUi(self)
        self.icao = "uuee"
        self.main_page = False
        
        
        self.url = f"http://www.caiga.ru/common/AirInter/validaip/aipsource1/aip/ad/ad2/{self.icao}/"
        self.folder_location = r'/Users/aleksandrlupij/🐍Python🐍/Charts-Parser/pdfs_uuww'
        if not os.path.exists(self.folder_location):os.mkdir(self.folder_location)
    def GetMetar(self,ICAO=""):
        ICAO = str(ICAO).upper()
        print(ICAO)
        url_metar = f"https://metartaf.ru/{ICAO}"
        print(url_metar)
        response = requests.get(url_metar)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            quotes = str(soup.find_all('pre')[0]).replace("<pre>", "").replace("</pre>", "")
        except Exception as e:
            print(e)
        metar_text = quotes #[20:]
        print(metar_text)
        self.setMetar(metar_text)
        quotes = []
        metar_text = ""
        MainWindow.getPDF(MainWindow, ICAO.lower())
        # self.ui.graphicsView.load(QUrl(f"http://www.caiga.ru/common/AirInter/validaip/aipsource1/aip/ad/ad2/{self.icao}/"))
    #If there is no such folder, the script will create one automatically
    
    def getPDF(self,ICAO=""):
        taxiing_map = f"1-ad2-rus-{ICAO}-031-031"
        self.url = f"http://www.caiga.ru/common/AirInter/validaip/aipsource1/aip/ad/ad2/{ICAO}/"
        response = requests.get(self.url)
        soup= BeautifulSoup(response.text, "html.parser")     
        self.folder_location = r'/Users/aleksandrlupij/🐍Python🐍/Charts-Parser/pdfs_uuww'
        if not os.path.exists(self.folder_location):os.mkdir(self.folder_location)
        for link in soup.select("a[href$='.pdf']"):
            
            if taxiing_map in link["href"]:
                try:
            #Name the pdf files using the last portion of each link which are unique in this case
                    filename = os.path.join(self.folder_location,link['href'].split('/')[-1])
                    # with open(filename, 'wb') as f:
                    #     f.write(requests.get(urljoin(self.url,link['href'])).content)
                    print(requests.get(urljoin(self.url,link['href'])))
                    webbrowser.open(f"{urljoin(self.url,link['href'])}", new=0, autoraise=True)
                except Exception as e:
                    print(e)
                # break
            elif MainWindow.main_page:
                webbrowser.open("http://www.caiga.ru/common/AirInter/validaip/html/rus.htm", new=0, autoraise=True)

        # print(self.GetMetar(self.icao))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())