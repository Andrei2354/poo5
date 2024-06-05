from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll, Binding
from textual.widgets import Button, Static, Footer, Header


class ButtonsApp(App[str]):

    CSS_PATH = "button.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Salir de la app"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            VerticalScroll(
                Static("Botones Saludar", classes="header"),
                Button("Saludar", id="Saludar"),
            ),
            VerticalScroll(
                Static("Boton Salir", classes="header"),
                Button("Salir"),
            ),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Header"
        self.sub_title = "Saludar y Salir"


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "Saludar":
            self.notify("Saludando a la nada")
        else:
            self.exit(str(event.button))


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())