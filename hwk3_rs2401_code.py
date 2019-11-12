#import time, random, and math modules
from time import time
from random import randint
from math import log2
#define a function insertion sort
def insertion_sort(unsorted_list):
    #create an empty sorted list
    sorted_list=[]
    #add valueues to the sorted list
    sorted_list.append(unsorted_list[0])

    n=len(unsorted_list)
    #check each valueues of unsorted list with sorted list and add the valueues to the sorted list.
    
    for i in range(1,n):
        value= unsorted_list[i]
        
        for j in range(len(sorted_list)):
            number=sorted_list[j]
            #check if valueue is less than than the number in the sorted list and insert the valueue to the list
            
            if value<number:
                sorted_list.insert(j,value)
               
               
                break
            #check if the valueue is greater than the valueues of the sorted list
            elif value>= sorted_list[len(sorted_list)-1]:
            
                sorted_list.append(value)
              
                break
    return sorted_list

#create an empty list 
mylist=[]
#create an empty list of list sizes
listSize=[256, 1024, 4096, 16384, 65536, 262144]
#create the list of serial already sorted list of integers from 0 to listSize specified
for Size in listSize:
    for w in range(Size):
       mylist.append(w)
    z= len(mylist)
    #start timing
    start_time= time()
    #time for larger repetition and call the insertion sort function
    for r in range(10000):
        listsort = insertion_sort(mylist)
    #end timing
    end_time = time()
    time_all_reps = end_time - start_time
    #get the single timing 
    timeonce = time_all_reps / 10000
    C = timeonce/ (z*z)
# print the results
    print("list length Size: ",z)
    print("single sorting time: ", format(timeonce, " .3g"))
    print("value of C: ", format(C, ".3g"))




