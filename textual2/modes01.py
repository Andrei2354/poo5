from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widgets import Footer, Placeholder, Button
from textual.containers import Horizontal, Grid


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Main Screen")
        yield Footer()
        yield Grid(
                Button("Saludar", id="Saludar"),
                Button("Salir"),
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "Saludar":
            self.notify("Saludando a la nada")
        else:
            self.exit(str(event.button)) 
        


class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Settings Screen")
        yield Footer()

class ModalApp(App):
    """An app with a modal dialog."""

    CSS_PATH = "modal01.tcss"
    BINDINGS = [("q", "request_quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Footer()

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.push_screen(MainScreen())

class ModesApp(App):
    BINDINGS = [
        ("M", "switch_mode('Main')", "Main"),  
        ("e", "switch_mode('settings')", "Edición"),
    ]
    MODES = {
        "Main": MainScreen,  
        "settings": SettingsScreen,
    }

    def on_mount(self) -> None:
        self.switch_mode("Main")  


if __name__ == "__main__":
    app = ModesApp()
    app.run()