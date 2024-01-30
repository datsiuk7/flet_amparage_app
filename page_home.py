from settings import *

def page_home(page: ft.Page):

    style = ft.ButtonStyle(
        color={
            ft.MaterialState.DEFAULT: "white",
        },
        bgcolor={
            ft.MaterialState.DEFAULT: colors["primary"],
        },
    )

    def clearInput(nameInput):
        print("clear")
        print(page.window_width)
        print(page.width)
        print(page.window_min_width)
        print(page.window_max_width)
        inputs[nameInput].value = ""
        page.update()

    def clearAllInput(e):
        print("clearAll")
        for i in inputs:
            inputs[i].value = ""
        page.update()
        
    inputs = {
        name : ft.TextField(
            # label=name, 
            label_style=ft.TextStyle(color=ft.colors.WHITE, size=20),
            hint_text=name,
            hint_style=ft.TextStyle(color=ft.colors.WHITE, size=20),
            keyboard_type="NUMBER", 
            color="#FFFFFFFF",
            bgcolor="#55000000",
            suffix_text=name,
            suffix_style=ft.TextStyle(color=ft.colors.WHITE, size=20),
            # text_size=20,
            border=ft.InputBorder.NONE,
            input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$"),
            text_style=ft.TextStyle(size=25),
            width=100+page.width*0.5,
        ) for name in "VAWΩ"
    }

    def inputsAdd(nameInput, top=0):
        return ft.Container(
            ft.Row(
                [
                    ft.Container(
                        expand=1, 
                        content=inputs[nameInput],
                    ),
                    ft.Container(
                        width=50,
                        content=ft.IconButton(icon="close", style=style, on_click=lambda _: clearInput(nameInput))
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=top),
        )
    def close_dlg(e):
        dlg_modal.open = False
        page.update()
    
    def open_dlg():
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Увага"),
        content=ft.Text("Введіть лише 2 поля!!!"),
        actions=[
            ft.TextButton("Ок", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


    def count(e):
        onlyTwoInputSet = [x.value for x in inputs.values()]
        A = inputs["A"].value
        V = inputs["V"].value
        W = inputs["W"].value
        O = inputs["Ω"].value

        if onlyTwoInputSet.count("") == 2:
            print(onlyTwoInputSet)
            if V and A:
                inputs["W"].value = float(V) * float(A)
                inputs["Ω"].value = float(V) / float(A)
            elif V and W:
                inputs["A"].value = float(W) / float(V)
                inputs["Ω"].value = float(V) / inputs["A"].value
            elif V and O:
                inputs["A"].value = float(V) / float(O)
                inputs["W"].value = inputs["A"].value * float(V) 
            elif A and W:
                inputs["V"].value = float(W) / float(A)
                inputs["Ω"].value = float(W) / (float(A)*float(A))
            elif A and O:
                inputs["V"].value = float(A) * float(O)
                inputs["W"].value = (float(A)*float(A)) * float(O)
            elif W and O:
                inputs["V"].value = math.sqrt(float(W) * float(O))
                inputs["A"].value = math.sqrt(float(W) / float(O))
            history_list.append(
                {
                    "A" : inputs["A"].value,
                    "V" : inputs["V"].value,
                    "W" : inputs["W"].value,
                    "O" : inputs["Ω"].value
                }
            )
            page.update()
        else:
            # print("має бути лише 2 поля")
            open_dlg()

    return ft.Container(
        
        content=ft.Column(
            [
                inputsAdd("V", top=20),
                inputsAdd("A"),
                inputsAdd("W"),
                inputsAdd("Ω"),
                ft.Container(
                    
                    ft.Row(
                        [
                            ft.Container(
                                expand=1, 
                                content=ft.IconButton(
                                    icon="close",
                                    width=page.width/2.2, 
                                    style=style,
                                    on_click=clearAllInput,
                                )
                            ),
                            ft.Container(
                                expand=1, 
                                content=ft.IconButton(
                                    icon="NAVIGATE_NEXT_ROUNDED",
                                    style=style,
                                    # width=150, 
                                    on_click=count,
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    
                ),
            ],
        ),
        margin=10,
    )