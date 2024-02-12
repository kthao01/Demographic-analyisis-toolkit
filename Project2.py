################## Helper Code Below -- don't delete! ##################


# Helper Code 1
bach_data = []
with open("Bachelors.txt", "r") as f:
    for num in f:
        num = float(num.strip())
        bach_data.append(num)
f.close()


# Helper Code 2
pop_data = []
with open("Population.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        pop_data.append(value)
file.close()



# Helper Code 3
avg_income = []
with open("Income.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        avg_income.append(value)
file.close()



# Helper Code 4
high_school_data = []
with open("HighSchool.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        high_school_data.append(value)
file.close()


# Helper Code 5
poverty_data = []
with open("Poverty.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        poverty_data.append(value)
file.close()

# TASK 1
def Avg(lst):                     # function for finding average
    return sum(lst)/len(lst)


# QUESTION 1.1
def percent_bachelors(bach_data, pop_data):
    avg_lst = []
    for i in range(len(pop_data)):
        avg_lst.append(bach_data[i]*pop_data[i])
    return (sum(avg_lst)/sum(pop_data))
        
print(percent_bachelors(bach_data,pop_data))
'''
This function takes the bachelor's and population data
for each county and returns the percentage of people
with a bachelors or higher across all counties
'''

# QUESTION 1.2


def income_above_50k(avg_income):
    inc = 0
    for i in range(len(avg_income)):
        if avg_income[i] > 50000:
            inc = inc + 1
    return (inc*100/len(pop_data))
print(income_above_50k(avg_income))
'''
This function takes the average income of all counties
and returns the percentage of counties with an income
above $50,000
'''

# ---------------------------------------------------------------------------------------------------- #


# TASK 2
def high_school_below_threshold(high_school_data, threshold):
    num_counties = 0
    for i in range(len(high_school_data)):
        if high_school_data[i] < threshold:
            num_counties = num_counties + 1
    return num_counties
print(high_school_below_threshold(high_school_data,60))
'''
This function takes the high school graduation rate in
each county and searches for the number of counties that
are below a given threshold and returns the value
'''

# ---------------------------------------------------------------------------------------------------- #


# TASK 3
def bachelors_above_threshold(bach_data, threshold):
    num_bach = 0
    for i in range(len(bach_data)):
        if bach_data[i] > threshold:
            num_bach = num_bach + 1
    return num_bach
print(bachelors_above_threshold(bach_data, 60))
'''
This function takes the bachelor graduation percentage
in each county and searches for the number of counties
that have a percentage above a given threshold and 
returns that value
'''


# ---------------------------------------------------------------------------------------------------- #


# TASK 4


def below_poverty_total(poverty_data, pop_data):
    num_pov = []
    for i in range(len(pop_data)):
        num_pov.append(poverty_data[i]/100*pop_data[i])
    return sum(num_pov)
print(below_poverty_total(poverty_data, pop_data))
'''This function takes the poverty data of each county and
returns the total amount of people under the poverty level'''


# ---------------------------------------------------------------------------------------------------- #


# TASK 5
def percent_below_poverty(poverty_data, pop_data):
    return below_poverty_total(poverty_data, pop_data)/sum(pop_data)*100
print(percent_below_poverty(poverty_data, pop_data))
'''This function takes the poverty data and returns the 
national percentage of all the people under the poverty
level'''


# ---------------------------------------------------------------------------------------------------- #


# TASK 6
def education_vs_poverty(bach_data, poverty_data):
    below_10 = []
    below_20 = []
    below_30 = []
    greater_30 = []
    for i in range(len(poverty_data)):
        if bach_data[i] < 10:
            below_10.append(poverty_data[i])
        elif bach_data[i] < 20:
            below_20.append(poverty_data[i])
        elif bach_data[i] < 30:
            below_30.append(poverty_data[i])
        elif bach_data[i] >= 30:
            greater_30.append(poverty_data[i])
    return print(Avg(below_10), Avg(below_20), Avg(below_30), Avg(greater_30))

education_vs_poverty(bach_data, poverty_data)
'''This function takes the percentager of bachelors
graduates and percentage of people below poverty
level for each county and returns the national
average poverty level for each county'''

import matplotlib.pyplot as plt
plt.scatter(bach_data,poverty_data)
plt.xlabel("Bachelor's Graduates (%)")
plt.ylabel("Average Poverty Level (%)")
plt.title("Average Poverty Level vs Education Level in the US")
plt.show()

'''
I noticed that in the counties where the bachelors graduates are the lowest, 
the poverty rates are dramatically higher than the counties where the bachelors 
graduates are higher. Although this is sad, it doesn't surprise me as I grew up 
in areas with high poverty rates. There just isn't enough funding for educational 
resources for children and college students.
'''