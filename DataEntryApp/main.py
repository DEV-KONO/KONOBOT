from importlib import reload
import flet as ft
from httpx import request
import requests

def main(page: ft.Page):
    page.window.maximized = True

    msg_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("User")),
            ft.DataColumn(ft.Text("Agent"))
        ]
    )

    def send_new_msg(e):
        print(e.control.parent.controls[0].value)
        try:
            response = requests.post("https://4tlbbn0c-8000.usw3.devtunnels.ms/new_msg", json={"user" : e.control.parent.controls[0].value})
            response.raise_for_status()

            data = response.json()
            print("all good:", data)
            reload_table()
        except requests.exceptions.HTTPError as error:
            print("Hubo un error HTTP:", error)
        except requests.exceptions.RequestException as error:
            print("Hubo un problema al llamar la API:", error)

    def respond_msg(e):
        print(e.control.parent.controls[0].value)
        print(e.control.parent.parent.parent.cells[0].content.value)
        try:
            response = requests.patch("https://4tlbbn0c-8000.usw3.devtunnels.ms/answer_msg", json={"agent" : e.control.parent.controls[0].value, "id" : int(e.control.parent.parent.parent.cells[0].content.value)})
            response.raise_for_status()

            data = response.json()
            print("all good:", data)
            reload_table()
        except requests.exceptions.HTTPError as error:
            print("Hubo un error HTTP:", error)
        except requests.exceptions.RequestException as error:
            print("Hubo un problema al llamar la API:", error)

    def reload_table():
        msg_table.rows = []

        for i in requests.get("https://4tlbbn0c-8000.usw3.devtunnels.ms/all_msg").json():
            if i["agent"] == None:
                msg_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(i["id"])),
                            ft.DataCell(ft.Text(i["user"])),
                            ft.DataCell(
                                ft.Row(
                                    controls=[
                                        ft.TextField(hint_text="Ingrese una respuesta.",expand=True),
                                        ft.IconButton(ft.Icons.SEND, on_click=respond_msg)
                                    ],
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.END
                                )
                            )
                        ]
                    )
                )
            else:
                msg_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(i["id"])),
                            ft.DataCell(ft.Text(i["user"])),
                            ft.DataCell(ft.Text(i["agent"])),
                        ]
                    )
                )
        msg_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(requests.get("https://4tlbbn0c-8000.usw3.devtunnels.ms/all_msg").json()[-1]["id"] +1)),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                ft.TextField(hint_text="Ingrese un mensaje.",expand=True),
                                ft.IconButton(ft.Icons.SEND, on_click=send_new_msg)
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.END
                        )
                    ),
                    ft.DataCell(ft.Text("NULL"))
                ]
            )
        )
        page.update()

    reload_btn = ft.IconButton(ft.Icons.REFRESH,on_click=lambda _:reload_table())

    reload_table()

    page.add(
        msg_table,
        reload_btn
    )

ft.app(main)