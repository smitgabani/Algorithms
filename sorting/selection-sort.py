def selsort(myarray,r):
    for x in range(r):
        minimum = x 
        for y in range(x + 1, r):
            if myarray[y] < myarray[minimum]:
                minimum = y
        (myarray[x], myarray[minimum]) = (myarray[minimum],myarray[x])

mylist = input('Enter the list values to be stored: ').split()
r = len(mylist)
selsort(mylist, r)
print(mylist)