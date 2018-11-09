from tkinter import *
from tkinter import filedialog
import instagram

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.folder_path = StringVar()

    def init_window(self):
        self.master.title("Shanon")
        self.pack(fill=BOTH, expand=1)

        self.y_loc = [[0, 20]]
        y_loc = self.y_loc
        for x in range(6):
            y_loc.append([int(y_loc[x][0]) + 50, int(y_loc[x][1]) + 50])

        print(y_loc)

        Label(self, text="Username:").place(x=10, y=y_loc[0][0])
        self.username_input = Entry(self, width=40)
        self.username_input.place(x=10, y=y_loc[0][1])

        Label(self, text="Password:").place(x=10, y=y_loc[1][0])
        self.password_input = Entry(self, show='*', width=40)
        self.password_input.place(x=10, y=y_loc[1][1])

        login_button = Button(self, text="Login", width=10, command=self.login)
        login_button.place(x=10, y=y_loc[2][0]+10)


        Label(self, text="Instagram image URL:").place(x=10, y=y_loc[3][0])
        self.url_input = Entry(self, width=40)
        self.url_input.place(x=10, y=y_loc[3][1])

        Label(self, text="Download location:").place(x=10, y=y_loc[4][0])
        self.download_location = Button(self, text="Browse", width=40, command=self.browse)
        self.download_location.place(x=10, y=y_loc[4][1])

        download_button = Button(self, text="Download", width=10, command=self.download)
        download_button.place(x=10, y=y_loc[6][0]+10)

        quit_button = Button(self, text="Quit", width=10, command=self.client_exit)
        quit_button.place(x=280, y=y_loc[6][0]+10)

    def browse(self):
        folder = filedialog.askdirectory()
        self.folder_path.set(folder)

        Label(self, text=self.folder_path.get() + '/').place(x=10, y=self.y_loc[5][0])

        print(self.folder_path.get())

    def login(self):
        instagram.login(self.username_input.get(), self.password_input.get())

    def download(self):
        instagram.get_image(self.url_input.get(), self.folder_path.get() + '/')

    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x400")

app = Window(root)
root.mainloop()