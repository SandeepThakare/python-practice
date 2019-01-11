a= "hello world" #assign string to a

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

print('\n-----String Properties-----')

print('print string 2 times - a*2 ==> ', a*2)

print('split words from given string - a.split() ==> ', a.split())

print("#Split by a specific element (doesn't include the element that was split on)")

print("Split word by latter 'W' - a.split('w')", a.split('w'))

print('\n-----String Formatting-----')

print("I'm going to inject %s here." %'something')

print('\n .format() method')

print('Add something inside curly braces, {}'.format('your name please'))

print('Add something by indexing {1} {2} {0}'.format('Hi', 'Hello', 'Bonzor'))

print("can insert by assigning keyword First: {a}, Second: {b}, Third: {c} .format(a=1,b='Two',c=12.3)")

print('can insert by assigning keyword First: {a}, Second: {b}, Third: {c}'.format(a=1, b='abc', c=1.25))

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

