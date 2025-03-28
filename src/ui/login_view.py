from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_back, handle_login):
        self._root = root
        self._handle_back = handle_back
        self._handle_login = handle_login
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Login Page")

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        
        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login
        )

        label.grid(row=0, column=0)
        back_button.grid(row=1, column=0)
        login_button.grid(row=2, column=0)
        