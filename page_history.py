from settings import *

class Table():
    star_select = False
    def __init__(self, page: ft.Page):
        self.page = page
        self.create_table()
        self.update()

    def create_table(self):
        self.tableHistory = ft.DataTable(
            columns=[
                ft.DataColumn(ft.IconButton(icon="NUMBERS_OUTLINED")),
                ft.DataColumn(ft.Text("Позн", size=20)),
                ft.DataColumn(ft.Text("Знач", size=20)),
                ft.DataColumn(ft.IconButton(icon="DELETE")),
            ],
            data_row_max_height=120,
            horizontal_lines=ft.border.BorderSide(1, "#096c05"),
            bgcolor="#99000000",
        )

    def only_star(self):
        self.star_select = not self.star_select
        self.update()

    def delete(self, index):
        self.page.storage_data.history_list.pop(index)
        self.update()

    def star(self, index):
        self.page.storage_data.history_list[index]["star"] = not self.page.storage_data.history_list[index]["star"]
        self.update()

    def update(self):
        self.tableHistory.rows = []
        for index, history in enumerate(reversed(self.page.storage_data.history_list)): 
            index = len(self.page.storage_data.history_list) - index - 1 
            if self.star_select == False or self.star_select == history["star"]:
                self.tableHistory.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Column([
                                    ft.Text(f"{index+1}.", size=20),
                                    ft.IconButton(
                                        icon="STAR" if history["star"] else "STAR_BORDER", 
                                        icon_color="yellow" if history["star"] else "", 
                                        on_click=lambda _, 
                                        idx=index: self.star(idx)
                                    )
                                ])
                            ),
                            ft.DataCell(ft.Text("\n".join(v for v in history), size=20)),
                            ft.DataCell(ft.Text("\n".join(str(v) for v in history.values()), size=20)),
                            ft.DataCell(ft.IconButton(icon="DELETE", on_click=lambda _, idx=index: self.delete(idx))),
                        ],
                    ) 
                ) 
        # print("встановити1",self.page.client_storage.get("history_list"))
        # print("встановити2",self.page.storage_data.history_list)
        self.page.client_storage.set("history_list", self.page.storage_data.history_list)
        # print("завершити встановити",self.page.client_storage.get("history_list"))
        self.page.update()

def page_history(page: ft.Page):
    page.change_star_button_status = False
    def change_star_button_click():
        change_star_button.icon = "STAR" if not page.change_star_button_status else "STAR_BORDER"
        change_star_button.icon_color = "yellow" if not page.change_star_button_status else "default"
        page.change_star_button_status = not page.change_star_button_status
        page.datatable.only_star()

    change_star_button = ft.IconButton(
        icon="STAR_BORDER", 
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: "white",
            },
            bgcolor={
                ft.MaterialState.DEFAULT: colors["primary"],
            },
        ),
        icon_size=50,
        on_click=lambda _: change_star_button_click(),
    )

    return ft.Stack(
        [
            ft.Column(
                [
                    ft.Container(
                        content=page.datatable.tableHistory,
                        width=page.width,
                    ),
                ],
                scroll=True,
            ),
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=change_star_button,
                                padding=40,
                                bgcolor="FF0000",
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        ]
    )
    # return ft.Column(
    #     [
    #         ft.Container(
    #             content=page.datatable.tableHistory,
    #             width=page.width,
    #         ),
    #     ],
    #     scroll=True,
    # )