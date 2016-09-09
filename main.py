from Tkinter import *
from ttk import Frame, Button, Style
from tkintertable import TableCanvas, TableModel

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        dirLabel = Label(self, text="Directory Path of all files",)
        dirLabel.pack(side=TOP)
        fileText = Entry(self, text="test", width=90)
        fileText.pack(side=TOP)
        outputLabel = Listbox(self, yscrollcommand=scrollbar.set, width=90)
        outputLabel.pack(side=TOP)
        var = StringVar(self)
        var.set("format type") # initial value
        menu = OptionMenu(self, var, "png", "jpg")
        menu.pack(side=TOP)
        self.parent.title("Bulk Image Converter")
        self.style = Style()
        #self.style.theme_use("clam")
        frame = Frame(self, relief=RAISED)
        frame.pack(fill=NONE, expand=True)
        self.pack(fill=BOTH, expand=True)

        def image (text, var) :
            from PIL import Image
            import glob, os
            import sys
            #/Users/augustus/Pictures/iep/
            filepath = text

            print('working....\n')
            if not os.path.exists(filepath):
                print('not a file path\n' + filepath)
            
            for file in glob.glob(filepath + "/*.*"):
                im = Image.open(file)
                file = file.strip("../")
                file = file.strip(".jpg")
                file = file.strip(".jpeg")
                file = file.strip(".png")
                file = file.strip(".tiff")
                file = file.strip(filepath)
                if not os.path.exists(filepath + "output"):
                    os.makedirs(filepath + "output")
                print(file)
                outputLabel.insert(END, file)
                if var == "jpg" :
                    im.save(filepath + "output/" + file + ".jpg", "JPEG")
                elif var == "png" :
                    im.save(filepath + "output/" + file + ".png", "PNG")
                else :
                    im.save(filepath + "output/" + file + ".jpg", "JPEG")
        def fileTextDef () :
            image(fileText.get(), var.get())

        okButton = Button(self, text="OK", command=fileTextDef )
        okButton.pack(side=RIGHT)
        #closeButton = Button(self, text="cancel")
        #closeButton.pack(side=RIGHT, padx=5, pady=5)


def main():
  
    root = Tk()
    def white(*args,**kwargs):
        root.configure(background="white")

    root.configure(background="white")

    root.configure(bg='white')
    root.geometry("350x350+300+300")
    app = App(root)
    #app.bind("okButton", image('/Users/Augsutus/Pictures/iep'))
    root.mainloop()  


if __name__ == '__main__':
    main()
