import tkinter
import tkinter.ttk

class Example(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background="#333")
        self.parent = parent
        self.centerWindow()
        self.initUI()


    def initUI(self):
        self.parent.title("Окно по центру экрана")
        self.style = tkinter.ttk.Style()
        self.style.theme_use("default")
        self.pack(fill=tkinter.BOTH, expand=1)
        quitButton = tkinter.ttk.Button(self, text="Закрыть окно", command=self.quit)
        quitButton.place(x=0, y=0)

    def centerWindow(self):
        w = 1200
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = tkinter.Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()