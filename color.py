'''
Create a list of the whole colors
'''
import random
colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW',
         'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE',
         'BLUE', 'BLUE', 'GREEN', 'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE',
         'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE',
         'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'YELLOW',
         'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED',
         'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE',
         'WHITE','BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK',
         'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE',
         'BLUE', 'BLUE', 'BLUE', 'GREEN', 'GREEN', 'WHITE', 'GREEN', 'BROWN',
         'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE',
         'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
'''
create an empty dictionary to hold the colors and their frequencies
'''
frequency = {}

for color in  colors:
    if color in frequency:
        frequency[color] += 1
    else:
        # Initializing the frequencies
        frequency[color] = 1

'''
1) Mean Color 
'''
print(frequency)


def totalColorFrequency():
    sum = 0
    for i in frequency.values():
        sum = sum + i
    return sum

# mean = sum/j

mean = round(totalColorFrequency()/len(frequency.values()), 2)

print('1) Mean is 8\n','The BROWN shirt is the mean color as its frequency 9, is closer to the mean,', mean)





'''
2) Color of shirt mostly worn throughout the week
'''

for j in frequency.values():
        for i in frequency.keys():
            if j == 30 and frequency[i] == 30:
                print(
                    '--------------------------------------------------------------------------------------------------')
                print(
                    '--------------------------------------------------------------------------------------------------')
                print('2)',i, 'is the most worn color of shirt')



'''
3) Median color
'''
frequencyList = []

for i in frequency.values():
    frequencyList.append(i)

frequencyList.sort()

median = round((frequencyList[5] + frequencyList[6])/2, 2)
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
print('3)The median color is BROWN as the approximated value is equal to',median)

'''
4) Variance = E(x - mean)^2/n-1; 
'''

sum2 = 0
for i in frequencyList:
    y = i - mean
    z = y ** 2
    sum2 = sum2 + z
variance = round(sum2/(len(frequencyList)-1), 2)
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
print('4) The variance is', variance)


'''
5) Probability of choosing a RED shirt; 
Probability(RED) = frequency of RED shirt/summation of the whole frequencies
'''
probabilityOfRed = frequency['RED']/totalColorFrequency()
probabilityOfRedPercentage = round(probabilityOfRed * 100, 2)
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
print('5) Probability of RED is', probabilityOfRedPercentage, '%')


'''
6) Save the color and their frequencies in postgresql
'''
# import psycopg2
#
#
# con = psycopg2.connect(
#    database="color",
#    user="Emmanuel",
#    password="dictionary1234",
#    host="localhost",
#    port= '5432'
#    )

# curs_obj = con.cursor()
g = []
for i in frequency.keys():
    g.append()
    # curs_obj.execute("INSERT INTO emp_data(emp_name, emp_age) VALUES(str(i), frequency[i]);")
# print("Data Inserted")









'''
7) Recursive Search algorithm
'''

def Recursive_Search_Algorithm(data, lowerBound, higherBound, SearchItem):
    if lowerBound <= higherBound:
        mid = (lowerBound + higherBound) // 2
        if data[mid] == SearchItem:
            return mid
        elif SearchItem < data[mid]:
            return Recursive_Search_Algorithm(data, lowerBound, mid - 1, SearchItem)
        else:
            return Recursive_Search_Algorithm(data, mid + 1, higherBound, SearchItem)
    else:
        return -1

data = [1,5,68,8,6,89,23,76,9,25,65,75]
data.sort()
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
print('7) 89 is present and its index is',Recursive_Search_Algorithm(data, 0, len(data)-1, 89))


'''
8) Generating 4 digit binary number and converting to base 10
'''
a = random.randint(0,1)
b = random.randint(0,1)
c = random.randint(0,1)
d = random.randint(0,1)
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
baseTenNumber = ((a*(2**3))+(b*(2**2))+ (c*(2**1)) + d)
print('8)', a, b, c, d, 'in base 10 is', baseTenNumber)


'''
9) First 50 fibonacci sequence
'''
fibonacci_sequence = []
for i in range(0,50):
    if i == 0:
        y = 0 + 1
        fibonacci_sequence.append(y)
    elif i == 1:
        y = fibonacci_sequence[i-1] + 1
        fibonacci_sequence.append(y)
    else:
        y = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(y)
print ('--------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------------------------------------------------------')
print('9) The first 50 Fibonacci sequence is:', fibonacci_sequence)

