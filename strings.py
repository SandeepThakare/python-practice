a= "hello" #assign string to a

print("value of a is ", a) #print string

print("Length of string a = ", len(a)) #returns the length of string

print('\nCan also get string variable using indexes')

for x in a:
    print("X values is = ", x)

print('\ncan also get by indexing')

print('Strint charecter at 0th index is - a[0] is ', a[0])

print('\nwe can also use : for slicing to get char upto mark')

print('print all from index 1 from string ==> ', a[1:])

print('print everything upto 3rd index from string ==> ', a[:3])

print('\nWe can also use negative indexing - work as index-1 in this')

print('Print string except last one a[:-1] ==> ', a[:-1])

print('Print string by negative indexing ==> ', a[-3:-1])



