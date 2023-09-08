""":file: app.py File contains classes based on tkinter library,
    describing application style, settings if GUI
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

import sys


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title('Powells Method')
        self.geometry("860x520")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.makeStyles()


        container = ttk.Frame(self,style="Timer.TFrame")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        container.grid(column=0, row=0, sticky="NSWE",padx=10, pady=10)

        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        container.columnconfigure(1,weight=10)
    
        sidePanel = ttk.Frame(container,style="Timer2.TFrame")
        sidePanel.rowconfigure(0,weight=10)
        sidePanel.rowconfigure(1,weight=11)
        sidePanel.columnconfigure(0,weight=1)
        sidePanel.grid(column=0,row=0, sticky="NSW",padx=5,pady=5)


        paramsFrame = OptionPanel(container=sidePanel, controller=self)
        paramsFrame.grid(row=0, column=0, sticky='NSW', padx=2,pady=2)
        logFrame = ttk.Frame(sidePanel,style="Timer4.TFrame")
        logFrame.grid(row=1, column=0, sticky='NSW', padx=2,pady=2)


        plotFrame = ttk.Frame(container,style="Timer3.TFrame")
        plotFrame.grid(row=0,column=1, sticky="NSWE",padx=5,pady=5)
    
    def makeStyles(self):
        print(self.style.theme_names())
        self.style.theme_use("classic")
        self.style.configure("Timer.TFrame", background="grey",foreground="magenta", highlightbackground="blue", highlightthickness=10)
        self.style.configure("Timer2.TFrame", background="#999",foreground="#0f0")
        self.style.configure("Timer3.TFrame", background="#050f",foreground="#0f0")
        self.style.configure("Timer4.TFrame", background="#ddd",foreground="#ddd")
        self["background"] = "#aaa"
    def proceedPowellsMethod(self):
        print("POWELL!")
        pass

    def showHelp(self):

        self.help1=HelpWindow()
        # self.help1.protocol('WM_DELETE_WINDOW', self.destroy)
        self.help1.mainloop()
    
    # self.help1.protocol('WM_DELETE_WINDOW', exit)
    # self.help1.closeMe()
def closeMe(self):
    if self.help1!=None:
        self.help1.destroy()  
    print(2)
    self.destroy()
class OptionPanel(ttk.Frame):
    OPTIONS = {}
    def __init__(self, container,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        # self.columnconfigure(2,weight=1)
        # self.columnconfigure(2,weight=1)
        # self.rowconfigure(3,weight=2)
        
        titleLabel = ttk.Label(self, text="Parameters", anchor='center', font=('Courier 16'))
        titleLabel.grid(row=0, column=0, sticky='WN')

        stopCritFrame = ttk.Frame(self, style ="Timer.TFrame",padding=2, border=1, borderwidth=2)
        stopCritFrame.rowconfigure(0,weight=1)
        stopCritFrame.rowconfigure(1,weight=1)
        stopCritFrame.rowconfigure(2,weight=1)
        stopCritFrame.rowconfigure(3,weight=1)
        stopCritFrame.columnconfigure(0,weight=1)
        stopCritFrame.grid(row=1, column=0, sticky='WN')
        # stopCritFrame.columnconfigure(1,weight=1)

        titleLabel = ttk.Label(stopCritFrame, text="Stop params", anchor='w',font=('Courier 12'))
        titleLabel.grid(row=0, column=0, sticky='W')
        
        eps1Label=ttk.Label(stopCritFrame, text='ε_1:')
        eps1Label.grid(row=1, column=0, sticky='W')
        eps1Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'))
        eps1Entry.grid(row=1, column=0, sticky='E')


        eps2Label=ttk.Label(stopCritFrame, text='ε_1:')
        eps2Label.grid(row=2, column=0, sticky='W')
        eps2Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'))
        eps2Entry.grid(row=2, column=0, sticky='E')

        eps2Label=ttk.Label(stopCritFrame, text=' L :')
        eps2Label.grid(row=3, column=0, sticky='W')
        eps2Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'))
        eps2Entry.grid(row=3, column=0, sticky='E')


        searchDirectFrame = ttk.Frame(self, style ="Timer.TFrame",padding=2, border=1, borderwidth=2)
        searchDirectFrame.rowconfigure(0,weight=1)
        searchDirectFrame.rowconfigure(1,weight=1)
        searchDirectFrame.rowconfigure(2,weight=1)
        searchDirectFrame.rowconfigure(3,weight=1)
        searchDirectFrame.columnconfigure(0,weight=1)
        searchDirectFrame.grid(row=1, column=1, sticky='WN')

        titleLabel2 = ttk.Label(searchDirectFrame, text="Dir. search\nparams", anchor='w',font=('Courier 12'))
        titleLabel2.grid(row=0, column=0, sticky='W')
        
        sep1 = ttk.Separator(searchDirectFrame, orient='horizontal')
        sep1.grid(row=1, column=0, sticky='WE')
        sectionLabel=ttk.Label(searchDirectFrame, text='[a,b]:')
        sectionLabel.grid(row=2, column=0, sticky='W')
        sectionEntry = ttk.Entry(searchDirectFrame, width=6,font=('Courier 10'))
        sectionEntry.grid(row=2, column=0, sticky='E')


        epsLabel=ttk.Label(searchDirectFrame, text=' ε: ')
        epsLabel.grid(row=3, column=0, sticky='W')
        epsEntry = ttk.Entry(searchDirectFrame, width=6,font=('Courier 10'))
        epsEntry.grid(row=3, column=0, sticky='E')

        # eps2Label=ttk.Label(searchDirectFrame, text=' L :')
        # eps2Label.grid(row=3, column=0, sticky='W')
        # eps2Entry = ttk.Entry(searchDirectFrame, width=6,font=('Courier 10'))
        # eps2Entry.grid(row=3, column=0, sticky='E')





        
        generalButtonsFrame = ttk.Frame(self, style ="Timer.TFrame",padding=2, border=1, borderwidth=2)
        generalButtonsFrame.columnconfigure(0, weight=1)
        generalButtonsFrame.rowconfigure(0,weight=1)
        generalButtonsFrame.rowconfigure(1,weight=1)
        generalButtonsFrame.grid(row=1, column=2,sticky='NW')

        runButton = ttk.Button(generalButtonsFrame, text='run', width=10, command=controller.proceedPowellsMethod)
        runButton.grid(row=0, column=0, sticky='W')
        helpButton = ttk.Button(generalButtonsFrame, text='help', width=10, command=controller.showHelp)
        helpButton.grid(row=1, column=0, sticky='W')


        functionFrame = ttk.Frame(self, style ="Timer2.TFrame",padding=5)
        functionFrame.grid(row=2, column=0, sticky='WN',columnspan=2)

        functionFrame.columnconfigure(0,weight=1)
        functionFrame.columnconfigure(1,weight=2)
        functionFrame.rowconfigure(0,weight=1)

        funcLabel = ttk.Label(functionFrame, text='function:')
        funcLabel.grid(row=0, column=0,sticky='E')
        funcEntry = ttk.Entry(functionFrame, width=25)
        funcEntry.grid(row=0, column=1,sticky='W',padx=5)

        x0Frame = ttk.Frame(self, style ="Timer2.TFrame",padding=6)
        x0Frame.grid(row=2, column=2, sticky='WN')
        x0Frame.columnconfigure(0,weight=1)
        x0Frame.columnconfigure(1,weight=1)
        x0Frame.rowconfigure(0,weight=1)
        
        x0Label=ttk.Label(x0Frame, text='X_0:')
        x0Label.grid(row=0, column=0, sticky='E')
        x0Entry = ttk.Entry(x0Frame, width=6,font=('Courier 10'))
        x0Entry.grid(row=0, column=1, sticky='W',padx=5)
        
        



class LogFrame(ttk.Frame):
    pass

class SolutionFrame(ttk.Frame):
    pass

class PlotWindow(tk.Canvas):
    pass

class HelpWindow(tk.Tk):
    counter = 0
    HELP_STRING = """
---------------------------------------
---------------------------------------
---------------------------------------
---------------------------------------
"""
    def __init__(self):
        super().__init__()
        self.counter+=1
        self.title('Powells Method - HELP')
        self.geometry('500x300')
        self.resizable(False,False)
        self['background'] = '#444'
        text = tk.Text(self, background="#555", foreground="white", height=20)
        text.insert("1.0", self.HELP_STRING)
        text["state"] = "normal"
        text.grid()
        self.protocol("WM_DELETE_WINDOW", self.closeMe)
        self.counterUp()
    @classmethod
    def counterUp(cls):
        cls.counter+=1
        print(cls.counter)
    @classmethod
    def counterDown(cls):
        cls.counter-=1
        print(cls.counter)

    def closeMe(self):
        self.counterDown()
        # print(self.counter)
        self.destroy()

        



def test():
    root = MainWindow()
    root.mainloop()



if __name__=='__main__':
    test()