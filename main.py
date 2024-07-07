from flet import *


def main(page: Page):
    background_color = "#1bf5af"
    username_field = TextField(width=300, height=35, text_size=12, text_align=TextAlign.CENTER,
                               text_style=TextStyle(font_family="arial"), bgcolor="white",
                               border_radius=25, label="username", label_style=TextStyle(font_family="arial"),
                               border_color=background_color)
    password_field = TextField(width=300, height=35, text_size=12, text_align=TextAlign.CENTER,
                               text_style=TextStyle(font_family="arial"), bgcolor="white",
                               border_radius=25, label="password", password=True,
                               label_style=TextStyle(font_family="arial"), border_color=background_color)
    username_field_signup = TextField(width=300, height=35, text_size=12, text_align=TextAlign.CENTER,
                                      text_style=TextStyle(font_family="arial"), bgcolor="white",
                                      border_radius=25, label="username", label_style=TextStyle(font_family="arial"),
                                      border_color=background_color)
    password_field_signup = TextField(width=300, height=35, text_size=12, text_align=TextAlign.CENTER,
                                      text_style=TextStyle(font_family="arial"), bgcolor="white",
                                      border_radius=25, label="password", password=True,
                                      label_style=TextStyle(font_family="arial"), border_color=background_color)
    repeat_password_field_signup = TextField(width=300, height=35, text_size=12, text_align=TextAlign.CENTER,
                                             text_style=TextStyle(font_family="arial"), bgcolor="white",
                                             border_radius=25, label="repeat password", password=True,
                                             label_style=TextStyle(font_family="arial"), border_color=background_color)
    usernames = []
    overview_text_label = Text(value="")

    # creer la page d'identification
    identification_page = Container(
        border_radius=10,
        bgcolor=background_color,
        expand=True,
        content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(value="Hello, welcome to our Application", size=25, font_family="arial",
                     weight=FontWeight.BOLD),
                Container(height=20),
                Text(value="Login", size=25, font_family="arial", weight=FontWeight.BOLD),
                Container(height=20),
                username_field,
                Container(height=10),
                password_field,
                Container(height=10),
                FloatingActionButton(text="Login", width=150, height=35, on_click=lambda _: iden_verify()),
                Container(height=10),
                Text(value="You don't have any account?", size=12),
                TextButton(text="Sign up", on_click=lambda _: page.go("/account_creation"))

            ]
        )
    )

    # creer l'overview page

    overview_page = Container(
        bgcolor="white",
        content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    bgcolor=background_color,
                    content=Row(
                        controls=[
                            Container(
                                expand=True,
                                content=Row(
                                    controls=[
                                        Container(
                                            expand=True,
                                            content=Row(
                                                alignment=MainAxisAlignment.END,
                                                controls=[
                                                    IconButton(icon=icons.ACCOUNT_CIRCLE, icon_color="white"),
                                                    IconButton(icon=icons.LOGOUT, icon_color="white",
                                                               on_click=lambda _: page.go("/")),
                                                ]
                                            )
                                        )

                                    ]
                                )
                            )
                        ]
                    )
                ),
                overview_text_label,

            ]
        )
    )

    account_creation_page = Container(
        bgcolor=background_color,
        expand=True,
        content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    content=Row(
                        controls=[
                            IconButton(icon=icons.ARROW_BACK, on_click=lambda _: page.go('/'))
                        ]
                    )
                ),
                Container(height=20),
                Text(value="Sign Up", size=25, font_family="arial", weight=FontWeight.BOLD),
                Container(height=20),
                username_field_signup,
                Container(height=10),
                password_field_signup,
                Container(height=10),
                repeat_password_field_signup,
                Container(height=10),
                FloatingActionButton(text="Sign up", width=150, height=35),

            ]
        )
    )

    # creer les routes
    pages = {
        '/': View(
            controls=[
                identification_page,
            ]
        ),
        '/overview': View(
            controls=[
                overview_page
            ]
        ),
        '/account_creation': View(
            controls=[
                account_creation_page
            ]
        )
    }

    # creer un fonction pour verifier les information d'identification

    def iden_verify():
        user = username_field.value
        password = password_field.value
        if user == "admin" and password == "admin":
            usernames.append(user)
            page.go("/overview")
            update_overview_page()

    # creer une fontion pour modifier l'overveiw page en fonction de user
    def update_overview_page():
        overview_text_label.value = "Logged in user : " + "" + usernames[-1]
        page.update()

    # creer une fonction pour le changement des routes

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
        page.update()

    page.on_route_change = route_change
    page.go("/account_creation")


app(target=main)
