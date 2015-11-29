__author__ = 'Abhi'

#Importing Tkinter
from tkinter import *

#Defining Myexception class to handle exceptions and print appropriate messages
class MyException(Exception):  # inherit from Exception
    error_description1 = "Only aplhabets allowed for"
    error_description2 = "please select appropriate value in radio button"
    error_description3 = "Image not found,please check your path"

    #constructor
    def __init__(self, value):
       self.value = value
    def __str__(self):
       return repr(self.value)


#Declaring fields used for text input
fields = 'Last Name', 'First Name', 'City', 'Country'

#This method prints field and text value entered, when show button is clicked
def fetch(entries):

      for entry in entries:
        field = entry[0]
        text  = entry[1].get()

        #raise an exception and  print an error message, if text entered contains characters other than alphabets.
        # else print the field
        try:
            if text.isalpha() == FALSE:
               raise MyException(text)
            else:
                print('%s: "%s"' % (field, text))
        except MyException:
            print(MyException.error_description1 + field)
            break

#This method creates labels for fields(lastname,firstname,city) declared and appends values entered in text fields to entries list
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      #Creating label for field and adjusting its position on screen with height and width
      lab = Label(row, width=15, text=field, anchor='w',font = "Verdana 10 bold")
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      #appending field and text value entered to entries.
      entries.append((field, ent))
   return entries



def radio(event):
#checking for appropriate selection  values of radio button,exception is raised if user doesnot select
    try:
        if v.get() != 1 and v.get() != 2 and v.get() != 3:
            raise MyException(event)
    except MyException:
        print(MyException.error_description2)
        quit()

#This class inherited from Frame creates Checkbox
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   #tracks status of the checkbox
   def state(self):
      return map((lambda var: var.get()), self.vars)

#Displays radio button selected
def ShowChoice():
   pass


if __name__ == '__main__':
    #initialize Tkinter
   root = Tk()

  #Handling exception when image file not found
   try:
      palacelogo = PhotoImage(file="palaceimage.gif")
      w1 = Label(root,image=palacelogo).pack(side="top")
   except TclError:
      print(MyException.error_description3)

   #Displaying heading of application
   Label(root,text="""Player Registration""",font = "Verdana 14 bold", fg = "blue",bg = "yellow").pack()


#Creating radio buttons
v = IntVar()
#v.set(1)  # initializing the choice
l1 =Label(root,text="""Choose your mode of play:""",font = "Verdana 10 bold")
l1.pack(anchor = W)
modes = [("Online",1),("Virtual",2),("Live",3),]
for txt, val in modes:
        Radiobutton(root,text=txt,padx = 2,variable=v,command=ShowChoice,value=val).pack(anchor = W)


#Label for checkbox
l2 =Label(root, text="""Choose your language:""",font = "Verdana 10 bold")
l2.pack(anchor = W)
#checkbox names
lng = Checkbar(root, ['English', 'Spanish', 'Russian'])
lng.pack(anchor =W)

#fetching values of entries,when show button is clicked
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e)))

#Show button
b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
#calling exception handler of radio button
b1.bind( '<Button-1>',radio)
b1.pack(side=LEFT, padx=5, pady=5)

#Quit Button exits Tkinter application
b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)
#for displaying widgets until termination
root.mainloop()

