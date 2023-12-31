from powell import powellsMethod
import tkinter as tk
from tkinter import ttk, END, DISABLED
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import messagebox
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import sys
from function_parser import parseFunction
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

"""FILE: app.py File contains classes based on tkinter library,
    describing application style and settings of GUI. 
"""

class MainWindow(tk.Tk):
    """Superior class of whole application. Contains instance of LogFram,
    OptionalPanel, PlotWindow, HelpWindow. Allows to input function of 2-5 variables
    and search minimum with Powells Method.

    Args:
        tk (tk.Tk): Parent class Tkinter.
    
     Static Public Attributes:
        DIRECT_METHODS: tuple of available mathematical methods for searching minimum in direction.
        LABELS_FONT: macro of font for labels, ready to use.
        ENTRY_FONT: macro of font for entries, ready to use.
        TITLE_FONT: macro of font for title, ready to use.
    Public Atributes:
        style (ttk.Style): visual settings for app
    """

    ###################################
    #### tuple('str'): Tuple of implementend method for searching minimum in direction.
    ###################################
    DIRECT_METHODS = ("Golden Search", 'To be Added',  'To be Added')
    
    ###################################
    #### Font type for tk.Label
    ###################################
    LABELS_FONT = ('Courier 13')

    ###################################
    #### Font type for tk.Entry
    ###################################
    ENTRY_FONT = ('Courier 12')
    ###################################
    #### Font type for tk.Label - title
    ###################################
    TITLE_FONT = ('Times 24')

    def __init__(self, *args, **kwargs)->None:
        """ Inits main window. Takes arguments same as tk.Tk.

        """
        super().__init__()
        self.title('Powells Method')
        self.geometry("1070x530")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        ################
        ### tk.stringVar value contains selected method in direction. 
        ################
        self.style = ttk.Style(self)
        self.makeStyles()

        


        ################
        ### tk.stringVar value contains selected method in direction. 
        ################
        self.selectedDirectMethod = tk.StringVar() 
        
        ################
        ### tk.stringVar value next message inserted in self.logFram.text: 
        ################
        self.logVariable = tk.StringVar()
        ################
        ### tk.stringVar: value contains information about startpoint 
        ################
        self.startPoint = tk.StringVar()
        self.startPoint.set('-4,4')

        ################
        ### tk.stringVar string with function to parse
        ################
        self.functionString = tk.StringVar()
        self.functionString.set('(x1-2)^2+(x1-x2^2)^2')

        ################
        ### tk.stringVar section for searching minimum in direction
        self.abGSS = tk.StringVar()
        self.abGSS.set('-1,1')
        ################
        ### tk.stringVar minimum length between 2  following points 
        ################
        self.epsilon1 = tk.IntVar(value=0.0001)
        ################
        ### tk.stringVar minimum length between 2  following values of fun 
        ################
        self.epsilon2 = tk.IntVar(value=0.0001)
        ################
        ### tk.stringVar minimum length between 2  following values of fun in direction
        ################
        self.epsilon  = tk.IntVar(value=0.001)

        ################
        ### tk.stringVar max number of iteration of algoruithm
        ################
        self.paramL  = tk.IntVar(value=100)

        ################
        ### tk.stringVar [a,b] describes range of plot x axis
        ################
        self.x1Range = tk.StringVar()
        self.x1Range.set('-10,10')
        ################
        ### tk.stringVar [a,b] describes range of plot y axis
        ################
        self.x2Range = tk.StringVar()
        self.x2Range.set('-10,10')



        ################
        ### ttk.Frame: main Frame of application
        ################
        self.container = ttk.Frame(self,style="Timer.TFrame")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.container.grid(column=0, row=0, sticky="NSWE",padx=5, pady=5,rowspan=2, columnspan=2)

        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)
        self.container.columnconfigure(1,weig=3)


        ################
        ### ttk.Frame Frame of side panel contains logs and params menu
        ################
        self.sidePanel = ttk.Frame(self.container,style="Timer2.TFrame")
        self.sidePanel.rowconfigure(0,weight=10)
        self.sidePanel.rowconfigure(1,weight=11)
        self.sidePanel.columnconfigure(0,weight=1)
        self.sidePanel.grid(column=0,row=0, sticky="NSW",padx=5,pady=5)


        ################
        ### ttk.Frame params menu.
        ################
        self.paramsFrame = OptionPanel(container=self.sidePanel, controller=self)
        self.paramsFrame.grid(row=0, column=0, sticky='NSWE', padx=1)


        ################
        ### ttk.Frame for logs with ttk.Text
        ################
        self.logFrame = LogFrame(self.sidePanel)
        self.logFrame.grid(row=1, column=0, sticky='NSWE', padx=2,pady=2)



        ################
        ### ttk.Frame Frame contains canvas with plot
        ################
        self.plotFrame = ttk.Frame(self.container,style="Timer3.TFrame")
        self.plotFrame.grid(row=0,column=1, sticky="NSWE",rowspan=2)
        self.plotCanvas = PlotWindow(self.plotFrame, self)
        self.plotCanvas.grid(sticky='WN')
        

    def on_closing(self)->None:
        """Handler for colisng main window using messagebox.
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quit()
            self.destroy()
            # sys.exit(0)

    def makeStyles(self):
        """Function makes few new styles for app.
        """

        self.style.theme_use("clam")
        self.style.configure("Timer.TFrame", background="grey",foreground="magenta", highlightbackground="grey", highlightthickness=10,padding=2, border=3, borderwidth=3)
        self.style.configure("Timer3.TFrame", background="#050f",foreground="#0f0",padding=2,)
        self.style.configure("Timer4.TFrame", background="#ddd",foreground="#ddd", highlightthickness=10,padding=2, border=3, borderwidth=3)
        self.style.configure("Title.TLabel", background="#ccc",foreground="#333", relief = 'ridge', highlightthickness=10,border=2, borderwidth = 3, font=self.TITLE_FONT)
        self.style.configure("Label1.TLabel", background="#ccc",foreground="#000",relief = 'groove', borderwidth = 2, font=self.LABELS_FONT, anchor = 'center')
        self["background"] = "#bbb"


    def proceedPowellsMethod(self):
        """Poweells Method Handler.
        """
        self.plotCanvas.plotHandler()
        # print("POWELL!")
        

    def showHelp(self):
        """Handler for open help window.
        """


        ################
        ### (HelpWindow): instance of independence window with help
        ################
        self.help1=HelpWindow()
        self.help1.mainloop()



class OptionPanel(ttk.Frame):
    """_summary_

    Args:
        ttk (Frame): Frame describing options with widgets for inputs.
    """
    OPTIONS = {}
    def __init__(self, container,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        # self.grid_columnconfigure(2,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(1,weight=3)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)


        titleLabel = ttk.Label(self, text="Parameters", anchor='center',style="Title.TLabel")
        titleLabel.grid(row=0, column=0, sticky='WN')

        stopCritFrame = ttk.Frame(self, style ="Timer.TFrame")
        stopCritFrame.rowconfigure(0,weight=1)
        stopCritFrame.rowconfigure(1,weight=1)
        stopCritFrame.rowconfigure(2,weight=1)
        stopCritFrame.rowconfigure(3,weight=1)
        stopCritFrame.columnconfigure(0,weight=1)
        stopCritFrame.columnconfigure(1,weight=1)
        stopCritFrame.grid(row=2, column=0, sticky='WN')
        # stopCritFrame.columnconfigure(1,weight=1)

        titleLabel = ttk.Label(stopCritFrame, text=" Stop conditions ", style='Label1.TLabel')
        titleLabel.grid(row=0, columnspan=2, sticky='WNE')

        eps1Label=ttk.Label(stopCritFrame, text='ε_1:', style='Label1.TLabel')
        eps1Label.grid(row=1, column=0, sticky='ENWS')
        eps1Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'), textvariable=controller.epsilon1)
        eps1Entry.grid(row=1, column=1, sticky='WENS')


        eps2Label=ttk.Label(stopCritFrame, text='ε_2:', style='Label1.TLabel')
        eps2Label.grid(row=2, column=0, sticky='EWNS')
        eps2Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'), textvariable=controller.epsilon2)
        eps2Entry.grid(row=2, column=1, sticky='WENS')

        eps2Label=ttk.Label(stopCritFrame, text=' L : ', style='Label1.TLabel')
        eps2Label.grid(row=3, column=0, sticky='EWN')
        eps2Entry = ttk.Entry(stopCritFrame, width=6,font=('Courier 10'), textvariable=controller.paramL)
        eps2Entry.grid(row=3, column=1, sticky='WENS')


        searchDirectFrame = ttk.Frame(self, style ="Timer.TFrame")
        searchDirectFrame.rowconfigure(0,weight=1)
        searchDirectFrame.rowconfigure(1,weight=1)
        searchDirectFrame.rowconfigure(2,weight=1)
        searchDirectFrame.rowconfigure(3,weight=1)
        searchDirectFrame.columnconfigure(0,weight=1)
        searchDirectFrame.columnconfigure(1,weight=1)
        searchDirectFrame.grid(row=2, column=1, sticky='WN')



        methodList = ttk.Combobox(searchDirectFrame, state='readonly')
        methodList['values'] = controller.DIRECT_METHODS
        methodList.current(0)
        methodList.grid(row=0, columnspan=2, sticky='WEN')

        # sep1 = ttk.Separator(searchDirectFrame, orient='horizontal')
        # sep1.grid(row=1, column=0, sticky='WEN')
        sectionLabel=ttk.Label(searchDirectFrame, text=' [a,b]: ', style='Label1.TLabel')
        sectionLabel.grid(row=2, column=0, sticky='WSEN')
        sectionEntry = ttk.Entry(searchDirectFrame, width=3,font=('Courier 10'),textvariable= controller.abGSS)
        sectionEntry.grid(row=2, column=1, sticky='EWSN')


        epsLabel=ttk.Label(searchDirectFrame, text=' ε: ', style='Label1.TLabel')
        epsLabel.grid(row=3, column=0, sticky='EWNS')
        epsEntry = ttk.Entry(searchDirectFrame, width=3,font=('Courier 10'), textvariable=controller.epsilon)
        epsEntry.grid(row=3, column=1, sticky='WENS')


        generalButtonsFrame = ttk.Frame(self, style ="Timer.TFrame")
        generalButtonsFrame.columnconfigure(0, weight=1)
        generalButtonsFrame.columnconfigure(1,weight=1)
        generalButtonsFrame.rowconfigure(0,weight=1)
        generalButtonsFrame.grid(row=0, column=1,sticky='N',columnspan=2)

        runButton = ttk.Button(generalButtonsFrame, text='RUN', width=10, command=controller.proceedPowellsMethod)
        runButton.grid(row=0, column=0, sticky='W')
        helpButton = ttk.Button(generalButtonsFrame, text='HELP', width=10, command=controller.showHelp)
        helpButton.grid(row=0, column=1, sticky='W')


        functionFrame = ttk.Frame(self, style ="Timer2.TFrame",padding=5,height=15)
        functionFrame.grid_columnconfigure(0,weight=1)
        functionFrame.grid_columnconfigure(1,weight=1)
        functionFrame.columnconfigure(0,weight=1)
        functionFrame.columnconfigure(1,weight=1)
        functionFrame.rowconfigure(0,weight=1)
        functionFrame.grid(row=1, column=0, sticky='WN',columnspan=2)

        funcLabel = ttk.Label(functionFrame, text=' function: ', style='Label1.TLabel')
        funcLabel.grid(row=0, column=0,sticky='EW')
        funcEntry = ttk.Entry(functionFrame, width=25,textvariable=controller.functionString)
        funcEntry.grid(row=0, column=1,sticky='WE',padx=2)

        x0Frame = ttk.Frame(functionFrame, style ="Timer2.TFrame",padding=6)
        x0Frame.columnconfigure(0,weight=1)
        x0Frame.columnconfigure(1,weight=1)
        x0Frame.rowconfigure(0,weight=1)
        x0Frame.grid(row=1, column=0, sticky='WN',columnspan=2)


        x0Label=ttk.Label(x0Frame, text=' X_0:  ',style='Label1.TLabel',width=5,anchor='center')
        x0Label.grid(row=0, column=0, sticky='E')
        x0Entry = ttk.Entry(x0Frame, width=6,font=('Courier 12'), textvariable=controller.startPoint)
        x0Entry.grid(row=0, column=2, sticky='E',padx=5)


        xAmountFrame = ttk.Frame(functionFrame, style ="Timer2.TFrame",padding=6)
        xAmountFrame.columnconfigure(0,weight=1)
        xAmountFrame.columnconfigure(1,weight=1)
        xAmountFrame.rowconfigure(0,weight=1)
        xAmountFrame.rowconfigure(1,weight=1)
        xAmountFrame.grid(row=1, column=1, sticky='SE',columnspan=1)


        x1AmountLabel=ttk.Label(xAmountFrame, text=' X1 range:',style='Label1.TLabel')
        x1AmountLabel.grid(row=0, column=0, sticky='NE')
        x1RangeEntry = ttk.Entry(xAmountFrame,width=7, textvariable=controller.x1Range)
        x1RangeEntry.grid(row=0, column=1,sticky='NW')
        x2AmountLabel=ttk.Label(xAmountFrame, text=' X2 range:',style='Label1.TLabel')
        x2AmountLabel.grid(row=1, column=0, sticky='SE')
        x2RangeEntry = ttk.Entry(xAmountFrame,width=7,textvariable= controller.x2Range)
        x2RangeEntry.grid(row=1, column=1,sticky='SW')


class LogFrame(ttk.Frame):
    """Simple frame with text field for saving logs.

    Args:
        ttk (Frame): parent class.
    """

    def __init__(self, container)->None:
        """ Creates new instance of LogFrame based on ttk.Frame.
        Args:
            container (tk.Tk): ref to main window

        """
        super().__init__(container)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)
        self.text = tk.Text(self, height=self.winfo_height()-5, width=50)
        self.text.grid(row=0, column=0,sticky="NSW")
        self.text_scroll = ttk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text_scroll.grid(row=0, column=0, sticky="nse")
        self.text["yscrollcommand"] = self.text_scroll.set

    def addLog(self,controller):
        self.text.insert("1.0", 'test text!\n')
    pass


class PlotWindow(tk.Frame):
    """ PlotWindow plot function and plot it with contourf

    Args:
        tk (Frame): Frame with canvas and figure from matplotlib.
    
    Public Attributes:
        container (tk.Tk): ref to main window
        fig (matplotlib.pyplot): figure for visualization of function and PM.
        canvas (FigureCanvasTkAgg): canvas for visalization
        ax (Axes): axes of Plot
        fig (plot.Figure()) figure to plot
        contourf (Axes.contourf): Plot filled contours for func of 2 variables.
        cb (colorbar): colourbar for Plot filled contours.

    """


    def __init__(self, container, controller):
        """Inits object and creates all public attributes.

        Args:
            container (ttk.Frame: Superior caontainer
            controller (tk.Tk)): MainWindow witth global variables
        """
        super().__init__(container)
        ##########################
        #########  (tk.Tk): ref to main window
        #########################
        self.controller = controller
        
        ##########################
        #########  (matplotlib.pyplot): figure for visualization of function and PM.
        #########################
        self.fig = plt.Figure()

        ##########################
        #########  (FigureCanvasTkAgg): canvas for visalization
        #########################
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        NavigationToolbar2Tk(self.canvas, self)

        ##########################
        ######### (Axes): axes of Plot
        #########################
        self.ax = self.fig.add_subplot(111)
        # print(type(self.ax))
        # input()
        self.ax.set_title(str(self.controller.functionString.get()))
        self.ax.set_xlabel('X_1')
        self.ax.set_ylabel('X_2')

        ##########################
        #########(Axes.contourf): Plot filled contours for func of 2 variables.
        #########################
        self.contourf=self.ax.contourf([0,0], [0,0], [(0,0),(0,0)], extend='both', levels=1)
        self.ax.plot()

        ##########################
        ######### cb (colorbar): colorbar for Plot filled contours.
        #########################
        self.cb=plt.colorbar(self.contourf)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()



    def plotHandler(self)->None:
        """Realization of visualisation of Powell Method.
            Update plot with following points from PM.
        """
        self.ax.cla()
        self.cb.remove()


        func = parseFunction(self.controller.functionString.get())
        
        ab = self.controller.abGSS.get().split(',')
        x10, x20 = self.controller.startPoint.get().split(',')
        x10 =float(x10)
        x20=float(x20)
        x1lim = tuple([float(xo) for xo in self.controller.x1Range.get().split(',')])
        x2lim = tuple([float(xo) for xo in self.controller.x2Range.get().split(',')])

        # run Powell
        powellResult = powellsMethod(func,[x10,x20],int(self.controller.epsilon1.get()),int(self.controller.epsilon2.get()), [ float(x) for x in ab],
                                     self.controller.paramL.get(),ax=self.ax,gssEps=self.controller.epsilon.get(),
                                     logVar=self.controller.logFrame.text)

        
        self.ax.set_xlim(*x1lim)
        self.ax.set_ylim(*x2lim)
        # print(self.controller.functionString.get())
        self.ax.set_title(str(self.controller.functionString.get()))
        self.ax.set_xlabel('X_1')
        self.ax.set_ylabel('X_2')
        x1=np.linspace(x1lim[0], x1lim[1],1000)
        x2=np.linspace(x2lim[0], x2lim[1],1000)

        X1, X2 = np.meshgrid(x1, x2)
        Z = func(X1, X2)
        Z = np.array(Z)
        Z = np.reshape(Z, (len(x1), len(x2)))
        # plt.plot.clear()
        self.contourf=self.ax.contourf(X1, X2, Z, extend='both', levels=20)
        self.cb=plt.colorbar(self.contourf)


        self.canvas.draw()


    def __del__(self):
        """deconstructor
        """
        self.quit()
        # self.destroy()

class HelpWindow(tk.Tk):
    """HelpWindow is simple class based on tk.Tk providing window with
    text field with some information.

    Args:
        tk (tk.Tk): Parent class.
    
     Static Public Attributes:
        HELP_STRING: Help text String.
        counter: Counter of active instances.
    Public Atributes:
        container (ttk.Frame): main Frame contains all widgets.
        text (ttk.Text): Text field.
        text_scroll (ttk.Scrollbar): Scrollbar widget vertical.
        text_scrollHor (ttk.Scrollbar): Scrollbar widget horizontal.    
    """




    ##################################
    ##### Counter of active instances.
    ##################################
    counter = 0

    ##################################
    ##### String with helpful informations.
    ##################################
    HELP_STRING = """|----------------------------------------------------------|
|---------------------------HELP---------------------------|
|App allows to  search local minimum with Powells Method.  |
|This is an alternative for project made for classes of    |
|Theory and methods of optimalization at WUST.             |
|                                                          |
|Available functions contains from 1 to 5 variables in     |
|form from x1 to x5                                        |
|Available input parameters: name: label || example        |
|                                                          |
|function string: function || x1^2+(X2+1)^2+x3^3           |
|start point: X_0 || -4,-4                                 |
|number of variables: X No. || 2                           |
|Stop conditions                                           |
|Min difference between two following pts:  ε_1  ||  0.001 |
|Min difference between two following values: ε_2 || 0.001 |
| Max. number of iteration: L || 1000                      |
|                                                          |
|-------------------------------------------------------   |
|-------------------------------------------------------   |
|Stop critteria for methods searching in direction:        |
|                                                          |
|Range: [a,b] || -2, 1 ; measured from current Powell point|
|Min difference beetween function value: ε || 0.01         |
|            !!!!!+!  ε < ε_1   !+!!!!!                    |
|-------------------------------------------------------   |
|                                                          |
|-------------------------------------------------------   |
"""

    def __init__(self):
        """ Constructor of HelpWindow. 
        """
        super().__init__()
        self.counter+=1
        self.title('Powells Method - HELP')
        self.geometry('500x300')
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self['background'] = '#444'
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        ##################################
        ##### Main container for widgets in this window.
        ##################################
        self.container  = ttk.Frame(self)
        self.container.grid_columnconfigure(0,weight=1)
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid(row=0, column=0,sticky="NSEW")

        ##################################
        ##### Text field for HelpString.
        ##################################
        self.text = tk.Text(self.container, background="#555", foreground="white", height=self.winfo_height()-3, state=DISABLED)
        self.text.insert("1.0", self.HELP_STRING)
        self.text["state"] = "disabled"
        self.text.grid(sticky='NSW')

        ##################################
        ##### Scrollbar widget connected with text field. Y-axis.
        ##################################
        self.text_scroll = ttk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text["yscrollcommand"] = self.text_scroll.set
        self.text_scroll.grid(row=0, column=0, sticky="NSE")


        ##################################
        ##### Scrollbar widget connected with text field. X-axis.
        ##################################
        self.text_scrollHor = ttk.Scrollbar(self, orient="horizontal", command=self.text.xview)
        self.text["xscrollcommand"] = self.text_scrollHor.set
        self.text_scrollHor.grid(row=0, column=0, sticky="WE")
        self.counterUp()


    @classmethod
    def counterUp(cls):
        """Classmethod for debugging destructor with counting new intances.
        """
        cls.counter+=1
        # print(cls.counter)
    @classmethod
    def counterDown(cls):
        """Classmethod for debugging destructor.
        """
        cls.counter-=1
        # print(cls.counter)

    def on_closing(self):
        """Closuring of HelpWindow and destroying instance if HelpWindow()
        """
        self.counterDown()
        self.quit()
        self.destroy()



def main():
    root = MainWindow()
    root.mainloop()

if __name__=='__main__':
    main()