from settings import *

def update_table():
    table.rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{index+1}.", size=20)),
                ft.DataCell(ft.Text("\n".join(v for v in history), size=20)),
                ft.DataCell(ft.Text("\n".join(str(v) for v in history.values()), size=20)),
                ft.DataCell(ft.IconButton(icon="DELETE")),
            ] 
        ) for index, history in enumerate(history_list)
    ]


table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("#4", size=20)),
        ft.DataColumn(ft.Text("Sign", size=20)),
        ft.DataColumn(ft.Text("Value", size=20)),
        ft.DataColumn(ft.IconButton(icon="DELETE")),
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{index+1}.", size=20)),
                ft.DataCell(ft.Text("\n".join(v for v in history), size=20)),
                ft.DataCell(ft.Text("\n".join(str(v) for v in history.values()), size=20)),
                ft.DataCell(ft.IconButton(icon="DELETE")),
            ],
        ) for index, history in enumerate(history_list)
    ],
    data_row_max_height=120,
    # border=ft.border.all(1, "#096c05"),
    horizontal_lines=ft.border.BorderSide(1, "#096c05"),
    # border_radius=20,
    # column_spacing=0,
    bgcolor="#99000000",
)

def page_history(page: ft.Page):
    # def test(e):
    #     history_list =[
    #         {
    #             "V":2,
    #             "A":3,
    #             "W":3,
    #             "Ω":23,
    #         }
    #     ]
    #     table.rows = [
    #          ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text(f"{index+1}.", size=20)),
    #                 ft.DataCell(ft.Text("\n".join(v for v in history), size=20)),
    #                 ft.DataCell(ft.Text("\n".join(str(v) for v in history.values()), size=20)),
    #                 ft.DataCell(ft.IconButton(icon="DELETE", on_click=test)),
    #             ],
    #         ) for index, history in enumerate(history_list)
    #     ]
    #     table.rows.pop()
    #     table.rows.append(
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text(f".")),
    #                 ft.DataCell(ft.Text("\n")),
    #                 ft.DataCell(ft.Text("\n")),
    #                 ft.DataCell(ft.IconButton(icon="DELETE", on_click=test)),
    #             ]
    #         )
    #     )
        # page.update()

    # table = ft.DataTable(
    #     columns=[
    #         ft.DataColumn(ft.Text("#4", size=20)),
    #         ft.DataColumn(ft.Text("Sign", size=20)),
    #         ft.DataColumn(ft.Text("Value", size=20)),
    #         ft.DataColumn(ft.IconButton(icon="DELETE")),
    #     ],
    #     rows=[
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text(f"{index+1}.", size=20)),
    #                 ft.DataCell(ft.Text("\n".join(v for v in history), size=20)),
    #                 ft.DataCell(ft.Text("\n".join(str(v) for v in history.values()), size=20)),
    #                 ft.DataCell(ft.IconButton(icon="DELETE", on_click=test)),
    #             ],
    #         ) for index, history in enumerate(history_list)
    #     ],
    #     data_row_max_height=120,
    #     # border=ft.border.all(1, "#096c05"),
    #     horizontal_lines=ft.border.BorderSide(1, "#096c05"),
    #     # border_radius=20,
    #     # column_spacing=0,
    #     bgcolor="#99000000",
    # )

    
    # page.update()

    return ft.Column(
        [
            ft.Container(
                content=table,
                width=page.width,
            )
        ],
        scroll=True,
    )