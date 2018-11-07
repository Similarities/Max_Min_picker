# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:30:25 2017

@author: similarities
"""

import numpy as np
import Tkinter, tkFileDialog
import ntpath
import matplotlib.pyplot as plt


root = Tkinter.Tk()

root.withdraw()

ntpath.basename("a/b/c")

file_path = tkFileDialog.askopenfilename()
#open(file_path)


def path_leaf(path):
    
    head, tail = ntpath.split(path)
    
    return tail or ntpath.basename(head)
    
print(path_leaf(file_path))



class Max_Min:

    def __init__(self, file_path):
        
        self.file_path = file_path
        
        self.array_min = np.empty([1, 2])
        
        self.array_max = np.empty([1, 2])
        
        self.raw_data = np.array

        
        
        
    
    
    def loadarray(self):
    
        #reads coloumn1 from txt / skips first rows (3), 
        liste1 = np.loadtxt(self.file_path, skiprows = (3), usecols = (0,))
    
        #reads coloumn2 from txt / skips first rows (3), 
        liste = np.loadtxt(self.file_path, skiprows = (3), usecols = (1,))
    
        #converts loaded coloumn1 to an numpy array:
        matrix1 = np.array((liste1))
    
        #converts loaded coloumn2 to an numpy array:
        aa = np.array((liste))
    
        #joins the arrays into a 2xN array 
        self.raw_data = np.column_stack((matrix1, aa))
    
        self.raw_data.view('i8,i8').sort(order = ['f0'], axis = 0)    
       
       #print submatrix1
        plot_xy(self.raw_data, "b", "rawdata")
    
        return self.raw_data
    
    

    
    
    def peak_detect(self):
    
        i = 1
    
        N = len(self.raw_data)
    
        #peak_min = np.empty([1, 2])
    
        peak = np.empty([1, 2])
    
        #peak_max = np.empty([1, 2])
    
        while i < N-1:
        
            delta_1 = self.raw_data[i+1, 1]-self.raw_data[i, 1]
        
            delta_2 = self.raw_data[i-1, 1]-self.raw_data[i, 1]
        
            
            if delta_1 < 0 and delta_2 > 0:
            
                None
            
            
            elif delta_1 > 0 and delta_2 < 0:
            
                None
            
            
            elif delta_1 < 0 and delta_2 < 0:
            
            #make new array and mark points
            
                peak[0, 0] = self.raw_data[i, 0]
            
                peak[0, 1] = self.raw_data[i, 1]
            
                self.array_min= np.concatenate((peak,self.array_min))
            
            
            
            elif delta_1 > 0 and delta_2 > 0:
            
            #make new array and mark points
            
                peak[0, 0] = self.raw_data[i, 0]
            
                peak[0, 1] = self.raw_data[i, 1]
            
                self.array_max = np.concatenate((peak, self.array_max))
            
            

            else:
            
                print "equal?", delta_1, delta_2
            
            i=i+1
            
        # info: 
            
        print "number of raw data points:", len(self.raw_data)
        
        print "number of maxima:", len(self.array_max)
    
        print "number of minima:", len(self.array_min)
        
    
        plot_xy(self.array_max, "r", "max" )
    
        plot_xy(self.array_min, "y", "min")
    
        print_to_file(self.array_min, "picked_Minimum")
    
        print_to_file(self.array_max, "picked_Maximum")
    
        return self.array_max, self.array_min
        
                                
    

# global functions: 

def plot_xy(array, color, name):
    
    x = array[:,0]
    
    y = array[:,1]
    
    plot=plt.scatter(x, y, color = color,label = name)
    
    plt.legend(handles = [plot])
    
    plt.ylabel(name)
    
    plt.show()
    
    
    
    
def print_to_file(array,name):
    
    print "now to file"
    
    np.savetxt("test" + "_" + name + ".txt", array[:], fmt = '%.3E', delimiter = '\t')
    
    return array
        
        
my_filter = Max_Min(file_path)
my_filter.loadarray()
# including the plot and print call here -- might be done in a nicer way outside
my_filter.peak_detect()



            
        
