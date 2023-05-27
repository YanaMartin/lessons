
mystring="32.054,23"

def comma_dot(mystring):
    """swap comma and dot in a string"""
    mystring=mystring.replace(",", "$$")
    mystring=mystring.replace(".", ",")
    mystring=mystring.replace("$$", ".")
        
    return mystring

#print(comma_dot(mystring))


l=['p', 'q']
n=8

def new_list(l):
    """return a list by concatenating elements of a given list
#and elements of range from 1 to n"""
    mylist=[]
    for number in range (1, n+1):
        for element in l:
            new=('{}{}'.format(element,number))
            mylist.append(new)
            
    return mylist

#print(new_list(l))

mydict={'b':1, 'a':2, 'c':3}
number=2

def multi_dict(d):
    for key, value in d.items():
        d.update({key: value*number})

    return d

#print(multi_dict(mydict))


mydict={'b':1, 'a':2, 'c':3}
#print(mydict.items())


def sorted(d):
    Keys = list(d.keys())
    Keys.sort()
    new_dict = {key: d[key] for key in Keys}
    print(new_dict)

#print(sorted(mydict))

#Write a program to replace the last value of tuples in a list.
mylist= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in mylist])
#for t in mylist:
#    print(t[:-1] + (444,))






        


