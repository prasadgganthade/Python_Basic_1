print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky\nTwinkle twinkle litter star')
# 2. chek python version
import sys
print(sys.version)
# 3. Python Programme to display current date and time
import datetime
now  = datetime.datetime.now()
print("Current date and time is : ")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
#4. Python program which accepts the radius of a circle from the user and compute the area
"""
from math import pi
radius = float(input('Enter the radius of circle : '))
area = pi * radius * radius
print('Area of circle is',area)
"""
# 5. Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
fname = input('Enter first name : ')
lname = input('Enter last name : ')
name = lname +' '+ fname
print('Reversed name',name)
"""

# 6. Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""values = input('Enter comma seperated values : ')
list = values.split(',')
tuple = tuple(list)
print('List is',list)
print('Tuple is',tuple)
"""
# 8 Python program to display the first and last colors from the following list.
color_list = ['Red','Green','White','Black']
print(color_list[0::3])

#9 Python program to display the examination schedule.
exam_date = (11,12,2022)
print('Examination will start from : %i / %i / %i'%exam_date)
# 10 Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""n = int(input('Enter the value : '))
n1 = int('%s'%n)
n2 = int('%s%s'%(n,n))
n3 = int('%s%s%s'%(n,n,n))
result = n1+n2+n3
print('The result is',result)
"""
#12. Python program to print the calendar of a given month and year.
"""import calendar
y = int(input('Input the year : '))
m = int(input('Input the month : '))
print(calendar.month(y,m))
"""
# 14 Python program to calculate number of days between two dates.
from datetime import date
f_date = date(2022, 7, 2)
l_date = date(2022, 7, 11)
delta = l_date - f_date
print(delta.days)

# 15 Python program to get the volume of a sphere with radius 6.
from math import pi
r = 6
volume = 4/3 * pi * r**3
print('Volume of sphere',volume)

#16 Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""num = int(input('Enter the number : '))
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')"""

# 17 Python program to count the number 4 in a given list.

def list_count_4(num):
    count = 0
    for i in num:
        if i == 4:
            count = count + 1
    return count
print(list_count_4([1,4,6,7,4]))
print(list_count_4([1,4,6,4,7,4]))

# 18 Python program to test whether a passed letter is a vowel or not.
"""l = input('Enter a letter : ')
if l == 'a' or l == 'A' or l == 'e' or l=='E' or l =='i' or l=='I' or l =='o' or l == 'O' or l=='u' or l=='U':
    print('The letter is Vowel')
else:
    print('The letter is not VOWEL')"""

# 19 Print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for i in numbers:
    if i == 237:
        print(i)
        break;
    elif i % 2 == 0:
        print(i)

#20 Print out a set containing all the colors from a list which are not present in other list
color_list_1 = set(['white', 'black','red'])
color_list_2 =set(['red','green'])
print('Different color of list and list2',color_list_1.difference(color_list_2))
print('Difference colorlist2 and list',color_list_2.difference(color_list_1))

# 21 Python program that will accept the base and height of a triangle and compute the area.
"""base = float(input('Enter the base of triangle : '))
height = float(input('Enter the height of triangle : '))
area = 0.5* base * height
print('The area of triangle is',area)"""

# 22 Greatest common divisor (GCD) of two positive integers
def gcd(x,y):
    gcd = 1
    if x% y == 0:
        return y
    for i in range(int(y/2),0,-1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd
print(gcd(12,17))
print(gcd(4,6))
print(gcd(336,360))

# 23 Python program to get the least common multiple (LCM) of two positive integers.
from functools import reduce
from math import gcd

def lcm(numbers):
    return reduce((lambda x, y: int(x * y /gcd(x,y))),numbers)

print(lcm([12,7]))
print(lcm([1,3,4,5]))
print(lcm([4,6]))
print(lcm([15,17]))

