from tkinter import ttk, constants
from service.diary_service import diary_service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_back, handle_login):
        self._root = root
        self._handle_back = handle_back
        self._handle_login = handle_login
        self._username_login = None
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_user(self):
        username = self._username_login.get()

        try: 
            diary_service.login(username)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Login Page")

        self._username_login = ttk.Entry(master=self._frame)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        
        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login_user
        )

        label.grid(row=0, column=0)
        ttk.Label(master=self._frame, text="Käyttis:").grid(row=2, column=0)
        self._username_login.grid(row=3, column=0)
        back_button.grid(row=6, column=0)
        login_button.grid(row=4, column=0)

