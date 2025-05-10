from tkinter import ttk, constants
from service.diary_service import diary_service, InvalidCredentialsError

class LoginView:
    """Näkymä, joka hoitaa sisäänkirjautumisen
    """
    def __init__(self, root, handle_back, handle_login):
        self._root = root
        self._root.geometry("860x560")
        self._root.minsize(700, 400)
        self._root.configure(bg='PaleVioletRed1')
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)

        self._handle_back = handle_back
        self._handle_login = handle_login
        self._username_login = None
        self._frame = None

        self._style = ttk.Style()
        self._style.configure("Custom.TFrame", background="PaleVioletRed1")
        self._style.configure("Custom.TButton", background="LightPink1", padding=10, font=('Fixedsys'))
        self._style.map("Custom.TButton", background=[('active', 'LightPink2')])

        self._initialize()

    def pack(self):
        """Näyttää ikkunan
        """
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        """Tuhoaa ikkunan
        """
        self._frame.destroy()

    def _login_user(self):
        username = self._username_login.get()

        try:
            diary_service.login(username)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Virheellinen käyttäjänimi")

    def _show_error(self, message):
        self._error_label.config(text=message)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        self._frame.grid(row=0, column=0, sticky="NSEW")

        for i in range(6):
            self._frame.grid_rowconfigure(i, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)


        label = ttk.Label(
            master=self._frame,
            text="Kirjautuminen",
            font=("Fixedsys",18, "bold"),
            background="PaleVioletRed1")

        entry_frame = ttk.Frame(master=self._frame, style="Custom.TFrame")
        entry_frame.grid(row=1, column=0, pady=10)


        ttk.Label(
            master=entry_frame,
            text="Käyttäjätunnus:",
            background="PaleVioletRed1",
            font=("Fixedsys", 12)
        ).grid(row=0, column=0, padx=(10, 5), sticky="e")

        self._username_login = ttk.Entry(master=entry_frame, width=30)

        back_button = ttk.Button(
            master=self._frame,
            text="  Back  ",
            command=self._handle_back,
            style="Custom.TButton"
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login_user,
            style="Custom.TButton"
        )

        self._error_label = ttk.Label(
            master=self._frame,
            text="",
            foreground="red",
            background="PaleVioletRed1",
            font=("Fixedsys", 11)
        )

        self._username_login.grid(row=0, column=1, padx=(5, 10), sticky="w")
        label.grid(row=0, column=0, pady=20, sticky="n")
        login_button.grid(row=3, column=0, pady=10, ipadx=100, ipady=10, sticky="n")
        back_button.grid(row=4, column=0, pady=10, ipadx=114, ipady=10, sticky="n")
        self._error_label.grid(row=2, column=0)