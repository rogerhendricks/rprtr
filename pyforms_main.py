import re
import getData
from jinja2 import Environment, FileSystemLoader
#from weasyprint import HTML
import subprocess
import sqlite3
import datetime
# Importing pyforms widgets
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls import ControlButton

class Rprtr_Window (BaseWidget):

    def __init__(self, *args, **kwargs) -> None:
        super(Rprtr_Window, self).__init__('Rprtr Device Form')

        self._fullName = ControlText('Full Name', 'Unkown')
        self._manufacturer = ControlText('Manufacturer', 'Unkown')

        self._formset = [{
            'Tab1':['_fullName', '||','_manufacturer'],
            'Tab2':[],
        },    
        ]


        def __openEvent(self):
            pass

        def __saveEvent(self):
            pass

        def __editEvent(self):
            pass

        def __pastEvent(self):
            pass


        # self.mainmenu = [
        #     { 'File': [
        #             {'Open': self.__openEvent},
        #             '-',
        #             {'Save': self.__saveEvent},
        #             {'Save as': self.__saveAsEvent}
        #         ]
        #     },
        #     { 'Edit': [
        #             {'Copy': self.__editEvent},
        #             {'Past': self.__pastEvent}
        #         ]
        #     }
        # ]
if __name__ == "__main__":
    from pyforms import start_app
    start_app(Rprtr_Window)