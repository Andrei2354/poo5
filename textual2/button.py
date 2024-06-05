from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button


class ButtonsApp(App[str]):


    def compose(self) -> ComposeResult:
        yield Horizontal(
                Button("Saludar", id="Saludar"),
                Button("Salir"),
        )


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "Saludar":
            self.notify("Saludando a la nada")
        else:
            self.exit(str(event.button))


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())