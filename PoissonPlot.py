#! /usr/bin/env python

#Creates Plot of Data

#import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function
if __name__ == "__main__":
   
    #initialize
    haveInput = False
    lamb = 1.0
    Nmeas = 1 #Will redefine later. 
    Nexp = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    data = [] # will turn 2D array into 1D array of all measurements. len = Nmeas * Nexp
    data_0 = [] #array of lists. Each list is a single experiment. [[exp1], [exp2], ....]
    
    #system inputs
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   -lambda [float number]  Parameter of the Poisson Distribution")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    if '-lambda' in sys.argv:
        p = sys.argv.index('-lambda')
        ptemp = float(sys.argv[p+1])
        lamb = ptemp
 
    #Count Nmeas and Nexp. Generate Data lists.
    with open(InputFile) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #Each experiment.
            Nmeas = len(lineVals) #Each experiment has Nmeas measurements.
            
            data_exp = [] #Data for each individual experiment. Gets reset every time.
            
            for v in lineVals: 
               val = float(v) #each measurement in an experiment.
               data.append(val) #each measurement in the 2D array gets fed into a 1D array.
               data_exp.append(val) #each measurement gets fed into a temporary 1D array. 
            
            data_0.append(data_exp) #feed in list of a single experiment into this list
            Nexp += 1 

    #Calculate total amount of measurements throughout all experiments
    Ntot = Nmeas * Nexp
    
    #Print Results
    print(f"Number of measurements/experiment: {Nmeas}")
    print(f"Number of experiments: {Nexp}")
    #print(data) #all measurements
    #print(data_0[0]) #Experiment 1
    
    #Histogram of Data
    data = np.asarray(data)
    
    n, bins, patches = plt.hist(data, 16, edgecolor = 'black', linewidth = 3, density = True, facecolor = 'orange', alpha=0.75)
    
    #Plot actual curve   
    x = np.linspace(0, 20, 1000)
    y = []	
     
    def LogPoisson(x): #Log of Poisson Distribution + Stirling Approximation
        if x == 0:
            f = -1 * lamb
        
        else: 
            f = x * (np.log(lamb) + 1) - x * np.log(x) - lamb  
        
        return f 
        
    for i in range(len(x)):
        y.append(np.exp(LogPoisson(x[i])))
    
    plt.plot(x, y, color = 'blue', label = 'Poisson Distribution') #correct shape, not normalized??
    #plt.plot(x, np.log(y), color = 'red', label = 'Log of Poisson Distribution') 
    
    
    #Plot Formatting
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('P(x | $\lambda$)', fontsize = 15)
    plt.title('Poisson Distribution', fontsize = 20)
    plt.legend(loc = 'upper right')
    plt.grid(True)
    
    plt.savefig('PoissonData.png')
    plt.show()

