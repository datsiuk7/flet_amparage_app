from settings import *
from page_settings import *
from page_history import *
from page_home import *
from settings import *

def main(page: ft.Page):
    page.title = "Amperage App"

    def start_app():
        page.client_storage.set("ThemeMode", "LIGHT")
        page.storage_data = Storage_data(page)
        
    
    start_app()

    if not hasattr(page, 'datatable'):    
        page.datatable = Table(page)
    else:
        page.datatable.create_table()
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        divider_color=colors["primary"],
        indicator_color="green",
        unselected_label_color=colors["primary"],
        label_color="green",
        tabs=[
            ft.Tab(
                icon=ft.icons.HISTORY,
                content=page_history(page),
                
            ),
            ft.Tab(
                icon=ft.icons.HOME,
                content=page_home(page)
            ),
            ft.Tab(
                icon=ft.icons.SETTINGS,
                content=page_settings()
            ),
        ],
        scrollable=False,
        expand=1,
    )

    page.padding = 0
    page.add(
        ft.Container(
            image_src='./images/background.png',
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=ft.SafeArea(
                ft.Container(
                    t,
                ),
                expand=True
            ),
            margin=0,
            padding=0,
            
        ),
    )

ft.app(main)