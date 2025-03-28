from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_log_in, handle_register):
        self._root = root
        self._handle_log_in = handle_log_in
        self._handle_register = handle_register
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Hello!")
        
        log_in_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_log_in
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=self._handle_register
        )

        label.grid(row=0, column=0)
        log_in_button.grid(row=1, column=0)
        register_button.grid(row=2,column=0)