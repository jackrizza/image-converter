from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style
from tkintertable import TableCanvas, TableModel
import glob, os
import sys

class App(Frame):

      def __init__(self, parent):
            Frame.__init__(self, parent)   
            self.parent = parent
            self.initUI()
        
    
      def initUI(self):
      
            self.parent.title("Buttons")
            self.style = Style()
            self.style.theme_use("clam")
        
            frame = Frame(self, relief=RAISED, borderwidth=1)
            frame.pack(fill=BOTH, expand=True)
            self.pack(fill=BOTH, expand=True)
            okButton = Button(self, text="OK")
            okButton.pack(side=RIGHT)
            closeButton = Button(self, text="cancel")
            closeButton.pack(side=RIGHT, padx=5, pady=5)

def main():
  
    root = Tk()
    root.configure(background='black')
    root.geometry("750x550+300+300")
    app = App(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
