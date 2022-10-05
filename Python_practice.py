

print('helo wordl')

counties = ["Arapahoe","Denver","Jefferson"]

print(counties[0])

print(counties[0:2])

counties.append("El Paso")
print(counties)

counties.insert(2, "El Paso")
print(counties)


counties.remove("El Paso")
print(counties)

counties.pop(3)

#DICTIONARIES

counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

items=counties_dict.items()
print(items)

keys=counties_dict.keys()
print(keys)

values=counties_dict.values()
print(values)

get=counties_dict.get('Denver')
print(get)


#LIST OF DICTIONARIES
voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

#IF STAT:

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    
#IF ELSE STATEMENTS:

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")
    
# score = int(input("What is your test score? "))

# # Determine the grade.

# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# #logical operators


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
    
#while

x = 0
while x <= 5:
    print(x)
    x = x + 1
    

#FOR LOOPS

for county in counties:
    print(county)
    

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)
    
for i in range(len(counties)):
    print(counties[i])
    
#ITERATE THROUGH DICT:

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:  #-----> get keys and values
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():   #----->get th value of the key
    print(voters)
    
    
    
for county in counties_dict:
    print(counties_dict[county]) #----> GET THE VALUE OF THE KEY

      # OR
      
for county in counties_dict:
    print(counties_dict.get(county))  #get the value of the key
    
#GET THE KEY-VALUE PAIRS OF A DICT:

for key, value in counties_dict.items():
    print(key,value)
    
#ITERATE THROUGH A LIST OF DICTIONARIES:

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

    
for county_dict in voting_data:
    print(county_dict)
    

#GET THE VALUES FROM A LIST OF DICT

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
        
#if we just want to print the name:-->>>
for county_dict in voting_data:
    print(county_dict['county'])
    

#f strings:

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    
#or FSTRINGS: (EASILY)


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    
    
