#import packages
import math
import numpy as np
import matplotlib.pyplot as plt
import sys

#import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function for our Gaussian code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -seed [integer number]  seed")
        print ("   -Nmeas [integer number]  number of measurements per experiments")
        print ("   -Nexp [integer number]  number of experiments")
        print ("   -lambda [float number]  Parameter for the Poisson Distribution")
        print ("   -output [float number]  name of output file")
        print
        sys.exit(1)
        
    #Initialize 
    seed = 5555
    Nmeas = 1
    Nexp = 1
    lamb = 1.0
    
    #System Inputs
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
        
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        ptemp = int(sys.argv[p+1])
        Nmeas = ptemp

    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        ptemp = int(sys.argv[p+1])
        Nexp = ptemp
        
    if '-lambda' in sys.argv:
        p = sys.argv.index('-lambda')
        ptemp = float(sys.argv[p+1])
        lamb = ptemp
        
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True
               
    #class instance of our Random class using seed
    random = rng.Random(seed)

    #Output data from Gaussian Distribution
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0, Nexp):
            for m in range(0, Nmeas):
                mylist = random.Poisson(lamb)
                outfile.write(str(mylist[0]) + ' ')
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0, Nexp):
            for m in range(0, Nmeas):
                print(random.Poisson(lamb), end=' ')
            print(" ")
           
    
