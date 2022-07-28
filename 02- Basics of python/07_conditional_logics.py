# logical operator are either true or false, yes or no, 0 or 1
# equal to                   ==
# less than                   <
# greater than                >
# less than and equal to      <=
# greater than and equal to   >=

# is 4 equal to 4?
print(4==4)
print(4!=4)
print(4 > 3)
print(3 < 6)
print(3 <= 5)
print(5 >= 4)

# application of logical operator
hammad_age = 4
age_at_school = 5
print(hammad_age == age_at_school)

# input funciton and logical operator
age_at_school = 5
hammad_age = input("How old is hammad? ")
hammad_age = int(hammad_age)
print(type(hammad_age))
print(hammad_age == age_at_school)
