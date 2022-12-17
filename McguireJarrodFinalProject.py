#SDEV140 Final Project
#dorm.py
#Author: Jarrod McGuire
#This program will assist college students in preparing to pack before moving into their dorm at college

#import Python GUI Tkinter and modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
#from tkinter.ttk import *




#Create a new window to hold our GUI
#using tKinter to make the GUI
#setting an icon in the window, title, size, and setting up rows and columns - similar on other windows
window = tk.Tk()
window.iconbitmap("icon2.ico")
window.title("Dorm Room Planner")
window.geometry("300x300+150+150")
#row set up
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 0)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1)
window.rowconfigure(4, weight = 1)
window.rowconfigure(5, weight = 1)
window.rowconfigure(6, weight = 1)
window.rowconfigure(7, weight = 1)
#column set up
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)



#A label with the title of the program
lbl_header = Label(window, text = "Dorm Room Planner", foreground = "white", background = "light blue")
lbl_header.grid(row = 0, column = 0, columnspan = 4)

#adding images to the window
logo = ImageTk.PhotoImage(Image.open("dorm3.gif"))
logoLabel = Label(image = logo)
logoLabel.grid(row = 1, column = 0)
altText1Label = Label(window, text = "dorm", font=("Helvetica", 9))
altText1Label.grid(row = 2, column = "0", sticky = N)

logo2 = ImageTk.PhotoImage(Image.open("furniture2.gif"))
logo2Label = Label(image = logo2)
logo2Label.grid(row = 1, column = 3)
altText2Label = Label(window, text = "couch", font=("Helvetica", 9))
altText2Label.grid(row = 2, column = "3", sticky = N)

#image for window 3
dormLogo = ImageTk.PhotoImage(Image.open("dorm3.gif"))

infoLabel = Label(window, text = "Rm2 +$50...Rm3 +$75",
                   foreground = "white", background = "gray")
infoLabel.grid(row = 5, column = 0, columnspan = 4)


#radio buttons to select room size
v = IntVar(value=1)         #automatically select option 1...v=IntVar(value=1)

room1 = tk.Radiobutton(window,
               text="Room 1 ( NO Wi-Fi )",
               padx = 20, 
               variable=v, 
               value=1).grid(row = 3, column = 0, columnspan = 4)

room2 = tk.Radiobutton(window, 
               text="Room 2 (Wi-Fi Reg)",
               padx = 20, 
               variable=v, 
               value=2).grid(row = 4, column = 0, columnspan = 4)

room3 = tk.Radiobutton(window, 
               text="Room 3 (Wi-Fi Fast)",
               padx = 20, 
               variable=v, 
               value=3).grid(row = 5, column = 0, columnspan = 4)



#Second window for furniture selection
#set up a class with functions within the class
class furnitureWindow():
    def __init__(self):
        
        self.furniture = Tk()
        self.furniture.title("Dorm Room Furniture")
        self.furniture.geometry("400x600+150+150")
        #print confirms to terminal that the button from window 1 worked
        print("Room Selected")
        
        # This code is for the furniture screen title
        self.dormFurniture = Label(self.furniture,
                            text="Mark the furniture you would like to have.",
                            font=("Helvetica", 10)
                            )
        self.dormFurniture.pack()

        self.setUp()
        
        #count the items selected
    def getItemCount(self):
        result = self.bedVar.get() + self.bedFullVar.get() + self.deskVar.get() + self.dresserVar.get() + self.dresserLgVar.get() + self.bookShelfVar.get() + self.nightVar.get() + self.tvVar.get() + self.fridgeVar.get()
        print(result)
        return result

    #checking to see if there is enough room or not...if so, messageWindow() is called and user taken to 3rd window
    def roomCheck(self):
        if self.getItemCount() < 10:
            roomCheckLabel = Label(self.furniture, text="Select more items").pack()
            print("Select more items")
        elif self.getItemCount() > 14:
            roomCheckLabel = Label(self.furniture, text="NOT enough room.  You are " + str(self.getItemCount() - 14) + "ft over.  Select less items").pack()
            print("NOT enough room.  You are " + str(self.getItemCount() - 14) + "ft over.  Select less items")
        else:
            messageWindow()

#functions to get info from checkboxes and print to terminal
#bedLable (and others) were used for testing purposes to see values.
    def showBed(self):
        #self.bedLabel = Label(self.furniture, text=self.bedVar.get()).pack()
        print(self.bedVar.get())

    def showBedFull(self):
            #self.bedFullLabel = Label(self.furniture, text=self.bedFullVar.get()).pack()
            print(self.bedFullVar.get())


    def showDesk(self):
        #self.deskLabel = Label(self.furniture, text=self.deskVar.get()).pack()
        print(self.deskVar.get())

    def showDresserLg(self):
        #self.dresserLgLabel = Label(self.furniture, text=self.dresserLgVar.get()).pack()
        print(self.dresserLgVar.get())

    def showDresser(self):
        #self.dresserLabel = Label(self.furniture, text=self.dresserVar.get()).pack()
        print(self.dresserVar.get())

    def showbookShelf(self):
        #self.bookShelfLabel = Label(self.furniture, text=self.bookShelfVar.get()).pack()
        print(self.bookShelfVar.get())

    def showNight(self):
        #self.nightLabel = Label(self.furniture, text=self.nightVar.get()).pack()
        print(self.nightVar.get())

    def showTv(self):
        #self.tvLabel = Label(self.furniture, text=self.tvVar.get()).pack()
        print(self.tvVar.get())

    def showFridge(self):
        #self.fridgeLabel = Label(self.furniture, text=self.fridgeVar.get()).pack()
        print(self.fridgeVar.get())

    def setUp(self):
    
        # defining variables from buttons...NOTICE...have to pass self.furniture as argument.  
        # Python is storing data in window 1 which is paused in background while this window is open.  
        # Passing the self.furniture will allow the get() to work and use the variables in this window
        self.bedVar = IntVar(self.furniture)

        # Here is the code for each of the dorm furniture checkbox buttons
        self.bedButton = Checkbutton(self.furniture,
                                    text="Bed Twin (4u)",
                                    height=2,
                                    width=15,
                                    variable=self.bedVar,
                                    onvalue=4,
                                    offvalue=0,
                                    command = self.showBed,
                                    )
        self.bedButton.pack()
        # bedTwinButton.select()
        #myButton = Button(furniture, text="Select", command=showBed).pack()

        self.bedFullVar = IntVar(self.furniture)
        self.bedFullButton = Checkbutton(self.furniture,
                                    text="Bed Full (5u)",
                                    height=2,
                                    width=15,
                                    variable=self.bedFullVar,
                                    onvalue=5,
                                    offvalue=0,
                                    command = self.showBedFull
                                    )
        self.bedFullButton.pack()
        # bedFullButton.select()
        #myButton = Button(furniture, text="Select", command=showBed).pack()

        self.deskVar = IntVar(self.furniture)
        self.deskButton = Checkbutton(self.furniture,
                                    text="Desk (3u)",
                                    height=2,
                                    width=15,
                                    variable=self.deskVar,
                                    onvalue=3,
                                    offvalue=0,
                                    command = self.showDesk)
        self.deskButton.pack()
        #myButton2 = Button(furniture, text="Select", command=showDesk).pack()

        self.dresserVar = IntVar(self.furniture)
        self.dresserButton = Checkbutton(self.furniture,
                                    text="Dresser (2u)",
                                    height=2,
                                    width=15,
                                    variable=self.dresserVar,
                                    onvalue=2,
                                    offvalue=0,
                                    command = self.showDresser)
        self.dresserButton.pack()
        #myButton3 = Button(furniture, text="Select", command=showDress).pack()

        self.dresserLgVar = IntVar(self.furniture)
        self.dresserLgButton = Checkbutton(self.furniture,
                                    text="Dresser-Lg (3u)",
                                    height=2,
                                    width=15,
                                    variable=self.dresserLgVar,
                                    onvalue=3,
                                    offvalue=0,
                                    command = self.showDresserLg)
        self.dresserLgButton.pack()
        #myButton3 = Button(furniture, text="Select", command=showDresserLg).pack()

        self.bookShelfVar = IntVar(self.furniture)
        self.bookShelfButton = Checkbutton(self.furniture,
                                    text="Bookshelf (2u)",
                                    height=2,
                                    width=15,
                                    variable=self.bookShelfVar,
                                    onvalue=2,
                                    offvalue=0,
                                    command = self.showbookShelf)
        self.bookShelfButton.pack()
        #myButton4 = Button(furniture, text="Select", command=showbookShelf).pack()


        self.nightVar = IntVar(self.furniture)
        self.nightButton = Checkbutton(self.furniture,
                                    text="Night Stand (1u)",
                                    height=2,
                                    width=15,
                                    variable=self.nightVar,
                                    onvalue=1,
                                    offvalue=0,
                                    command = self.showNight)
        self.nightButton.pack()
        #myButton5 = Button(furniture, text="Select", command=showNight).pack()

        self.tvVar = IntVar(self.furniture)
        self.tvButton = Checkbutton(self.furniture,
                                    text="TV Stand (2u)",
                                    height=2,
                                    width=15,
                                    variable=self.tvVar,
                                    onvalue=2,
                                    offvalue=0,
                                    command = self.showTv)
        self.tvButton.pack()
        #myButton6 = Button(furniture, text="Select", command=showTv).pack()

        self.fridgeVar = IntVar(self.furniture)
        self.fridgeButton = Checkbutton(self.furniture,
                                    text="Mini-Fridge (2u)",
                                    height=2,
                                    width=15,
                                    variable=self.fridgeVar,
                                    onvalue=2,
                                    offvalue=0,
                                    command = self.showFridge)
        self.fridgeButton.pack()
        #myButton7 = Button(furniture, text="Select", command=showFrdige).pack()

        # Check button will see if they have enough room for the items selected by calling a function
        self.checkButton = Button(self.furniture, text="Check", command=self.roomCheck)
        # checkButton.grid(row=5, column=0, columnspan=4)
        self.checkButton.pack()

        self.exit2Button = Button(self.furniture, text="Exit", command=self.furniture.quit)
        # exit2Button.grid(row=6, column=0, columnspan=4)
        self.exit2Button.pack()




#final window to show success and say good-bye
def messageWindow():
    message = Toplevel(window)
    message.title("Good-Bye")
    message.geometry("400x400+150+150")
    message.rowconfigure(0, weight = 0)
    message.rowconfigure(1, weight = 0)
    message.rowconfigure(2, weight = 1)
    message.rowconfigure(3, weight = 1)
    message.rowconfigure(4, weight = 1)
    message.columnconfigure(0, weight = 1)
    message.columnconfigure(1, weight = 1)
    message.columnconfigure(2, weight = 1)
    message.columnconfigure(3, weight = 1)
    
    #let us know if we successfully made it to window 3
    print("Success!")
    
    messageLabel = Label(message,
                    text = "Success!  Enjoy Your Stay.",
                    font = ("Helvetica", 18)
                    )
    messageLabel.grid(row = 0, column = 0, columnspan = 4)
    
    dormLogoLabel = Label(message, image = dormLogo)
    dormLogoLabel.grid(row = 1, column = 0, columnspan = 4)
    altText3Label = Label(message, text = "dorm", font=("Helvetica", 9))
    altText3Label.grid(row = 2, column = "0", columnspan = 4, sticky = N)

    finishButton = Button(message, text = "Finish", command = window.quit)
    finishButton.grid(row = 3, column = 0, columnspan = 4)    



#button to confirm selction
selectButton = Button(window, text = "Select", command = furnitureWindow)
selectButton.grid(row = 6, column = 0, columnspan =4)
#button to exit program
exitButton = Button(window, text = "Exit", command = window.quit)
exitButton.grid(row = 7, column = 0, columnspan = 4)



def main():
    #Starts the first window
    window.mainloop()
    exit()

if __name__ == "__main__":
    main()
