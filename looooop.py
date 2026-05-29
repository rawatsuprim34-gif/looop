# 1. Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.

# Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."

# Output

# Number 1 is odd.

# Number 2 is even.

# Number 3 is odd.

# Number 4 is even.

# Number 5 is odd.



# for i in range(1, 6):
#     if i % 2 == 0:
#         print(f"Number {i} is even.")
#     else:
#         print(f"Number {i} is odd.")


# 2. Write a Python script that uses a for loop to calculate the sum of all elements in the given list.

# list = [10,20,30,40]

# Your script must:

# Initialize a variable to keep track of the running total.

# Iterate through the data list using a for loop.

# Inside the loop, print the value currently being added and the new running total.

# Finally, print the total sum after the loop finishes.

# Added 10. Running total is 10.

# Added 20. Running total is 30.

# Added 30. Running total is 60.

# Added 40. Running total is 100.

# New_total=0
# Lst=[10,20,30,40]
# for i in Lst:
#     New_total+=i
#     print(f'Added {i}. Running total is {New_total}')
# print('____________')
# print(f'Total Sum{New_total}')




# 3. Write a program that uses a for loop to iterate through the list student_names = ["Ram", "Hari", "Sita"] and
#  prints a personalized message for each student in the format 'Hi [Name], your course approval is ready!'.
#  Include the header ' --- Email Greetings Generated ---' before the loop.

# student_names=["Ram","Hari","Sita"]
# print('Email Greetings Generated'.center(32,"-"))
# for i in student_names:
#     print(f"'Hi {i}, your course approval is ready!'")

# 4. write a program that iterates through the list of chapter page counts [45, 30, 50, 40] and (starting the count at 1) 
# to print a message for each chapter in the format: 'Chapter [Number] has [Pages] pages.'
#     . Include the header '--- Book Chapter Summary ---'."
print('--- Book Chapter Summary ---')
page_count=[45,30,50,40]
for i in range(1,5):
    print(f'Chapter {i} has {page_count[i-1]} pages.')
   