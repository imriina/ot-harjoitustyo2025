from tkinter import ttk, constants
from service.diary_service import diary_service

class DiaryView:
    """Näkymä jossa voit luoda ja katsoa päiväkirja postauksia
    """
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._username = None

        self._initialize()

    def pack(self):
        """Näyttää ikkunan
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _send_post(self):
        message = self._entry_message.get()  # Hakee tekstikentän sisällön
        if message.strip():  # Estetään tyhjät viestit
            diary_service.create_post(message)  # Tallennetaan kirjautuneen käyttäjän nimellä
            self._entry_message.delete(0, constants.END)

    def logout(self):
        diary_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._username = diary_service.get_logged_in_username()
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Päiväkirjassa")
        sublabel = ttk.Label(master=self._frame, text=f"Hei {self._username}")

        self._entry_message = ttk.Entry(master=self._frame)
        send_button = ttk.Button(
            master=self._frame,
            text="Lähetä kirjaus",
            command=self._send_post
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self.logout
        )

        label.grid(row=0, column=0, pady=10)
        sublabel.grid(row=1, column=0, pady=10)
        self._entry_message.grid(row=2, column=0, pady=10)  # Tekstikenttä viestille
        send_button.grid(row=3, column=0, pady=10)  # Lähetä-nappi
        logout_button.grid(row=4, column=0, pady=20)