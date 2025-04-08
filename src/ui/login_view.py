from tkinter import ttk, constants
from service.diary_service import diary_service, InvalidCredentialsError

class LoginView:
    """Näkymä, joka hoitaa sisäänkirjautumisen
    """
    def __init__(self, root, handle_back, handle_login):
        self._root = root
        self._handle_back = handle_back
        self._handle_login = handle_login
        self._username_login = None
        self._frame = None

        self._root.configure(bg='lightblue')
        self._style = ttk.Style()
        self._style.configure("Custom.TFrame", background="lightblue")
        self._style.configure("Custom.TButton", background="#ECB993", padding=10)
        self._style.map("Custom.TButton", background=[('active', '#E6A370')])

        self._initialize()

    def pack(self):
        """Näyttää ikkunan
        """
        self._frame.pack(fill=constants.BOTH, expand=True)

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
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        label = ttk.Label(
            master=self._frame,
            text="Login Page",
            font=("Helvetica",18, "bold"),
            background="lightblue")

        self._username_login = ttk.Entry(master=self._frame)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back,
            style="Custom.TButton"
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login_user,
            style="Custom.TButton"
        )

        label.grid(row=0, column=0, pady=20, padx=10, sticky="n")
        ttk.Label(
            master=self._frame,
            text="Käyttis:",
            background="lightblue").grid(row=1, column=0, pady=10, sticky="w", padx=10)
        self._username_login.grid(row=1, column=0, pady=10, padx=10)
        back_button.grid(row=4, column=0, pady=20, padx=10, ipady=10, sticky="ew")
        login_button.grid(row=3, column=0, pady=10, padx=10, ipady=10, sticky="ew")

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_rowconfigure(3, weight=1)
        self._frame.grid_rowconfigure(4, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
