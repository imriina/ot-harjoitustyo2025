from tkinter import ttk, constants
from service.diary_service import diary_service

class RegisterView:
    def __init__(self, root, handle_back, handle_register):
        self._root = root
        self._handle_back = handle_back
        self._handle_register = handle_register
        self._frame = None
        self._username_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_to_db(self):
        username = self._username_entry.get()

        if username.strip():
            diary_service.create_new_user(username)
            self._handle_register()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Register Page")

        self._username_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._create_user_to_db
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        label.grid(row=0, column=0)
        ttk.Label(master=self._frame, text="Käyttis:").grid(row=2, column=0)
        self._username_entry.grid(row=3, column=0)
        back_button.grid(row=6, column=0)
        register_button.grid(row=4, column=0)