from tkinter import*

root = Tk()

root.title("Driving license")
root.geometry("500x400")
root.configure(bg= "white")

canvas=Canvas(root,width=300,height=400) 
canvas.create_image(0,0,anchor=NW) 
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Driving License")
label_name_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :") 
label_DOB_tag = canvas.create_text(50,205, font=('Times', '16', 'bold') ,text="DOB :")
label_Pinno_tag = canvas.create_text(50,245, font=('Times', '16', 'bold') ,text="Pin Num :")
label_address_tag = canvas.create_text(50,290, font=('Times', '16', 'bold') ,text="Address :")
label_typeofvehicle_tag = canvas.create_text(80,330, font=('Times', '16', 'bold') ,text="Authorization for vehicles  :")

label_name = Label(root) 
label_DOB = Label(root) 
label_Pinno = Label(root) 
label_address = Label(root) 
label_typeofvehicle = Label(root) 

def myCardDetails():
    name = "Mosikaran" 
    print(type(name)) 
    DOB = 13
    print(type(DOB)) 
    Pinno = ["451379"]
    print(type(Pinno)) 
    address = "chennai,tamilnadu"
    print(type(address)) 
    typeofvehicle = "four wheeler"
    print(type(typeofvehicle)) 
    
    label_name['text'] = name
    label_DOB['text'] = DOB
    label_Pinno['text'] = Pinno 
    label_address['text'] = address 
    label_typeofvehicle['text'] = typeofvehicle

button1 = Button(root, text = "Show my Driving License", command=myCardDetails)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT) 
button1_window = canvas.create_window(150, 360, anchor=CENTER, window=button1) 
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name) 
label_DOB_window = canvas.create_window(120, 205, anchor=CENTER, window=label_DOB) 
label_Pinno_window = canvas.create_window(140,245, anchor=CENTER, window=label_Pinno) 
label_address_window = canvas.create_window(150, 290, anchor=CENTER, window=label_address) 
label_typeofvehicle_window = canvas.create_window(250 , 330, anchor=CENTER, window=label_typeofvehicle) 
canvas.pack()        

root.mainloop()
