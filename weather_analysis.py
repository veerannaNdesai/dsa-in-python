
arr = []

with open("nyc_weather.csv","r") as f:
    for i in f:
        token = i.split(',')
        try:
            arr.append(int(token[1]))
        except:
            print("Invalid temp. ignore the row")

'''What was the average temperature in first week of Jan'''
average = round(sum(arr[0:7])/len(arr[0:7]),2)
print(average) #31.29

'''What was the maximum temperature in first 10 days of Jan'''
first_10_temp = arr[0:10]
max_temp = max(first_10_temp)
print(max_temp) #38

#The best data structure to use here was a list because all we wanted was access of temperature elements.


'''
(2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the temperature on Jan 9?

  (b) What was the temperature on Jan 4?

  Figure out data structure that is best for this problem

'''

dict = {}

with open("nyc_weather.csv","r") as f:
    for i in f:
        token = i.split(',')
        try:
            dict[token[0]] = int(token[1])
        except:
            print("Invalid temp. Ignore the row")

'''(a) What was the temperature on Jan 9?'''
print(dict['Jan 9']) #35

'''b) (b) What was the temperature on Jan 4?'''
print(dict['Jan 4']) #34

'''
The best data structure to use here was a dictionary (internally a hash table) 
because we wanted to know temperature for specific day, requiring key, value pair access 
where you can look up an element by day using O(1) complexity

'''

'''
3. poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out why you selected that 
specific data structure.

 'diverged': 2,
 'in': 3,
 'I': 8
'''

WordCount = {}

with open("poem.txt","r") as poem:
    for i in poem:
        tokens = i.split(' ')
        for j in tokens:
            j = j.replace('\n','')
            if j not in WordCount.keys():
                WordCount[j] = 1
            else:
                WordCount[j] += 1

for i,j in WordCount.items():
    print(i+":",j,end="\n")