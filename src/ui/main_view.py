from tkinter import ttk, constants

class MainView:
    """Alkunäkymä, josta pääsee kirjautumaan ja rekisteröitymään
    """
    def __init__(self, root, handle_log_in, handle_register):
        self._root = root
        self._root.geometry("860x560")
        self._root.minsize(700, 400)
        self._root.configure(bg='PaleVioletRed1')
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)

        self._handle_log_in = handle_log_in
        self._handle_register = handle_register
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        self._frame.grid(row=0, column=0, sticky="NSEW")

        for i in range(5):
            self._frame.grid_rowconfigure(i, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(
            master=self._frame,
            text="Virtuaalipäiväkirja",
            font=('Fixedsys', 18, 'bold'),
            background="PaleVioletRed1")

        sub_label1 = ttk.Label(
            master=self._frame,
            text="Tervetuloa sovellukseen!",
            font=('Fixedsys', 11),
            background="PaleVioletRed1",
            justify="center")

        sub_label2 = ttk.Label(
            master=self._frame,
            text="Käytä painikkeita kirjautuaksesi tai rekisteröityäksesi, " \
            "jotta pääset käsiksi päiväkirjaan",
            font=('Fixedsys', 11),
            background="PaleVioletRed1",
            justify="center")


        log_in_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_log_in,
            style="Custom.TButton"
        )

        register_button = ttk.Button(
            master=self._frame,
            text="  Rekisteröidy  ",
            command=self._handle_register,
            style="Custom.TButton"
        )

        label.grid(row=0, column=0, pady=20, sticky="N")
        sub_label1.grid(row=1, column=0, pady=5, sticky="N")
        sub_label2.grid(row=2, column=0, pady=5, padx=20, sticky="N")
        log_in_button.grid(row=3, column=0, pady=10, padx=10, ipady=10, ipadx=100, sticky="N")
        register_button.grid(row=4, column=0, pady=10, padx=10, ipady=10, ipadx=100, sticky="N")