import secrets

from captcha.image import ImageCaptcha
from PIL import Image, ImageTk
from ttkbootstrap import Frame, Label, Entry, Button

# No 0/O/1/I/L so users don't confuse similar characters.
ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"
LENGTH = 5


class CaptchaWidget(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self._generator = ImageCaptcha(width=160, height=60)
        self._code = ""
        self._photo = None  # keep a reference, otherwise Tk garbage-collects the image

        self.image_label = Label(self)
        self.image_label.grid(row=0, column=0, sticky="w")

        self.refresh_button = Button(self, text="↻", width=3, bootstyle="secondary", command=self.refresh)
        self.refresh_button.grid(row=0, column=1, padx=(10, 0))

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0, columnspan=2, pady=(8, 0), sticky="ew")

        self.refresh()

    def refresh(self):
        self._code = "".join(secrets.choice(ALPHABET) for _ in range(LENGTH))
        image = Image.open(self._generator.generate(self._code))
        self._photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self._photo)
        self.entry.delete(0, "end")

    def is_valid(self) -> bool:
        return self.entry.get().strip().upper() == self._code