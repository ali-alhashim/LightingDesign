import tkinter as tk
from tkinter.constants import LEFT, X
from tkinter import ttk
from typing import Text 
# lux level = (lumen * CU * LF) / area
# No lamp needed =( Required lux * area ) / (lumens * CU * LF)
# Code by Ali Alhashim ( AliCode.io@gmail.com )
#
#
class MainWindow():
    def __init__(self,mainW):
        
        self.mainW = mainW
        mainW.title("Lighting Design")
        mainW.geometry("720x400+0+0")
        
        frame1 = tk.Frame(mainW)
        frame1.pack()

        frame2 = tk.Frame(mainW, background='#e6ba34')
        frame2.pack(fill=X)

        frame3 = tk.Frame(mainW, background='#87c6cd')
        frame3.pack(fill=X,pady=20)

        frame4 = tk.Frame(mainW, background='#c5aa84')
        frame4.pack(fill=X,pady=20)

        ###_______________________________________________________###
        self.LuxStandards = {
                         'Badroom':'150',
                         'Living rooms':'150',
                         'Aircraft Hanger ':'500',
                         'Under Pipe-ways':'30',
                         'Piers':'200',
                         'Regualr Office':'500',
                         'CAD Work Station':'500',
                         'Conference Room':'500',
                         'Elevators':'200',
                         'Corridors':'75',
                         'Stairways':'75',
                         'Washrooms':'150',
                         'Control Room':'500',
                         'Instrument Panels':'500',
                         'Consoles':'500',
                         'Back of Panel':'100',   
                         'Dining Area':'150',
                         'Dining Area Service':'300',
                         'Food Preparation':'500',
                         'Entrance Halls':'200',
                         'Electrical Room':'300',
                         'Outdoor Switch Yard':'20',
                         'General Substation(outdoor)':'20',
                         'General Substation(indoor)':'50',
                         'Indoor Substation Operating Aisles':'150',
                         'Powerhouse Contral Area':'300',
                         'Powerhouse Burner Platform':'150',
                         'Powerhouse Contral Desk':'500',
                         'Powerhouse Gauges':'300',
                         'Compressor Area':'50',
                         'Pump Rows':'50',
                         'Tank Stairs':'15',
                         'Tank Truck (Loading Point)':'100',
                         'Firehouse Repairs & Service Area':'750',
                         'Firehouse Storage Parts':'300',
                         'Labratories Washrooms':'300',
                         'Labratories Physical':'500',
                         'Labratories Stock Rooms':'150',
                         'Locker Room Shower':'100',
                         'Lavatory W.C.':'200',
                         'School Classrooms':'750',
                         'School Manual Training':'1000',
                         'School Library':'750',
                         'School Corridors':'200',
                         'Football':'200',
                         'Gym':'300',
                         'Tennis':'300',
                         'Basketball':'300',
                         'Local Road':'10',
                         'Parking Lots':'10'
                        }
        ###_______________________________________________________###

        ##---------- frame1------------##
        self.Label1 = tk.Label(master=frame1, text ="Lighting Design Calculator", font='arial 14 bold')
        self.Label1.pack()


        self.Label2 = tk.Label(master=frame1, text ="Area = ")
        self.Label2.pack(padx=5, pady=20,side=tk.LEFT)

        self.Label3 = tk.Label(master=frame1, text ="width : ")
        self.Label3.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtWidthX = tk.StringVar()
        self.txtWidth = tk.Entry(master=frame1,textvariable=self.txtWidthX)
        self.txtWidth.insert(0,"1")
        self.txtWidth.pack(padx=5, pady=20,side=tk.LEFT)
        self.txtWidthX.trace('w',self.AreaResult)

        self.Label5 = tk.Label(master=frame1, text ="*")
        self.Label5.pack(padx=5, pady=20,side=tk.LEFT)

        self.Label6 = tk.Label(master=frame1, text ="length : ")
        self.Label6.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtLengthX = tk.StringVar()
        self.txtLength = tk.Entry(master=frame1, textvariable=self.txtLengthX)
        self.txtLength.insert(0,"1")
        self.txtLength.pack(padx=5, pady=20,side=tk.LEFT)
        self.txtLengthX.trace('w',self.AreaResult)
        

        self.Label8 = tk.Label(master=frame1, text =" = ")
        self.Label8.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtArea = tk.Entry(master=frame1)
        self.txtArea.insert(0,"1")
        self.txtArea.pack(padx=5, pady=20,side=tk.LEFT)

        ##______________frame2______________##
        self.Label9 = tk.Label(frame2, text='lumen :', background='#e6ba34')
        self.Label9.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtLumen = tk.Entry(frame2)
        self.txtLumen.pack(padx=5, pady=20,side=tk.LEFT)

        self.Label10 = tk.Label(frame2, text='Watt :', background='#e6ba34')
        self.Label10.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtWatt = tk.Entry(frame2)
        self.txtWatt.pack(padx=5, pady=20,side=tk.LEFT)


        self.Label11 = tk.Label(frame2, text='CU :', background='#e6ba34')
        self.Label11.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtCU = tk.Entry(frame2)
        self.txtCU.insert(0,"0.6")
        self.txtCU.pack(padx=5, pady=20,side=tk.LEFT)


        self.Label12 = tk.Label(frame2, text='LF :', background='#e6ba34')
        self.Label12.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtLF = tk.Entry(frame2)
        self.txtLF.insert(0,"0.8")
        self.txtLF.pack(padx=5, pady=20,side=tk.LEFT)

        ##______________frame3________________##

        self.Label3 = tk.Label(frame3, text='Application Area :', background='#87c6cd')
        self.Label3.pack(padx=5, pady=20,side=tk.LEFT)
        
        
        self.areaBox = ttk.Combobox(frame3,values=list(self.LuxStandards.keys()),width=40)
        self.areaBox.pack(padx=5, pady=20,side=tk.LEFT)
        
        self.areaBox.bind("<<ComboboxSelected>>", self.SelectedApplicationArea)

        


        self.Label4 = tk.Label(frame3, text='Target Lux:', background='#87c6cd')
        self.Label4.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtTargetLux = tk.Entry(frame3)
        self.txtTargetLux.pack(padx=5, pady=20,side=tk.LEFT)

        self.btnStart = tk.Button(frame3,text='Start Calculating',command=self.StartCalculating)
        self.btnStart.pack(padx=5, pady=20)

        ##---------------frame4-------------------##

        self.Label5 = tk.Label(frame4, text='Lux Level :', background='#c5aa84')
        self.Label5.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtLuxLevel = tk.Entry(frame4)
        self.txtLuxLevel.pack(padx=5, pady=20,side=tk.LEFT)


        self.Label6 = tk.Label(frame4, text='Quantity of needed lamps :', background='#c5aa84')
        self.Label6.pack(padx=5, pady=20,side=tk.LEFT)

        self.txtNeededLamps = tk.Entry(frame4)
        self.txtNeededLamps.pack(padx=5, pady=20,side=tk.LEFT)


        self.Label6 = tk.Label(frame4, text='Power Consumption :', background='#c5aa84')
        self.Label6.pack(padx=5, pady=20,side=tk.LEFT)


        self.txtPowerCons = tk.Entry(frame4)
        self.txtPowerCons.pack(padx=5, pady=20,side=tk.LEFT)

        ##--------------------------------------##

    def AreaResult(self,*args):
        self.areaX = float(self.txtWidth.get()) * float(self.txtLength.get())
        self.txtArea.delete(0,'end')
        self.txtArea.insert(0,self.areaX)

    def StartCalculating(self,*args):

        #No lamp needed =( Required lux * area ) / (lumens * CU * LF)
        NeededLamp = (float(self.txtTargetLux.get()) * float(self.txtArea.get())) / (float(self.txtLumen.get()) * float(self.txtCU.get()) * float(self.txtLF.get()))
        self.txtNeededLamps.delete(0,'end')
        self.txtNeededLamps.insert(0,int(NeededLamp))
        # lux level = (lumen * CU * LF) / area
        totalLumen = float(self.txtLumen.get()) * int(NeededLamp)
        luxLevel = (float(totalLumen) * float(self.txtCU.get()) * float(self.txtLF.get())) / (float(self.txtArea.get()))
        self.txtLuxLevel.delete(0,'end')
        self.txtLuxLevel.insert(0,luxLevel)

        #Power 
        PowerCons = int(NeededLamp) * float(self.txtWatt.get())
        self.txtPowerCons.delete(0,'end')
        self.txtPowerCons.insert(0,PowerCons)

        #--GUI Design & pdf----------------------------

        self.DesignWindow = tk.Tk()
        
        self.DesignWindow.title('Design View')
        self.DesignWindow.geometry('620x877+750+0')
        
        lengthLable = tk.Label(self.DesignWindow,text=self.txtLength.get())
        lengthLable.grid(row=1,column=2)

        roomGeometry = tk.Canvas(self.DesignWindow,width=37*int(self.txtWidth.get()) ,height=37*int(self.txtLength.get()) ,bg='#ffffff',borderwidth=1,relief="solid")
        roomGeometry.grid(row=1,column=3)

        lengthLable = tk.Label(self.DesignWindow,text=self.txtWidth.get())
        lengthLable.grid(row =2,column=3)

        
        for w in range(int(self.txtLength.get())):
            
            
            for h in range(int(self.txtWidth.get())):
                top = w * 37
                left = h * 37
                bottom = w * 37 + 37 +2
                right = h * 37 + 37 +2
                
                roomGeometry.create_rectangle(left,top,right,bottom,fill='#ffffff',outline='black')
                
        #_______________Lighting distribution ___________________#
        
        #Factorzation 
        nX = int(NeededLamp)
        
        i = 1 
        x = []
        x2 = []
        while i <= nX:
            if nX % i == 0 :
                x.append([int(i), int(nX / i)])
            i = i + 1

        for p in range(len(x)):
            x2.append(sum(x[p]))

        keyX = x2.index(min(x2))
        
        xy = x[keyX]
        
        AxisX = xy[0]

        AxisY = xy[1]

        Label14 = tk.Label(self.DesignWindow,text='Lighting distribution : Axis X = '+str(AxisX) +" Axis Y = "+str(AxisY))
        Label14.grid(row=1,column=4)

        for p1 in range(AxisY):
            for p2 in range(AxisX):
                top = p1 * 30
                left = p2 * 30
                bottom = p1 * 30 + 30 +2
                right = p2 * 30 + 30 +2
                lamp = roomGeometry.create_oval(left,top,right,bottom,fill="red")

        



         



        


        
        


        ##---------------------------------------------##

    def SelectedApplicationArea(self,*args):
        
        
        
        self.txtTargetLux.delete(0,'end')
        self.txtTargetLux.insert(0,self.LuxStandards[self.areaBox.get()])

        




if __name__ == "__main__":
    root = tk.Tk()
    myGUI = MainWindow(root)
    root.mainloop()
