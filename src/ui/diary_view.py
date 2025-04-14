from tkinter import ttk, constants, END, Text
from service.diary_service import diary_service

class DiaryView:
    """Näkymä jossa voit luoda ja katsoa päiväkirja postauksia
    """
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._username = None
        self._post_display = None

        self._initialize()

    def pack(self):
        """Näyttää ikkunan
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _send_post(self):
        message = self._entry_message.get()
        if message.strip():
            diary_service.create_post(message)
            self._entry_message.delete(0, constants.END)
            self._update_post()

    def _update_post(self):
        posts = diary_service.get_posts() or []
        self._post_display.config(state="normal")
        self._post_display.delete("1.0", END)

        for post in posts:
            self._post_display.insert(END, f"{post.created_at} - {post.message}\n\n")

        self._post_display.config(state="disabled")

    def logout(self):
        diary_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._username = diary_service.get_logged_in_username()
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Päiväkirjassa")
        sublabel = ttk.Label(master=self._frame, text=f"Hei {self._username}")

        self._entry_message = ttk.Entry(master=self._frame)
        send_button = ttk.Button(
            master=self._frame,
            text="Lähetä kirjaus",
            command=self._send_post
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self.logout
        )

        self._post_display = Text(master=self._frame, height=15, width=50)
        self._post_display.config(state="disabled")

        label.grid(row=0, column=0, pady=5)
        sublabel.grid(row=1, column=0, pady=5)
        self._entry_message.grid(row=2, column=0, pady=5)
        send_button.grid(row=3, column=0, pady=5)
        self._post_display.grid(row=4, column=0, pady=10)
        logout_button.grid(row=5, column=0, pady=10)

        self._update_post()