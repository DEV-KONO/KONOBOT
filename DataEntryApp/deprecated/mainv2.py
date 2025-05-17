import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Gestor de Mensajes"
    page.window_maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT

    msg_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Usuario")),
            ft.DataColumn(ft.Text("Agente / Responder"))
        ],
        rows=[]
    )

    def update_row(row_index, response_text):
        # Actualiza la fila específica con la respuesta
        msg_table.rows[row_index] = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(msg_table.rows[row_index].cells[0].content.value))),
                ft.DataCell(ft.Text(msg_table.rows[row_index].cells[1].content.value)),
                ft.DataCell(ft.Text(response_text))
            ]
        )
        page.update()

    def add_row(item):
        if item["agent"] is None:
            agent_input = ft.TextField(hint_text="Responder...", width=200)
            row_index = len(msg_table.rows)  # Guardamos el índice de esta fila

            def send_response(e):
                response_text = agent_input.value.strip()
                if not response_text:
                    page.dialog = ft.AlertDialog(title=ft.Text("La respuesta no puede estar vacía."))
                    page.dialog.open = True
                    page.update()
                    return

                try:
                    res = requests.patch(
                        "http://127.0.0.1:8000/answer_msg",
                        json={"id": item["id"], "agent": response_text}
                    )
                    if res.status_code == 200:
                        update_row(row_index, response_text)
                    else:
                        page.dialog = ft.AlertDialog(title=ft.Text(f"Error al enviar respuesta: {res.text}"))
                        page.dialog.open = True
                        page.update()
                except Exception as err:
                    page.dialog = ft.AlertDialog(title=ft.Text(f"Error al conectar con backend: {err}"))
                    page.dialog.open = True
                    page.update()

            send_btn = ft.ElevatedButton(text="Enviar", on_click=send_response)

            msg_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(item["id"]))),
                        ft.DataCell(ft.Text(item["user"])),
                        ft.DataCell(ft.Row([agent_input, send_btn]))
                    ]
                )
            )
        else:
            msg_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(item["id"]))),
                        ft.DataCell(ft.Text(item["user"])),
                        ft.DataCell(ft.Text(item["agent"]))
                    ]
                )
            )

    def load_data():
        try:
            data = requests.get("http://127.0.0.1:8000/all_msg").json()
            msg_table.rows.clear()
            for item in data:
                add_row(item)
            page.update()
        except Exception as err:
            page.dialog = ft.AlertDialog(title=ft.Text(f"Error al conectar con backend: {err}"))
            page.dialog.open = True
            page.update()

    def submit_new_user_msg(e):
        user_msg = user_input.value.strip()
        if not user_msg:
            page.dialog = ft.AlertDialog(title=ft.Text("El mensaje no puede estar vacío."))
            page.dialog.open = True
            page.update()
            return

        try:
            res = requests.post("http://127.0.0.1:8000/new_msg", json={"user": user_msg})
            if res.status_code == 200:
                user_input.value = ""
                load_data()
            else:
                page.dialog = ft.AlertDialog(title=ft.Text(f"Error al agregar mensaje: {res.text}"))
                page.dialog.open = True
                page.update()
        except Exception as err:
            page.dialog = ft.AlertDialog(title=ft.Text(f"Error al conectar con backend: {err}"))
            page.dialog.open = True
            page.update()
    
    #def ChangeAgent(i):
        #user_msg = user_input.value.strip()

    # UI Components
    user_input = ft.TextField(label="Nuevo mensaje de usuario", expand=True)
    add_btn = ft.ElevatedButton(text="Agregar mensaje", on_click=submit_new_user_msg)
    refresh_btn = ft.IconButton(ft.Icons.REFRESH, on_click=lambda e: load_data())

    page.add(
        ft.Column([
            ft.Row([
                ft.Text("Gestor de Mensajes", size=20, weight=ft.FontWeight.BOLD),
                refresh_btn
            ]),
            ft.Text("Enviar nuevo mensaje", size=16),
            ft.Row([user_input, add_btn]),
            ft.Divider(),
            msg_table
        ], scroll=ft.ScrollMode.AUTO)
    )

    load_data()

ft.app(target=main)