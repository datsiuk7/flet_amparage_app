from settings import *

def page_settings():
    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Empty"),
                        # ft.Text("Theme"),
                        # ft.Switch(value=bool(page.theme_mode == ft.ThemeMode.LIGHT), on_change=changeTheme)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    
                ),
            ]
        ),
        margin=ft.margin.only(top=20),
    )