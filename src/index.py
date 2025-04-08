from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()

    window.title("Päiväkirja")

    ui_screen = UI(window)
    ui_screen.start()
    window.configure(cursor="heart")
    window.mainloop()

if __name__ == "__main__":
    main()
