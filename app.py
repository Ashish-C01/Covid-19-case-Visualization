from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
root=Tk()
def graph():
    df=pd.read_csv('https://data.covid19india.org/csv/latest/case_time_series.csv')
    value1=clicked.get()
    value2=clicked1.get()
    fig,ax=plt.subplots()
    if value1=='India':
        data2=pd.read_csv(str(value2)+'.csv') 
        plt.plot(data2['Confirmed'],label=value2)
        plt.plot(df['Daily Confirmed'],label='India')
        plt.ylabel('Number of cases')
        plt.xlabel('Days')
    elif value2=='India':
        data1=pd.read_csv(str(value1)+'.csv')
        plt.plot(data1['Confirmed'],label=value1)
        plt.plot(df['Daily Confirmed'],label='India')
        plt.ylabel('Number of cases')
        plt.xlabel('Days')
    else:
        plt.plot(df['Daily Confirmed'],label='India')
        data1=pd.read_csv(str(value1)+'.csv')
        data2=pd.read_csv(str(value2)+'.csv')
        ax.plot(data1['Confirmed'],label=value1)
        ax.plot(data2['Confirmed'],label=value2)
        plt.ylabel('Number of cases')
        plt.xlabel('Days')
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()




def myClick():
    myLabel1=Label(root,text="You clicked the button")
    myLabel1.pack()
#creating a label widget
myLabel=Label(root,text="Covid cases tracker") #created a label
myButton=Button(root,text="Plot the graph",command=graph) 
buttonquit=Button(root,text="Exit",command=root.quit)

#drop down box
clicked=StringVar()
clicked.set("Delhi")
options=[
    'India','Kerala', 'Delhi', 'Telangana', 'Rajasthan', 'Haryana'
 ,'Uttar Pradesh', 'Ladakh', 'Tamil Nadu', 'Jammu and Kashmir', 'Karnataka'
, 'Maharashtra', 'Punjab', 'Andhra Pradesh' ,'Himachal Pradesh', 'Uttarakhand'
, 'Odisha', 'Puducherry' ,'West Bengal', 'Chandigarh' ,'Chhattisgarh', 'Gujarat'
 ,'Madhya Pradesh', 'Bihar', 'Manipur', 'Goa', 'Mizoram',
 'Andaman and Nicobar Islands', 'Assam' ,'Jharkhand', 'Arunachal Pradesh',
 'Nagaland', 'Tripura', 'Dadra and Nagar Haveli and Daman and Diu',
 'Meghalaya', 'Sikkim' ,'Lakshadweep'
]
drop=OptionMenu(root,clicked,*options)

#second drop down box

clicked1=StringVar()
clicked1.set("India")
options1=[
    'India','Kerala', 'Delhi', 'Telangana', 'Rajasthan', 'Haryana'
 ,'Uttar Pradesh', 'Ladakh', 'Tamil Nadu', 'Jammu and Kashmir', 'Karnataka'
, 'Maharashtra', 'Punjab', 'Andhra Pradesh' ,'Himachal Pradesh', 'Uttarakhand'
, 'Odisha', 'Puducherry' ,'West Bengal', 'Chandigarh' ,'Chhattisgarh', 'Gujarat'
 ,'Madhya Pradesh', 'Bihar', 'Manipur', 'Goa', 'Mizoram',
 'Andaman and Nicobar Islands', 'Assam' ,'Jharkhand', 'Arunachal Pradesh',
 'Nagaland', 'Tripura', 'Dadra and Nagar Haveli and Daman and Diu',
 'Meghalaya', 'Sikkim' ,'Lakshadweep'
]
drop1=OptionMenu(root,clicked1,*options1)




# packing it for the screen
myLabel.pack()
drop.pack()
drop1.pack()
myButton.pack()
buttonquit.pack() 

root.mainloop()

#to get the selected value -> clicked.get()