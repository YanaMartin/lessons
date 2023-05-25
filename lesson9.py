
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

#Write a function to create a sorted dictionary by key from the original
#dictionary. https://github.com/YanaMartin/pyladies_poam.git


def sorted(d):
    new_d=d.sorted
    return new_d

#print(sorted(mydict))




        


