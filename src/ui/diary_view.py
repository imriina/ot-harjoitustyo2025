from tkinter import ttk, constants
from service.diary_service import diary_service

class DiaryView:
    """Näkymä jossa voit luoda ja katsoa päiväkirja postauksia
    """
    def __init__(self, root, handle_logout):
        self._root = root
        self._root.geometry("860x560")
        self._root.minsize(700, 400)
        self._root.configure(bg='PaleVioletRed1')
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)

        self._handle_logout = handle_logout
        self._frame = None
        self._username = None

        self._style = ttk.Style()
        self._style.configure("Custom.TFrame", background="PaleVioletRed1", font=('Fixedsys'))
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

    def _send_post(self):
        message = self._entry_message.get()
        if message.strip():
            diary_service.create_post(message)
            self._entry_message.delete(0, constants.END)
            self._update_post()

    def delete_post(self, post_id):
        diary_service.delete_post(post_id)
        self._update_post()

    def _update_post(self):
        for widget in self._posts_frame.winfo_children():
            widget.destroy()

        posts = diary_service.get_posts() or []

        for post in posts:
            post_text = f"{post.created_at} - {post.message}"

            post_frame = ttk.Frame(master=self._posts_frame, style="Custom.TFrame")
            post_frame.pack(anchor="w", pady=2, fill="x")

            post_label = ttk.Label(
                master=post_frame,
                text=post_text,
                wraplength=400,
                justify="left",
                background="PaleVioletRed1",
                font=('Fixedsys', 10))
            post_label.pack(side="left", padx=5)

            delete_button = ttk.Button(
                master=post_frame,
                text="Poista",
                command=lambda post_id=post.post_id: self.delete_post(post_id),
                style="Custom.TButton")
            delete_button.pack(side="right", padx=5)

    def logout(self):
        diary_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="Custom.TFrame")
        self._frame.grid(row=0, column=0, sticky="NSEW")

        for i in range(6):
            self._frame.grid_rowconfigure(i, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        self._username = diary_service.get_logged_in_username()

        label = ttk.Label(
            master=self._frame,
            text="Päiväkirja",
            font=('Fixedsys', 18, 'bold'),
            background="PaleVioletRed1")

        sublabel = ttk.Label(
            master=self._frame,
            text=f"Hei {self._username}",
            background="PaleVioletRed1",
            font=('Fixedsys', 12))

        self._entry_message = ttk.Entry(master=self._frame, width=50)

        send_button = ttk.Button(
            master=self._frame,
            text="Lähetä kirjaus",
            command=self._send_post,
            style="Custom.TButton"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self.logout,
            style="Custom.TButton"
        )

        self._posts_frame = ttk.Frame(master=self._frame, style="Custom.TFrame")

        label.grid(row=0, column=0, pady=(20, 5), sticky="n")
        sublabel.grid(row=1, column=0, pady=(0, 10), sticky="n")
        self._entry_message.grid(row=2, column=0, pady=5, ipadx=50, ipady=5)
        send_button.grid(row=3, column=0, pady=5, ipadx=20, ipady=5)
        self._posts_frame.grid(row=4, column=0, pady=10, sticky="n")
        logout_button.grid(row=5, column=0, pady=10, ipadx=20, ipady=5)

        self._update_post()