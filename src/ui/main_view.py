from tkinter import ttk, constants

class MainView:
    """Alkunäkymä, josta pääsee kirjautumaan ja rekisteröitymään
    """
    def __init__(self, root, handle_log_in, handle_register):
        self._root = root
        self._handle_log_in = handle_log_in
        self._handle_register = handle_register
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        self._frame.grid(row=0, column=0, sticky="NSEW")

        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(
            master=self._frame,
            text="Virtuaalipäiväkirja",
            font=('Helvetica', 18, 'bold'),
            background="lightblue")
        sub_label = ttk.Label(
            master=self._frame,
            text="Tervetuloa sovellukseen! Käytä painikkeita kirjautuaksesi tai " \
            "rekisteröityäksesi, jotta pääset käsiksi päiväkirjaan",
            font=('Helvetica', 13),background="lightblue")


        log_in_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_log_in,
            style="Custom.TButton"
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=self._handle_register,
            style="Custom.TButton"
        )
        label.grid(row=0, column=0, pady=20, sticky="N")
        sub_label.grid(row=1, column=0, pady=10, sticky="N")
        log_in_button.grid(row=2, column=0, pady=10, padx=40, ipady=10, sticky="EW")
        register_button.grid(row=3, column=0, pady=10, padx=40, ipady=10, sticky="EW")
