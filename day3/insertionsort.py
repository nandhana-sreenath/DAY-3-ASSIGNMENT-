def insertionSort(a):
  
    # Traverse through 1 to len(a)
    for i in range(1, len(a)):
  
        j=i
        while (j!=0 and a[j]<a[j-1]) :
            a[j],a[j-1]=a[j-1],a[j]
            j=j-1
        
# Driver code to test above
a= [12, 11, 13, 5, 6]
print("List before sorting:",a)
insertionSort(a)
print ("Sorted array is:",a)

