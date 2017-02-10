'''
**************************
Partners: Justin Ngo & Kayla Kim
Assignment: 3.2.7 Data Project
Subject: Following the prompt of our clients, we gather data to create a graph
    and solve the essential question
Extra: Used PLTW assignment 3.1.5 code to assist with creating the 
    histograph
**************************
'''

import matplotlib.pyplot as plt
import os.path

def scatter_plot():
    # Get the directory name for data files
    directory = os.path.dirname(os.path.abspath(__file__))
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, 'countries_gdp_cancer.csv')
    datafile = open(filename,'r')
    data = datafile.readlines()
    
    print ("Countries:GDP per Capita:Cancer Mortality Rate")
    for line in data[1:]:
        # Gives values to variables
        label,cancer,gdp = line.split(',')
        plt.plot([gdp],[cancer],'ro')

        print (label,gdp,cancer)
    
    # Plots the plot graph with labels
    plt.axis([0, 60000, 0, 400])
    plt.title('GDP Per Capita compared to Cancer Mortality Rate')
    plt.xlabel('GDP Per Capita')
    plt.ylabel('Cancer Mortality Rate (ASR)')
    plt.show()

# Main
scatter_plot()