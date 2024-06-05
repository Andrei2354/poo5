from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer


class FooterApp(App):
    BINDINGS = [
        Binding(key="Q", action="quit", description="Salir"),
        Binding(key="B", action="delete", description="Borrar"),
        Binding(key="E", action="down", description="Editar"),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()


if __name__ == "__main__":
    app = FooterApp()
    app.run()