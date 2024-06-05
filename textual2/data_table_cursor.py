from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("ID", "Nombre" ),
    (1, "Yoel" ),
    (4, "Samuel" ),
    (7, "Amaro" ),

]

# cursors = cycle(["column", "row", "cell"])


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    # def key_c(self):
    #    table = self.query_one(DataTable)
    #    table.cursor_type = next(cursors)


app = TableApp()
if __name__ == "__main__":
    app.run()