from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import predictor
import os  

def onClick():
    global message ,file ,image ,img  ,graph
    #os.system("script2.py "+ rain.get() +" " + temp.get()+ " " + Population_density.get())
    # filo = open("private 2.txt", "r")
    value = predictor.predict(city.get(),tempe.get(), rain.get() ,pop_den.get())
    # print(value)
    ########### MAKING GRAPH ###############################
    file = "C:\\Users\\acer\\Desktop\\programme_codes\\disease-outbreaks-predictor\\output.png" 
    image = Image.open(file)
    image = image.resize((1450,450), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(image)

    graph =Label(lowerFrame , image =img)
    graph.grid(row=0,column=0,columnspan=14,pady=2,padx=40)

    out1 = str(int(value[0]))  
    message = "The predicted disease count of next year is  "  + out1  
    answer["text"]=message 
    temp_contri["text"]="Current Temperature contribution is: " + str(value[1][0]/(sum(value[1]))*100)[:5]
    rain_contri["text"]="Current Rainfall contribution is: "  +  str(value[1][1]/(sum(value[1]))*100)[:5]
    pop_contri["text"]="Current  Population Density contribution is: " + str(value[1][2]/(sum(value[1]))*100)[:5]


message = '' 

#creating basic window 
window  = Tk()
window.geometry("1520x780") # size of window width:- 500 ,height :- 375
window.resizable(0,0) #this prevents from resizing 
window.title("predicto") 
window.configure(bg="#3E342C")

top_frame = Frame(window)
top_frame.pack()

Topic = Label(top_frame,text="Disease Outbreak Predictor",font=("Calibri (Body)",30,'bold'),fg="#008F11",bg="black",width=780)
Topic.pack(ipady=10)

bottom_frame = Frame(window,bg="#312A24")
bottom_frame.pack(pady=20)

rain_label = Label(bottom_frame,text="Rainfall", font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
rain_label.grid(row=0,column=0, pady=5 ,padx=1,sticky=W)

rain = IntVar()
rainfall = Entry(bottom_frame, font = ('Calibri (Body)' ,12,'bold'),bg="#AA8F79", textvariable = rain)
rainfall.grid(row=0,column=1, pady=5, padx=10)

temp_label = Label(bottom_frame,text="Temperature", font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
temp_label.grid(row=0,column=2, pady=5 ,padx=10,sticky=W)

tempe = IntVar()
temp = Entry(bottom_frame, font = ('Calibri (Body)' ,12 ,'bold'),bg="#AA8F79" , textvariable = tempe)
temp.grid(row=0,column=3, pady=5, padx=4)

Pop_label = Label(bottom_frame,text="Population Density", font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
Pop_label.grid(row=0,column=4, pady=5, padx=10,sticky=W)

pop_den= IntVar()
Population_density = Entry(bottom_frame, font = ('Calibri (Body)' ,12 ,'bold'),bg="#AA8F79", textvariable = pop_den)
Population_density.grid(row=0,column=5, pady=5, padx=4)

city_label = Label(bottom_frame,text="Subdivision", font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
city_label.grid(row=0,column=6, pady=5, padx=5,sticky=W)


#this is just for combo box font stly change 
bigfont = font.Font(family="Calibri (Body)",size=12)
bottom_frame.option_add("*TCombobox*Listbox*Font", bigfont)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': "#AA8F79",
                                       'fieldbackground': '#AA8F79',
                                       'background': '#AA8F79',
                                       'foreground':'black',
                                       'selectforeground':'black'
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle') 

values = ["city10" , "city9" , "city8" , "city7" ,"city6","city5" , "city4" ,"city3" ,"city2" ,"city1"]
city = ttk.Combobox(bottom_frame, width=40, values=values ,state='readonly',justify='center')
city.set("Select")
city.grid(row=0,column=7,columnspan=4,pady=5,padx=10)

btn1 = Button(bottom_frame, text =' Predict ' ,command = onClick, font = ('Calibri (Body)' ,12 ,'bold'),fg = "black" ,width = 10 ,height =1 ,bd = 0.5 ,bg = "#AA8F79") 
btn1.grid(row=0,column=11,columnspan=3,pady=20,padx=4)

lowerFrame = Frame(window,bg="#312A24")
lowerFrame.pack(expand=True ,fill=BOTH)

file ="C:\\Users\\acer\\Desktop\\programme_codes\\disease-outbreaks-predictor\\output.png" 
image = Image.open(file)
image = image.resize((1450,450), Image.ANTIALIAS)
img= ImageTk.PhotoImage(image)

graph =Label(lowerFrame , image =img)

answer = Label(lowerFrame,text='', font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
answer.grid(row=1,column=0,columnspan=10,pady=0,padx=0 )

temp_contri = Label(lowerFrame,text='', font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
temp_contri.grid(row=2,column=0,columnspan=10,pady=0,padx=0 )

rain_contri = Label(lowerFrame,text='', font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
rain_contri.grid(row=3,column=0,columnspan=10,pady=0,padx=0 )

pop_contri = Label(lowerFrame,text='', font = ('Calibri (Body)' ,12 ,'bold'),fg="#AA8F79",bg="#312A24")
pop_contri.grid(row=4,column=0,columnspan=10,pady=0,padx=0 )

window.mainloop()

