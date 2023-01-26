user_age = input("Please enter your age: ")
age_number = int(user_age)
age_in_months = age_number * 12
print(f"You are {age_in_months} months old!")

# this is another way of writing the code & eliminates line 2 above
user_age = int(input("Please enter your age: "))
age_in_months = user_age * 12
print(f"You are {user_age} years old which is also equal to {age_in_months} months old!")