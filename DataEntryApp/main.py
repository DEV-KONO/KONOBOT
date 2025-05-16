import flet as ft
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

    def reload_table():
        msg_table.rows = []

        for i in requests.get("http://127.0.0.1:8000/all_msg").json():
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
                    ft.DataCell(ft.Text(requests.get("http://127.0.0.1:8000/all_msg").json()[-1]["id"] +1)),
                    ft.DataCell(ft.Text("test")),
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