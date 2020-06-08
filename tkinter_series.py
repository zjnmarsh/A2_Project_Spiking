# https://www.youtube.com/watch?v=jBUpjijYtCk&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=4

import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):  # inheret from tk.Tk
    """Baseline code, adding new pages should be easy"""

    def __init__(self, *args,
                 **kwargs):  # args - can pass as many variables as you want; kwargs are keyboard arguments - passing through dictionaries
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both",
                       expand=True)  # fill - fills in space you have set, expand - increases if there is white space

        container.grid_rowconfigure(0, weight=1)  # 0 is minimum size, weight is priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo): # allows both pages to show - both pages loaded

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")  # assign some frame to grid; sticky - positino and stretch

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # raises to the front - if not in self.frames won't work;

def qf(string):
    print(string)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent class is seaofbtcapp
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)  # pack when very basic

        # button1 = tk.Button(self, text="Visit Page 1",
        #                     command=lambda: qf("hello"))   # lambda function - creates throwaway function that won't run immediately

        button1 = tk.Button(self, text="Visit Page1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Visit Page2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Go Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Go Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Go to page one",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()




app = SeaofBTCapp()
app.mainloop()
