import math
import flet as ft

colors = {
    "primary": "#6299D0",
    "second": ""
}

class Storage_data():
    def __init__(self, page: ft.Page):
        self.page = page

        self.history_list = page.client_storage.get("history_list") if page.client_storage.get("history_list") else []


    # def set_history(self, list):
    #     self.page.history_list
    
    # def get_history(self):
    #     return self.page.history_list

# history_list = [
    # {
    #     "V":i,
    #     "A":i,
    #     "W":i,
    #     "Ω":i,
    #     "star":False
    # } for i in range(10)
# ]

# storage_data = Storage_data()