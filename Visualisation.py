#----------------------------------------------------------------------------Visualisation.py----------------------------------------------------------------------------#
'''
Importing modules:
-pandas,as pd
-plotly.express,as ps
'''
import pandas as pd 
import plotly.express as ps 
#Formmal introduction and requesting input
print("Welcome to COVID-19.py.")
print("We provide the option of visualising Covid-19 Data in different types of data visualisation.")
data_type_visualisation=input("Please choose the chart/graph type you want to view the data in:(Enter:-Bar,Scatter,Pie)")

#Function to display desired data
def DisplayData():
    print("Generating data...")
  #Cases modelled according to the input provided
    #Case-1  
    if(data_type_visualisation=="Bar"):
      df=pd.read_csv("COVID-19.csv")
      bar_graph=ps.bar(df,x="Date",y="Cases",color="Country",title="COVID-19 Data(Bar Graph)")
      bar_graph.show()
      print("Graph rendered.")
      print("Thank you for using Visualisation.py")
    #Case-2 
    elif(data_type_visualisation=="Scatter"):
      df=pd.read_csv("COVID-19.csv")
      scatter_graph=ps.scatter(df,x="Date",y="Cases",color="Country",title="COVID-19 Data(Scatter Graph)",size="Cases")
      scatter_graph.show()
      print("Graph rendered.")
      print("Thank you for using Visualisation.py")
    #Case-3  
    elif(data_type_visualisation=="Pie"):
      df=pd.read_csv("COVID-19.csv")
      pie_chart=ps.pie(df,values="Cases",names="Country",color="Country",title="COVID-19 Data(Pie Chart)")
      pie_chart.show()  
      print("Chart rendered.")
      print("Thank you for using Visualisation.py")
   #Case-4  
    else:
      print("Request terminated.")
      print("Please enter a valid input(according to provided circumstances).")
      print("Thank you for using Visualisation.py")
  


def Main():
  DisplayData()   
Main()
#----------------------------------------------------------------------------Visualisation.py----------------------------------------------------------------------------#

    

   
  
