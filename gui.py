

#CREATING CALCULATOR
import tkinter as tk
mainWindow= tk.Tk()
mainWindow.title("CALCULATOR")

heading_label = tk.Label(mainWindow,text="Enter first number", pady=(10),padx=(20))
heading_label.pack()

first_number_entry = tk.Entry(mainWindow)
first_number_entry.pack()


s_num_label2 = tk.Label(mainWindow, text="Enter the second number",pady=(10),padx=(20))
s_num_label2.pack()

s_num_entry = tk.Entry(mainWindow)
s_num_entry.pack()

op_label = tk.Label(mainWindow, text="Choose Operation",pady=(10),padx=(20))
op_label.pack()


button1 = tk.Button(mainWindow, text="+",pady=(10),padx=(10),command= lambda :addition())
button1.pack()


button2 = tk.Button(mainWindow, text="-",pady=(10),padx=(10),command= lambda :minus())
button2.pack()

button3= tk.Button(mainWindow, text="*",pady=(10),padx=(10),command=lambda :multiply())
button3.pack()

button4= tk.Button(mainWindow, text="/",pady=(10),padx=(10),command=lambda :division())
button4.pack()

result_label = tk.Label(mainWindow,text="Result",pady=(10),padx=(20))
result_label.pack()

def addition():
    first=int(first_number_entry.get())
    second=int(s_num_entry.get())
    result = first+second
    print("Result is:", result)
    result_label.config(text="Operation result is:"+ str(result))

def minus():
    first=int(first_number_entry.get())
    second=int(s_num_entry.get())
    result = first-second
    print("Result is:", result)
    result_label.config(text="Operation result is:"+ str(result))

def multiply():
    first=int(first_number_entry.get())
    second=int(s_num_entry.get())
    result = first*second
    print("Result is:", result)
    result_label.config(text="Operation result is:"+ str(result))

def division():
    first=int(first_number_entry.get())
    second=int(s_num_entry.get())
    result = first/second
    print("Result is:", result)
    result_label.config(text="Operation result is:"+ str(result))

mainWindow.mainloop()
