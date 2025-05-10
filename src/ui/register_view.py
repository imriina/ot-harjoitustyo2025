from tkinter import ttk, constants
from service.diary_service import diary_service

class RegisterView:
    """Näkymä jossa voit rekisteröityä
    """
    def __init__(self, root, handle_back, handle_register):
        self._root = root
        self._root.geometry("860x560")
        self._root.minsize(700, 400)
        self._root.configure(bg='PaleVioletRed1')
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)

        self._handle_back = handle_back
        self._handle_register = handle_register
        self._frame = None
        self._username_entry = None

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

    def _create_user_to_db(self):
        username = self._username_entry.get()

        if username.strip():
            diary_service.create_new_user(username)
            self._handle_register()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        self._frame.grid(row=0, column=0, sticky="NSEW")

        for i in range(6):
            self._frame.grid_rowconfigure(i, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(
            master=self._frame,
            text="Rekisteröinti",
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

        self._username_entry = ttk.Entry(master=entry_frame, width=30)

        register_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._create_user_to_db,
            style="Custom.TButton"
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back,
            style="Custom.TButton"
        )

        label.grid(row=0, column=0, pady=20, sticky="n")
        self._username_entry.grid(row=0, column=1, padx=(5, 10), sticky="w")
        back_button.grid(row=4, column=0, pady=10, ipadx=104, ipady=10, sticky="n")
        register_button.grid(row=3, column=0, pady=10, ipadx=100, ipady=10, sticky="n")
