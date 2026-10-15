from ttkbootstrap import App


class Window(App):
    def __init__(self, title_value):
        super().__init__(theme="minty-light", title=title_value)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def resize(self, width, height):
        self.geometry(f"{width}x{height}")

    def show(self):
        self.mainloop()