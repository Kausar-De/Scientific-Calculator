import tkinter as tk #For GUI
import tkinter.ttk as ttk #For styling
from PIL import ImageTk, Image #For image processing
import numpy as np #For matrix operations
import math #For math expressions

LargeFont = ('Verdana', 12) #Standard large font to be used throughout
TitleFont = ('Times New Roman', 20, 'bold') #Standard font to be used for headline text
LabelFont = ('Arial', 13, 'bold') #Standard font to be used for labels

uHist = [] #Usage History array

expression = '' #Global variable declarations
uStatement = ''
prec = 2
evar = math.e
pivar = math.pi
phivar = 1.618033988749894

class Calculator(tk.Tk): #Main program class w/ container

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'Scientific Calculator') #Program title
        
        container = tk.Frame(self) #Code for main container
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} #Code for accomodating different frames in which code will run

        for F in (StartPage, ChoicePage, ArithPage, NumpyPage, HistPage): #Iterates through the different pages. Different page names will be added here as they are created
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(StartPage) #Shows the starting page

    def show_frame(self, cont): #This function is used to display the different frames

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame): #This class is for the starting page, which will be displayed first

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = '#222831') #Defines the frame, as well as inherits from container class

        def setPreci(): #This function sets global precision
            try:
                global prec
                
                val = int(precifield.get())

                prec = val
                precvar.set('Precision is now ' + str(prec))
            except:
                precvar.set('ERROR')

        def msclick(event): #This function is to empty precifield upon mouse click
            precifield.delete(0, 'end')
            return None

        precvar = tk.StringVar()
        precvar.set('Enter Precision')

        label1 = tk.Label(self, text = 'Welcome to the Calculator!', font = TitleFont, fg = '#00adb5', bg = '#222831') #These labels are for displaying the title text
        label1.grid(row = 0, column = 1, padx = 250, pady = 10) #To position label
        label2 = tk.Label(self, text = 'Please press START to continue or QUIT to exit!', font = TitleFont, fg = '#00adb5', bg = '#222831')
        label2.grid(row = 1, column = 1, padx = 150, pady = 10)

        startlf = tk.LabelFrame(self, bg = '#222831', borderwidth = 0, highlightthickness = 0) #This label enables positioning buttons centrally
        startlf.grid(row = 2, column = 1, padx = 420, pady = 10)

        s = ttk.Style() #Button styling
        s.theme_use('alt')
        s.configure('btn.TButton', font = ('Arial', 12), foreground = '#eeeeee', background = '#00adb5')
        s.map('btn.TButton', foreground = [('active', '!disabled', '#00adb5')], background = [('active', '#393e46')])

        startbutton = ttk.Button(startlf, text = 'START', style = 'btn.TButton', command = lambda: controller.show_frame(ChoicePage)) #This button redirects to ChoicePage
        startbutton.grid(row = 0, column = 0, padx = 10, pady = 50, sticky = 'e')

        quitbutton = ttk.Button(startlf, text = 'QUIT', style = 'btn.TButton', command = lambda: quit()) #This button ends the program
        quitbutton.grid(row = 0, column = 1, padx = 10, pady = 50, sticky = 'w')

        precilf = tk.LabelFrame(self, bg = '#393e46', borderwidth = 0, highlightthickness = 0) #This label enables positioning buttons centrally
        precilf.grid(row = 3, column = 1, padx = 420, pady = 10, sticky = 'n')
        
        precilabel = tk.Label(precilf, text = 'Set global precision:', font = LabelFont, fg = '#00adb5', bg = '#222831')
        precilabel.grid(row = 0, column = 0, padx = 10, pady = 10)

        precifield = tk.Entry(precilf, textvariable = precvar, font = LargeFont) #This entry field displays user input and output
        precifield.grid(row = 1, column = 0, ipadx = 0.1, ipady = 3, padx = 10, pady = 10)
        precifield.bind('<Button-1>', msclick)

        precibutton = ttk.Button(precilf, text = 'SET', style = 'btn.TButton', command = lambda: setPreci())
        precibutton.grid(row = 2, column = 0, padx = 10, pady = 10)
                                
class ChoicePage(tk.Frame): #This class is for the second page, where user can choose which part of calculator to use

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = '#222831')

        choiceslf = tk.LabelFrame(self, bg = '#222831', borderwidth = 0, highlightthickness = 0) #This label enables positioning buttons centrally
        choiceslf.grid(row = 1, column = 0, padx = 360, pady = 100)

        label = tk.Label(self, text = 'So, what are we doing?', font = TitleFont, fg = '#00adb5', bg = '#222831') #Title label
        label.grid(row = 0, column = 0, padx = 150, pady = 10, sticky = 'nsew') 

        arithbutton = ttk.Button(choiceslf, text = 'Arithmetic', style = 'btn.TButton', command = lambda: controller.show_frame(ArithPage)) #Button to take us to arithmetic operations (PLANNED)
        arithbutton.grid(row = 0, column = 0, padx = 10, pady = 20)

        numpybutton = ttk.Button(choiceslf, text = 'Matrices & More', style = 'btn.TButton', command = lambda: controller.show_frame(NumpyPage)) #Button to take us to numpy operations
        numpybutton.grid(row = 0, column = 1, padx = 10, pady = 20)

        graphbutton = ttk.Button(choiceslf, text = 'Graphs', style = 'btn.TButton') #Button to take us to matplotlib operations (PLANNED)
        graphbutton.grid(row = 1, column = 0, padx = 10, pady = 20)

        docsbutton = ttk.Button(choiceslf, text = 'Useful Formulae', style = 'btn.TButton') #Button to take us to documentations page (PLANNED)
        docsbutton.grid(row = 1, column = 1, padx = 10, pady = 20)

        backbutton = ttk.Button(choiceslf, text = 'Back', style = 'btn.TButton', command = lambda: controller.show_frame(StartPage)) #This button takes us to the previous page
        backbutton.grid(row = 0, column = 2, padx = 10, pady = 20)

        histbutton = ttk.Button(choiceslf, text = 'History', style = 'btn.TButton', command = lambda: controller.show_frame(HistPage)) #This button takes us to the usage history page (PLANNED)
        histbutton.grid(row = 1, column = 2, padx = 10, pady = 10)

class ArithPage(tk.Frame): #This class is for the Arithmetic operations page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = '#222831')

        def click(num): #This functions enables button inputs
            global prec
            global expression
            
            expression = expression + str(num) #Num argument is substituted by input from calculator buttons
            equation.set(expression)

        def solve(): #This function equates the inputted expression
            try:
                global prec
                global expression
                global uStatement
                global uHist
                
                ans = str(round(eval(expression), prec)) #Using eval to calculate user inputed expression and is then converted to string
                uStatement = str(expression + ' = ' + ans + '\n') #Usage history statement
                uHist.append(uStatement)
                equation.set(ans) #Displays answer in inputfield
                expression = ans
            except:
                equation.set('ERROR')
                expression = ''

        def clr(): #This function is for behaviour of CLEAR button for arithmetic
            global expression
            expression = ''
            equation.set('Enter your Input')

        def clrmod(): #This function is for behaviour of CLEAR button for modulus
            mod1var.set('Enter Dividend')
            mod2var.set('Enter Divisor')
            modansvar.set('Answer shows here')

        def clrabs(): #This function is for behaviour of CLEAR button for absolute value
            absvar.set('Enter your input')
            absansvar.set('Answer shows here')

        def clrperc(): #This function is for behaviour of CLEAR button for percentage
            perc1var.set('Enter Part')
            perc2var.set('Enter Whole')
            percansvar.set('Answer shows here')
            
        def msclick1(event): #This function is to empty modfield1 upon mouse click
            modfield1.delete(0, 'end')
            return None

        def msclick2(event): #Above function for modfield2
            modfield2.delete(0, 'end')
            return None

        def msclick3(event): #Above function for absfield
            absfield.delete(0, 'end')
            return None

        def msclick4(event): #Above function for percfield1
            percfield1.delete(0, 'end')
            return None

        def msclick5(event): #Above function for percfield2
            percfield2.delete(0, 'end')
            return None

        def modsolve(): #This function calculates modulus
            try:
                global uHist
                global uStatement
                
                dividend, divisor = float(modfield1.get()), float(modfield2.get()) #Acquires dividend and divisor
                
                ans = round((dividend % divisor), prec) #Calculates modulus
                uStatement = str('The modulus of ' + str(dividend) + ' and ' + str(divisor) + ' is ' + str(ans) + '\n') #Usage history statement
                uHist.append(uStatement) 
                modansvar.set(ans)
            except:
                mod1var.set('ERROR')
                mod2var.set('ERROR')

        def abssolve(): #This function calculates absolute value
            try:
                global uHist
                global uStatement
                
                abso = float(absfield.get()) #Acquires value for absolute
                
                ans = round((abs(abso)), prec) #Calculates absolute 
                uStatement = str('The absolute value of ' + str(abso) + ' is ' + str(ans) + '\n') #Usage history statement                
                uHist.append(uStatement) 
                absansvar.set(ans)
            except:
                absvar.set('ERROR')

        def percsolve(): #This function calculates percentage
            try:
                global uHist
                global uStatement
                
                part, whole = float(percfield1.get()), float(percfield2.get()) #Acquires numbers for percentage
                
                ans = round(((part / whole)*100), prec) #Calculates percentage
                ans = str(ans) + '%' #Displays answer with % sign at the end
                uStatement = str(str(part) + ' is ' + ans + ' of ' + str(whole) + '\n') #Usage history statement                
                uHist.append(uStatement) 
                percansvar.set(ans)
            except:
                perc1var.set('ERROR')
                perc2var.set('ERROR')

        equation = tk.StringVar() #These variables are the text variables for all the Entry fields
        equation.set('Enter your Input')
        mod1var = tk.StringVar()
        mod1var.set('Enter Dividend')
        mod2var = tk.StringVar()
        mod2var.set('Enter Divisor')
        absvar = tk.StringVar()
        absvar.set('Enter Number')
        modansvar = tk.StringVar()
        modansvar.set('Answer shows here')
        absansvar = tk.StringVar()
        absansvar.set('Answer shows here')
        perc1var = tk.StringVar()
        perc1var.set('Enter Part')
        perc2var = tk.StringVar()
        perc2var.set('Enter Whole')
        percansvar = tk.StringVar()
        percansvar.set('Answer shows here')        

        label = tk.Label(self, text = 'Arithmetic', font = TitleFont, fg = '#00adb5', bg = '#222831') #Title Label
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        arilf = tk.LabelFrame(self, text = 'Arithmetic:', font = LabelFont, fg = '#00adb5', bg = '#393e46') #This label frame contains all the stuff for simple arithmetic
        arilf.grid(row = 1, column = 0, padx = 10, pady = 10)

        inputfield = tk.Entry(arilf, textvariable = equation, font = LargeFont, state = 'disabled') #This entry field displays user input and output
        inputfield.grid(columnspan = 4, ipadx = 20, ipady = 3, pady = 15)

        btn1 = ttk.Button(arilf, text = '1', style = 'btn.TButton', command = lambda: click(1)) #Calculator buttons
        btn1.grid(row = 5, column = 0, padx = 10, pady = 10)

        btn2 = ttk.Button(arilf, text = '2', style = 'btn.TButton', command = lambda: click(2))
        btn2.grid(row = 5, column = 1, padx = 10, pady = 10)

        btn3 = ttk.Button(arilf, text = '3', style = 'btn.TButton', command = lambda: click(3))
        btn3.grid(row = 5, column = 2, padx = 10, pady = 10)

        btn4 = ttk.Button(arilf, text = '4', style = 'btn.TButton', command = lambda: click(4))
        btn4.grid(row = 4, column = 0, padx = 10, pady = 10)

        btn5 = ttk.Button(arilf, text = '5', style = 'btn.TButton', command = lambda: click(5))
        btn5.grid(row = 4, column = 1, padx = 10, pady = 10)

        btn6 = ttk.Button(arilf, text = '6', style = 'btn.TButton', command = lambda: click(6))
        btn6.grid(row = 4, column = 2, padx = 10, pady = 10)

        btn7 = ttk.Button(arilf, text = '7', style = 'btn.TButton', command = lambda: click(7))
        btn7.grid(row = 3, column = 0, padx = 10, pady = 10)

        btn8 = ttk.Button(arilf, text = '8', style = 'btn.TButton', command = lambda: click(8))
        btn8.grid(row = 3, column = 1, padx = 10, pady = 10)

        btn9 = ttk.Button(arilf, text = '9', style = 'btn.TButton', command = lambda: click(9))
        btn9.grid(row = 3, column = 2, padx = 10, pady = 10)

        btn0 = ttk.Button(arilf, text = '0', style = 'btn.TButton', command = lambda: click(0))
        btn0.grid(row = 6, column = 1, padx = 10, pady = 10)

        btndec = ttk.Button(arilf, text = '.', style = 'btn.TButton', command = lambda: click('.'))
        btndec.grid(row = 6, column = 0, padx = 10, pady = 10)

        btneql = ttk.Button(arilf, text = '=', style = 'btn.TButton', command = lambda: solve())
        btneql.grid(row = 6, column = 2, padx = 10, pady = 10)

        btndiv = ttk.Button(arilf, text = '/', style = 'btn.TButton', command = lambda: click('/'))
        btndiv.grid(row = 3, column = 3, padx = 10, pady = 10)

        btnmult = ttk.Button(arilf, text = '*', style = 'btn.TButton', command = lambda: click('*'))
        btnmult.grid(row = 4, column = 3, padx = 10, pady = 10)

        btnmin = ttk.Button(arilf, text = '-', style = 'btn.TButton', command = lambda: click('-'))
        btnmin.grid(row = 5, column = 3, padx = 10, pady = 10)

        btnplus = ttk.Button(arilf, text = '+', style = 'btn.TButton', command = lambda: click('+'))
        btnplus.grid(row = 6, column = 3, padx = 10, pady = 10)

        btnlbr = ttk.Button(arilf, text = '(', style = 'btn.TButton', command = lambda: click('('))
        btnlbr.grid(row = 1, column = 2, padx = 10, pady = 10)

        btnrbr = ttk.Button(arilf, text = ')', style = 'btn.TButton', command = lambda: click(')'))
        btnrbr.grid(row = 1, column = 3, padx = 10, pady = 10)

        btne = ttk.Button(arilf, text = 'e', style = 'btn.TButton', command = lambda: click(round(evar, prec)))
        btne.grid(row = 2, column = 1, padx = 10, pady = 10)

        btnpi = ttk.Button(arilf, text = '\u03C0', style = 'btn.TButton', command = lambda: click(round(pivar, prec)))
        btnpi.grid(row = 1, column = 0, padx = 10, pady = 10)

        btnexp = ttk.Button(arilf, text = '**', style = 'btn.TButton', command = lambda: click('**'))
        btnexp.grid(row = 2, column = 2, padx = 10, pady = 10)

        btnflrdiv = ttk.Button(arilf, text = '//', style = 'btn.TButton', command = lambda: click('//'))
        btnflrdiv.grid(row = 2, column = 3, padx = 10, pady = 10)

        btng = ttk.Button(arilf, text = 'g', style = 'btn.TButton', command = lambda: click(9.8))
        btng.grid(row = 2, column = 0, padx = 10, pady = 10)

        btnphi = ttk.Button(arilf, text = '\u03C6', style = 'btn.TButton', command = lambda: click(round(phivar, prec)))
        btnphi.grid(row = 1, column = 1, padx = 10, pady = 10)

        btnclr = ttk.Button(arilf, text = 'Clear', style = 'btn.TButton', command = lambda: clr()) #Button to clear inputfield
        btnclr.grid(row = 0, column = 3, padx = 10, pady = 10)
        
        modabslf = tk.LabelFrame(self, text = 'Modulus, Absolute and Percentage:', font = LabelFont, fg = '#00adb5', bg = '#393e46') #This label frame contains everything else
        modabslf.grid(row = 1, column = 2, padx = 10, pady = 10)

        modlabel = tk.Label(modabslf, text = 'Modulus:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Modulus Label
        modlabel.grid(row = 0, column = 0, padx = 10, pady = 7.5, sticky = 'w')

        perclabel = tk.Label(modabslf, text = 'Percentage:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Percentage Label
        perclabel.grid(row = 5, column = 0, padx = 10, pady = 7.5, sticky = 'w')

        abslabel = tk.Label(modabslf, text = 'Absolute value:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Absolute Value Label
        abslabel.grid(row = 3, column = 0, padx = 10, pady = 7.5, sticky = 'w')

        modfield1 = tk.Entry(modabslf, textvariable = mod1var) #This entry field is for dividend in modulus
        modfield1.grid(row = 1, column = 0, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)
        modfield1.bind('<Button-1>', msclick1)

        modfield2 = tk.Entry(modabslf, textvariable = mod2var) #This entry field is for divisor in modulus
        modfield2.grid(row = 1, column = 1, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)
        modfield2.bind('<Button-1>', msclick2)

        modansfield = tk.Entry(modabslf, textvariable = modansvar, state = 'disabled') #This entry field is for displaying modulus answer
        modansfield.grid(row = 2, column = 0, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)

        percfield1 = tk.Entry(modabslf, textvariable = perc1var) #This entry field is for part in percentage
        percfield1.grid(row = 6, column = 0, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)
        percfield1.bind('<Button-1>', msclick4)

        percfield2 = tk.Entry(modabslf, textvariable = perc2var) #This entry field is for whole in percentage
        percfield2.grid(row = 6, column = 1, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)
        percfield2.bind('<Button-1>', msclick5)

        percansfield = tk.Entry(modabslf, textvariable = percansvar, state = 'disabled') #This entry field is for displaying percentage answer
        percansfield.grid(row = 7, column = 0, ipadx = 1, ipady = 3, padx = 10, pady = 7.5)

        absfield = tk.Entry(modabslf, textvariable = absvar) #This entry field is for absolute value
        absfield.grid(row = 4, column = 0, ipadx = 1, padx = 10, ipady = 3, pady = 7.5)
        absfield.bind('<Button-1>', msclick3)

        absansfield = tk.Entry(modabslf, textvariable = absansvar, state = 'disabled') #This entry field is for displaying absolute answer
        absansfield.grid(row = 4, column = 1, ipadx = 1, padx = 10, ipady = 3, pady = 7.5)

        btnmod = ttk.Button(modabslf, text = 'Modulus', style = 'btn.TButton', command = lambda: modsolve()) #Button for calculating modulus
        btnmod.grid(row = 1, column = 2, padx = 10, pady = 7.5)

        btnabs = ttk.Button(modabslf, text = 'Absolute', style = 'btn.TButton', command = lambda: abssolve()) #Button for calculating absolute value
        btnabs.grid(row = 4, column = 2, padx = 10, pady = 7.5)

        btnperc = ttk.Button(modabslf, text = 'Percentage', style = 'btn.TButton', command = lambda: percsolve()) #Button for calculating percentage
        btnperc.grid(row = 6, column = 2, padx = 10, pady = 7.5)

        btnclr1 = ttk.Button(modabslf, text = 'Clear', style = 'btn.TButton', command = lambda: clrmod()) #Clear buttons
        btnclr1.grid(row = 0, column = 2, padx = 10, pady = 7.5, sticky = 'e')

        btnclr2 = ttk.Button(modabslf, text = 'Clear', style = 'btn.TButton', command = lambda: clrabs())
        btnclr2.grid(row = 3, column = 2, padx = 10, pady = 7.5, sticky = 'e')

        btnclr3 = ttk.Button(modabslf, text = 'Clear', style = 'btn.TButton', command = lambda: clrperc())
        btnclr3.grid(row = 5, column = 2, padx = 10, pady = 7.5, sticky = 'e')

        backbutton = ttk.Button(self, text = 'Back', style = 'btn.TButton', command = lambda: controller.show_frame(ChoicePage)) #This button takes us to the previous page
        backbutton.grid(row = 0, column = 2, padx = 10, sticky = 'e')

        histbutton = ttk.Button(self, text = 'History', style = 'btn.TButton', command = lambda: controller.show_frame(HistPage)) #This button takes us to the history page
        histbutton.grid(row = 0, column = 0, padx = 10, sticky = 'w')

class NumpyPage(tk.Frame): #This class is for Matrices, Trig and Logs page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = '#222831')

        def matAdd(): #This function is for matrix addition
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext1.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield1.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array

                mat2 = mattext2.get('1.0', 'end-1c') #Same but for mattext2
                list2 = list(map(float, mat2.split()))
                j=0
                col2 = int(matcolfield2.get())
                mat1n2=[]
                while j<len(list2):
                    mat1n2.append(list2[j : j + col2])
                    j += col2
                arr2 = np.array(mat1n2)
            
                ans = np.add(arr1, arr2).round(decimals = prec) #Calculate sum
                anslist = ans.tolist() #Display sum in same format as user input
                for i in anslist:
                    istr = ' '.join([str(elem) for elem in i]) 
                    istr = istr + '\n'
                    anstext.insert(tk.END, istr)

                mat3 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The addition of' + '\n' + mat1 + '\n' + 'and' + '\n' + mat2 + '\n' + 'is' + '\n' + mat3)
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")

        def matSub(): #This function is for matrix subtraction
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext1.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield1.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array

                mat2 = mattext2.get('1.0', 'end-1c') #Same but for mattext2
                list2 = list(map(float, mat2.split()))
                j=0
                col2 = int(matcolfield2.get())
                mat1n2=[]
                while j<len(list2):
                    mat1n2.append(list2[j : j + col2])
                    j += col2
                arr2 = np.array(mat1n2)
            
                ans = np.subtract(arr1, arr2).round(decimals = prec) #Calculate difference
                anslist = ans.tolist() #Display difference in same format as user input
                for i in anslist:
                    istr = ' '.join([str(elem) for elem in i]) 
                    istr = istr + '\n'
                    anstext.insert(tk.END, istr)

                mat3 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The difference between' + '\n' + mat1 + '\n' + 'and' + '\n' + mat2 + '\n' + 'is' + '\n' + mat3)
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")

        def matMul(): #This function is for matrix multiplication
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext1.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield1.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array

                mat2 = mattext2.get('1.0', 'end-1c') #Same but for mattext2
                list2 = list(map(float, mat2.split()))
                j=0
                col2 = int(matcolfield2.get())
                mat1n2=[]
                while j<len(list2):
                    mat1n2.append(list2[j : j + col2])
                    j += col2
                arr2 = np.array(mat1n2)
            
                ans = np.dot(arr1, arr2).round(decimals = prec) #Calculate product
                anslist = ans.tolist() #Display product in same format as user input
                for i in anslist:
                    istr = ' '.join([str(elem) for elem in i]) 
                    istr = istr + '\n'
                    anstext.insert(tk.END, istr)

                mat3 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The product of' + '\n' + mat1 + '\n' + 'and' + '\n' + mat2 + '\n' + 'is' + '\n' + mat3)
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")       

        def matDiv(): #This function is for matrix division
            try:
                global uHist
                global uStatement
                
                if matdivfield.get() != 'Divisor' or '': #This is for dividing matrix by user inputted number
                    anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                    mat1 = mattext3.get('1.0', 'end-1c') #Turn user input into list
                    list1 = list(map(float, mat1.split())) 
                    i=0
                    col1 = int(matcolfield3.get()) #Make nested list divided based on user input of column count
                    mat1nl=[]
                    while i<len(list1):
                        mat1nl.append(list1[i : i + col1])
                        i += col1
                    arr1 = np.array(mat1nl) #Convert nested list into numpy array

                    div = float(matdivfield.get()) #Gets divisor in float form
                
                    ans = np.divide(arr1, div).round(decimals = prec) #Calculate division
                    anslist = ans.tolist() #Display division in same format as user input
                    for i in anslist:
                        istr = ' '.join([str(elem) for elem in i]) 
                        istr = istr + '\n'
                        anstext.insert(tk.END, istr)

                    mat3 = anstext.get('1.0', 'end-1c') #Usage history statement
                    uStatement = str('The division of' + '\n' + mat1 + '\n' + 'and' + '\n' + str(div) + '\n' + 'is' + '\n' + mat3)
                    uHist.append(uStatement)
                
                elif matdivfield.get() == 'Divisor' or '': #This is for dividing matrices by each-other
                    anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                    mat1 = mattext1.get('1.0', 'end-1c') #Turn user input into list
                    list1 = list(map(float, mat1.split())) 
                    i=0
                    col1 = int(matcolfield1.get()) #Make nested list divided based on user input of column count
                    mat1nl=[]
                    while i<len(list1):
                        mat1nl.append(list1[i : i + col1])
                        i += col1
                    arr1 = np.array(mat1nl) #Convert nested list into numpy array

                    mat2 = mattext2.get('1.0', 'end-1c') #Same but for mattext2
                    list2 = list(map(float, mat2.split()))
                    j=0
                    col2 = int(matcolfield2.get())
                    mat1n2=[]
                    while j<len(list2):
                        mat1n2.append(list2[j : j + col2])
                        j += col2
                    arr2 = np.array(mat1n2)
                
                    ans = np.divide(arr1, arr2).round(decimals = prec) #Calculate division
                    anslist = ans.tolist() #Display division in same format as user input
                    for i in anslist:
                        istr = ' '.join([str(elem) for elem in i]) 
                        istr = istr + '\n'
                        anstext.insert(tk.END, istr)

                    mat3 = anstext.get('1.0', 'end-1c') #Usage history statement
                    uStatement = str('The division of' + '\n' + mat1 + '\n' + 'and' + '\n' + mat2 + '\n' + 'is' + '\n' + mat3)
                    uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")

        def matInv(): #This function is for matrix inverse
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext3.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield3.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array

                ans = np.linalg.inv(arr1).round(decimals = prec) #Calculate inverse
                anslist = ans.tolist() #Display inverse in same format as user input
                for i in anslist:
                    istr = ' '.join([str(elem) for elem in i]) 
                    istr = istr + '\n'
                    anstext.insert(tk.END, istr)

                mat2 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The inverse of' + '\n' + mat1 + '\n' + 'is' + '\n' + mat2)
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")      

        def matTrace(): #This function is for matrix trace
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext3.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield3.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array
            
                ans = round(np.trace(arr1), prec) #Calculate trace
                anstext.insert(tk.END, ans)

                mat2 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The trace of' + '\n' + mat1 + '\n' + 'is' + '\n' + mat2 + '\n')
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")       

        def matDet(): #This function is for matrix determinant
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext3.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield3.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array
            
                ans = round(np.linalg.det(arr1), prec) #Calculate determinant
                anstext.insert(tk.END, ans) 

                mat2 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The determinant of' + '\n' + mat1 + '\n' + 'is' + '\n' + mat2 + '\n')
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")       

        def matTrans(): #This function is for matrix transpose
            try:
                global uHist
                global uStatement

                anstext.delete('1.0', 'end') #Remove existing quantity in anstext

                mat1 = mattext3.get('1.0', 'end-1c') #Turn user input into list
                list1 = list(map(float, mat1.split())) 
                i=0
                col1 = int(matcolfield3.get()) #Make nested list divided based on user input of column count
                mat1nl=[]
                while i<len(list1):
                    mat1nl.append(list1[i : i + col1])
                    i += col1
                arr1 = np.array(mat1nl) #Convert nested list into numpy array

                ans = np.transpose(arr1) #Calculate inverse
                anslist = ans.tolist() #Display inverse in same format as user input
                for i in anslist:
                    istr = ' '.join([str(elem) for elem in i]) 
                    istr = istr + '\n'
                    anstext.insert(tk.END, istr)

                mat2 = anstext.get('1.0', 'end-1c') #Usage history statement
                uStatement = str('The transpose of' + '\n' + mat1 + '\n' + 'is' + '\n' + mat2)
                uHist.append(uStatement)
            except:
                anstext.delete('1.0', 'end')
                anstext.insert(tk.END, "ERROR")       

        def reset(): #This is to program reset button
            matcolfield1.delete(0, 'end')
            mat1var.set('Enter columns')
            
            matcolfield2.delete(0, 'end')
            mat2var.set('Enter columns')
            
            matcolfield3.delete(0, 'end')
            mat3var.set('Columns')

            matdivfield.delete(0, 'end')
            matdivvar.set('Divisor')

            mattext1.delete('1.0', 'end')
            mattext2.delete('1.0', 'end')
            mattext3.delete('1.0', 'end')
            anstext.delete('1.0', 'end')

        def trigSin(): #This function is for calculating sin
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigfield input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module
                
                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.sin(trigdeg), prec)) #Calculates sin rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Sin of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.sin(trigfinal), prec)) #Calculates sin rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Sin of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def trigCos(): #This function is for calculating cos
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigfield input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module

                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.cos(trigdeg), prec)) #Calculates cos rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Cos of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.cos(trigfinal), prec)) #Calculates cos rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Cos of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def trigTan(): #This function is for calculating tan
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigfield input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module

                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.tan(trigdeg), prec)) #Calculates tan rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Tan of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.tan(trigfinal), prec)) #Calculates tan rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Tan of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def trigArcsin(): #This function is for calculating arcsin
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigfield input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module
                
                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.asin(trigdeg), prec)) #Calculates arcsin rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arcsin of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.asin(trigfinal), prec)) #Calculates arcsin rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arcsin of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def trigArccos(): #This function is for calculating arccos
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigvar input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module

                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.acos(trigdeg), prec)) #Calculates cos rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arccos of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.acos(trigfinal), prec)) #Calculates cos rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arccos of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def trigArctan(): #This function is for calculating arctan
            try:
                global uHist
                global uStatement

                trigval = str(trigfield.get()) #Acquires trigvar input as string to accomodate fraction inputs
                trigfinal = float(eval(trigval)) #Evaluates fraction input and converts it to float for math module

                choice = radiovar.get()
                if choice == 1:
                    trigdeg = round(math.radians(trigfinal), prec)
                    ans = str(round(math.atan(trigdeg), prec)) #Calculates arctan rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arctan of ' + trigval + ' degrees is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)                
                elif choice == 2:
                    ans = str(round(math.atan(trigfinal), prec)) #Calculates arctan rounded to 2 places, converts it to string for entry widget
                    uStatement = str('Arctan of ' + trigval + ' radians is ' + ans + '\n') #Usage history statement
                    uHist.append(uStatement)

                trigvar.set(ans) #Display answer
            except:
                trigvar.set('ERROR')

        def clrtrig(): #This is to program trig clear button
            trigfield.delete(0, 'end')
            trigvar.set('Enter angle')

        def loge(): #This function is for calculating natural log
            try:
                global uHist
                global uStatement

                logval = str(logfield.get())#Acquires logfield input as string to accomodate fraction inputs
                logfinal = float(eval(logval)) #Evaluates fraction input and converts it to float for math module

                ans = str(round(math.log(logfinal), prec)) #Calculates ln rounded to 2 places, converts it to string for entry widget
                uStatement = str('Natural log of ' + logval + ' is ' + ans + '\n') #Usage history statement
                uHist.append(uStatement)
                logvar.set(ans) #Display answer
            except:
                logvar.set('ERROR')

        def log10(): #This function is for calculating natural log
            try:
                global uHist
                global uStatement

                logval = str(logfield.get())#Acquires logfield input as string to accomodate fraction inputs
                logfinal = float(eval(logval)) #Evaluates fraction input and converts it to float for math module

                ans = str(round(math.log10(logfinal), prec)) #Calculates log base 10 rounded to 2 places, converts it to string for entry widget
                uStatement = str('Log base 10 of ' + logval + ' is ' + ans + '\n') #Usage history statement
                uHist.append(uStatement)
                logvar.set(ans) #Display answer
            except:
                logvar.set('ERROR')

        def antilog(): #This function is for calculating natural log
            try:
                global uHist
                global uStatement

                logval = str(logfield.get())#Acquires logfield input as string to accomodate fraction inputs
                logfinal = float(eval(logval)) #Evaluates fraction input and converts it to float for math module

                ans = str(round(np.exp(logfinal), prec)) #Calculates antilog base e rounded to 2 places, converts it to string for entry widget
                uStatement = str('Antilog of ' + logval + ' is ' + ans + '\n') #Usage history statement
                uHist.append(uStatement)
                logvar.set(ans) #Display answer
            except:
                logvar.set('ERROR')

        def clrlog(): #This is to program log clear button
            logfield.delete(0, 'end')
            logvar.set('Enter value')

        def msclick1(event): #This function is to empty matcolfield1 upon mouse click
            matcolfield1.delete(0, 'end')
            return None

        def msclick2(event): #Above function for matcolfield2
            matcolfield2.delete(0, 'end')
            return None

        def msclick3(event): #Above function for mattext1
            mattext1.delete('1.0', 'end')
            return None

        def msclick4(event): #Above function for mattext2
            mattext2.delete('1.0', 'end')
            return None

        def msclick5(event): #Above function for mattext3
            mattext3.delete('1.0', 'end')
            return None

        def msclick6(event): #Above function for matcolfield3
            matcolfield3.delete(0, 'end')
            return None

        def msclick7(event): #Above function for matdivfield
            matdivfield.delete(0, 'end')
            return None

        def msclick8(event): #Above function for trigfield
            trigfield.delete(0, 'end')
            return None

        def msclick9(event): #Above function for logfield
            logfield.delete(0, 'end')
            return None

        mat1var = tk.StringVar() #These variables are the text variables for all the Entry fields
        mat1var.set('Enter columns')
        mat2var = tk.StringVar()
        mat2var.set('Enter columns')
        mat3var = tk.StringVar()
        mat3var.set('Columns')
        matdivvar = tk.StringVar()
        matdivvar.set('Divisor')
        trigvar = tk.StringVar()
        trigvar.set('Enter angle')
        logvar = tk.StringVar()
        logvar.set('Enter value')
        radiovar = tk.IntVar()
        radiovar.set(1)

        label = tk.Label(self, text = 'Matrices & More', font = TitleFont, fg = '#00adb5', bg = '#222831') #Title label
        label.grid(row = 0, column = 1, padx = 0, pady = 10, sticky = 'nsew')

        backbutton = ttk.Button(self, text = 'Back', style = 'btn.TButton', command = lambda: controller.show_frame(ChoicePage)) #This button takes us to the previous page
        backbutton.grid(row = 0, column = 2, padx = 10, pady = 20, sticky = 'e')

        histbutton = ttk.Button(self, text = 'History', style = 'btn.TButton', command = lambda: controller.show_frame(HistPage)) #This button takes us to the usage history page
        histbutton.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')

        matopslf = tk.LabelFrame(self, text = 'Matrix Operations:', font = LabelFont, fg = '#00adb5', bg = '#393e46') #This label frame contains all the stuff to be used for numpy matrices
        matopslf.grid(row = 1, column = 0, padx = 10, pady = 10)

        mat1label = tk.Label(matopslf, text = 'Matrix 1:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Matrix 1 label
        mat1label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'w')

        mat2label = tk.Label(matopslf, text = 'Matrix 2:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Matrix 2 label
        mat2label.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'w')

        mat3label = tk.Label(matopslf, text = 'Other ops:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Matrix 3 label
        mat3label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = 'w')

        mat4label = tk.Label(matopslf, text = 'Answers:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Answer matrix label
        mat4label.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = 'w')

        matcolfield1 = tk.Entry(matopslf, font = LargeFont, width = 12, textvariable = mat1var) #This field takes number of columns of matrix 1 for splitting into nested list
        matcolfield1.grid(row = 1, column = 0, ipadx = 0.1, ipady = 3, padx = 5, pady = 7.5)
        matcolfield1.bind('<Button-1>', msclick1)

        matcolfield2 = tk.Entry(matopslf, font = LargeFont, width = 12, textvariable = mat2var) #This field takes number of columns of matrix 2 for splitting into nested list
        matcolfield2.grid(row = 1, column = 1, ipadx = 0.1, ipady = 3, padx = 5, pady = 7.5)
        matcolfield2.bind('<Button-1>', msclick2)

        matcolfield3 = tk.Entry(matopslf, width = 8, textvariable = mat3var) #This field takes divisor for division
        matcolfield3.grid(row = 1, column = 2, ipadx = 0.1, ipady = 5, padx = 10, pady = 7.5, sticky = 'w')
        matcolfield3.bind('<Button-1>', msclick6)

        matdivfield = tk.Entry(matopslf, width = 8, textvariable = matdivvar) #This field takes divisor for division
        matdivfield.grid(row = 1, column = 2, ipadx = 0.1, ipady = 5, padx = 10, pady = 7.5, sticky = 'e')
        matdivfield.bind('<Button-1>', msclick7)

        mattext1 = tk.Text(matopslf, font = LargeFont, height = 7, width = 12) #This field takes input for matrix 1
        mattext1.grid(row = 2, column = 0, padx = 5, pady = 10)
        mattext1.bind('<Button-1>', msclick3)

        mattext2 = tk.Text(matopslf, font = LargeFont, height = 7, width = 12) #This field takes input for matrix 2
        mattext2.grid(row = 2, column = 1, padx = 5, pady = 10)
        mattext2.bind('<Button-1>', msclick4)

        mattext3 = tk.Text(matopslf, font = LargeFont, height = 7, width = 12) #This field takes input for matrix 3
        mattext3.grid(row = 2, column = 2, padx = 5, pady = 10)
        mattext3.bind('<Button-1>', msclick5)

        anstext = tk.Text(matopslf, font = LargeFont, height = 7, width = 12) #This field displays answer matrix
        anstext.grid(row = 2, column = 3, padx = 5, pady = 10)

        btnmatadd = ttk.Button(matopslf, text = 'Add', style = 'btn.TButton', command = lambda: matAdd()) #These buttons are for the different matrix operations
        btnmatadd.grid(row = 3, column = 0, padx = 10, pady = 10)

        btnmatsub = ttk.Button(matopslf, text = 'Subtract', style = 'btn.TButton', command = lambda: matSub()) 
        btnmatsub.grid(row = 3, column = 1, padx = 10, pady = 10)

        btnmatmul = ttk.Button(matopslf, text = 'Multiply', style = 'btn.TButton', command = lambda: matMul()) 
        btnmatmul.grid(row = 4, column = 0, padx = 10, pady = 10)

        btnmatdiv = ttk.Button(matopslf, text = 'Divide', style = 'btn.TButton', command = lambda: matDiv()) 
        btnmatdiv.grid(row = 4, column = 1, padx = 10, pady = 10)

        btninv = ttk.Button(matopslf, text = 'Inverse', style = 'btn.TButton', command = lambda: matInv()) 
        btninv.grid(row = 4, column = 2, padx = 10, pady = 10)

        btntrace = ttk.Button(matopslf, text = 'Trace', style = 'btn.TButton', command = lambda: matTrace()) 
        btntrace.grid(row = 3, column = 2, padx = 10, pady = 10)

        btndet = ttk.Button(matopslf, text = 'Determinant', style = 'btn.TButton', command = lambda: matDet()) 
        btndet.grid(row = 3, column = 3, padx = 10, pady = 10)

        btntranspose = ttk.Button(matopslf, text = 'Transpose', style = 'btn.TButton', command = lambda: matTrans()) 
        btntranspose.grid(row = 4, column = 3, padx = 10, pady = 10)

        resetbtn = ttk.Button(matopslf, text = 'Reset', style = 'btn.TButton', command = lambda: reset()) #This button resets all the fields in matrix label frame
        resetbtn.grid(row = 1, column = 3, padx = 10, pady = 10)

        otheropslf = tk.LabelFrame(self, text = 'Trigonometry and Logarithms:', font = LabelFont, fg = '#00adb5', bg = '#393e46') #This label frame contains everything for trig and logs
        otheropslf.grid(row = 1, column = 2, padx = 10, pady = 10)

        triglabel = tk.Label(otheropslf, text = 'Trigonometry:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Algebra Label
        triglabel.grid(row = 0, column = 0, padx = 2, pady = 10)

        trigfield = tk.Entry(otheropslf, width = 10, font = LargeFont, textvariable = trigvar) #This field takes input for trigonometric operation
        trigfield.grid(row = 1, column = 0, ipadx = 0.1, ipady = 3, padx = 2, pady = 7.5)
        trigfield.bind('<Button-1>', msclick8)

        clrtrigbutton = ttk.Button(otheropslf, text = 'Clear', style = 'btn.TButton', command = lambda: clrtrig()) #This button clears trigfield
        clrtrigbutton.grid(row = 1, column = 2, padx = 2, pady = 10)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('btn.TRadiobutton', font = ('Arial', 12, 'bold'), foreground = '#00adb5', background = '#222831', indicatorrelief = tk.FLAT, indicatormargin =- 1, indicatordiameter =- 1, relief = tk.RAISED, focusthickness = 0, highlightthickness = 0, padding = 5)
        s.map('btn.TRadiobutton', background=[('selected', '#222831'), ('active', '#222831')])

        degradio = ttk.Radiobutton(otheropslf, text = 'Degree', style = 'btn.TRadiobutton', variable = radiovar, value = 1)
        degradio.grid(row = 0, column = 1, padx = 2, pady = 10)

        radradio = ttk.Radiobutton(otheropslf, text = 'Radian', style = 'btn.TRadiobutton', variable = radiovar, value = 2)
        radradio.grid(row = 0, column = 2, padx = 2, pady = 10)

        btnsin = ttk.Button(otheropslf, text = 'Sin', style = 'btn.TButton', command = lambda: trigSin()) #These buttons are for different trig operations
        btnsin.grid(row = 2, column = 0, padx = 0, pady = 10)           

        btncos = ttk.Button(otheropslf, text = 'Cos', style = 'btn.TButton', command = lambda: trigCos())
        btncos.grid(row = 2, column = 1, padx = 0, pady = 10)

        btntan = ttk.Button(otheropslf, text = 'Tan', style = 'btn.TButton', command = lambda: trigTan())
        btntan.grid(row = 2, column = 2, padx = 7, pady = 10)

        btnarcsin = ttk.Button(otheropslf, text = 'Sin (-1)', style = 'btn.TButton', command = lambda: trigArcsin())
        btnarcsin.grid(row = 3, column = 0, padx = 0, pady = 10)           

        btnarccos = ttk.Button(otheropslf, text = 'Cos (-1)', style = 'btn.TButton', command = lambda: trigArccos())
        btnarccos.grid(row = 3, column = 1, padx = 0, pady = 10)

        btnarctan = ttk.Button(otheropslf, text = 'Tan (-1)', style = 'btn.TButton', command = lambda: trigArctan())
        btnarctan.grid(row = 3, column = 2, padx = 7, pady = 10)

        loglabel = tk.Label(otheropslf, text = 'Logarithms:', font = LabelFont, fg = '#00adb5', bg = '#222831') #Log Label
        loglabel.grid(row = 4, column = 0, padx = 2, pady = 7.5)

        logfield = tk.Entry(otheropslf, width = 10, font = LargeFont, textvariable = logvar) #This field takes input for logarithmic operation
        logfield.grid(row = 5, column = 0, ipadx = 0.1, ipady = 3, padx = 2, pady = 7.5)
        logfield.bind('<Button-1>', msclick9)

        clrlogbutton = ttk.Button(otheropslf, text = 'Clear', style = 'btn.TButton', command = lambda: clrlog()) #This button clears logfield
        clrlogbutton.grid(row = 5, column = 2, padx = 2, pady = 7.5)

        btnlog = ttk.Button(otheropslf, text = 'Log (e)', style = 'btn.TButton', command = lambda: loge()) #These buttons are for different log operations
        btnlog.grid(row = 6, column = 0, padx = 0, pady = 10)           

        btnlog10 = ttk.Button(otheropslf, text = 'Log (10)', style = 'btn.TButton', command = lambda: log10())
        btnlog10.grid(row = 6, column = 1, padx = 0, pady = 10)

        btnantilog = ttk.Button(otheropslf, text = 'Antilog', style = 'btn.TButton', command = lambda: antilog())
        btnantilog.grid(row = 6, column = 2, padx = 7, pady = 10)
        
class HistPage(tk.Frame): #This class is for the History page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = '#222831')

        label = tk.Label(self, text = 'Usage History', font = TitleFont, fg = '#00adb5', bg = '#222831') #Title label
        label.grid(row = 0, column = 1, padx = 350, pady = 10, sticky = 'nsew')

        def showHist(): #This function is to print usage history in text field
            try:
                global uHist
                
                n = len(uHist)
                element = ''
                for i in reversed(range(n)):
                    element = str(element + uHist[i] + '\n')
                history.insert(tk.END, element)            
            except:
                print("\nSomething went wrong!")

        def clrpage(): #This function is to clear the contents on usage history text field
            history.delete('1.0', 'end')

        def clrhist(): #This function is to delete the usage history
            global uHist
            uHist.clear()

        history = tk.Text(self, font = LargeFont, fg = '#00adb5', bg = '#393e46', height = 20, width = 80)
        history.grid(row = 1, column = 1, padx = 40, pady = 10)

        dispbutton = ttk.Button(self, text = 'Show', style = 'btn.TButton', command = lambda: showHist()) #This button displays usage history
        dispbutton.grid(row = 0, column = 0, padx = 10, sticky = 'w')

        clrtextbtn = ttk.Button(self, text = 'Clear Page', style = 'btn.TButton', command = lambda: clrpage()) #This button clears the history page
        clrtextbtn.grid(row = 1, column = 2, padx = 10, sticky = 'e')

        clrhistbtn = ttk.Button(self, text = 'Clear History', style = 'btn.TButton', command = lambda: clrhist()) #This button deletes usage history
        clrhistbtn.grid(row = 1, column = 2, padx = 10, sticky = 'ne')

        choicebutton = ttk.Button(self, text = 'Choices', style = 'btn.TButton', command = lambda: controller.show_frame(ChoicePage)) #This button takes us to the choices page
        choicebutton.grid(row = 0, column = 2, padx = 10, sticky = 'e')

root = Calculator()

icon = Image.open(r'calcicon.png') #This is to make the calculator icon utilizing PIL's modules
icon = icon.resize((64, 64), Image.ANTIALIAS) #Resize icon to desirable size
icon = ImageTk.PhotoImage(icon) #Make the icon file readable
root.iconphoto(False, icon)

root.mainloop()
