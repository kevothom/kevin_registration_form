from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():      
    print("Job well done")


# Heading
Label(root, text=" Kevin Thomas Registration Form", font="ar 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone") 
gender = Label(root, text="Gender")
emergencycontact = Label(root, text="Emergenct Contact")
paymenttype = Label(root, text="Payment Type")


# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergencycontact.grid(row=4, column=2)
paymenttype.grid(row=5, column=2)

# Variables for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencycontactvalue = StringVar
paymenttypevalue = StringVar
checkvalue = IntVar
submitvalue = IntVar

# Creating Entry Fields
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emergencycontactentry = Entry(root, textvariable =emergencycontactvalue)
paymenttypeentry = Entry(root, textvariable =paymenttypevalue)

# Packing Entry Field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencycontactentry.grid(row=4, column=3)
paymenttypeentry.grid(row=5, column=3)

# Creating Check Box
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

# Creating Submitting Box
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
