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
# print('--- Book Chapter Summary ---')
# page_count=[45,30,50,40]
# for i in range(1,5):
#     print(f'Chapter {i} has {page_count[i-1]} pages.')

# 5. Write a Python script to calculate the product (multiplication) of all numeric elements in a given list. given list=[4,5,3,2]
# lst = [4, 5, 3, 2]
# product = 1
# for i in lst:
#     product *= i
# print(product)


# 6. multiplication table of a given number. number= 11
# n = 11
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# 7. reverse a list given list = [3,2,1,4,5]
# lst = [3, 2, 1, 4, 5]
# print(lst[::-1])


# 8. You have two lists of numbers, and you need to find out which numbers appear in both lists. Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7] write a for loop to find the common elements.
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# for i in a:
#     if i in b:
#         print(i)


 # 9. Given list is lst=[1,2,3,4] but print 1 and 4 only
# lst = [1, 2, 3, 4]
# for i in lst:
#     if i == 1 or i == 4:
#         print(i)


## 10. Write a that removes all vowels (a, e, i, o, u) from a string.
# s = input()
# vowels = "aeiouAEIOU"
# res = ""
# for ch in s:
#     if ch not in vowels:
#         res += ch
# print(res)


# 11.  Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters. 

# given input: 

# 'Loops are Fun'

# expected Output:

# vowels: 5

# consonants: 7 
# s = "Loops are Fun"
# vowels_set = "aeiouAEIOU"

# vowels = 0
# consonants = 0

# for ch in s:
#     if ch.isalpha():
#         if ch in vowels_set:
#             vowels += 1
#         else:
#             consonants += 1

# print("vowels:", vowels)
# print("consonants:", consonants)



# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
# lst = [1, 2, 3, 4, 5]
# even = []
# odd = []

# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)


# 13. Write a program to determine whether a given number is a prime number.
# n = int(input())

# if n < 2:
#     print(False)
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(False)
#             break
#     else:
#         print(True)


# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
# lst = [1, 2, 3, 4, "a", "b"]
# ints = []
# strings = []

# for i in lst:
#     if isinstance(i, int):
#         ints.append(i)
#     else:
#         strings.append(i)

# print(ints)
# print(strings)


# 15. Python program that accepts a string and calculate the number of digits and letters
# s = input()
# digits = 0
# letters = 0

# for ch in s:
#     if ch.isdigit():
#         digits += 1
#     elif ch.isalpha():
#         letters += 1

# print(digits)
# print(letters)


# 16. Python program to check validity of username and password input by users
# u = input()
# p = input()

# if len(u) >= 5 and len(p) >= 5:
#     print("Valid")
# else:
#     print("Invalid")


# 17. program to print the given number is odd or even
# n = int(input())

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# 18. factorial of a given number
# n = int(input())
# fact = 1

# for i in range(1, n + 1):
#     fact *= i

# print(fact)


# 19. Print multiplication table of 1,2,3,4,5,6,7,8
# for n in range(1, 9):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")
#     print()


# 20. Given list is [1,2,3,4] but print 1 and 2 only
# lst = [1, 2, 3, 4]
# for i in lst:
#     if i in (1, 2):
#         print(i)


# 21. Python program to calculate the sum of all the odd numbers within the given range.
# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         total += i
# print(total)


# 22. Python program to calculate the sum of all the even numbers within the given range.
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)


# 23. Python program to count the space of a given string
# s = input()
# count = 0

# for ch in s:
#     if ch == " ":
#         count += 1

# print(count)


# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]
# lst = [1, 2, 3, 4]
# res = []

# for i in lst:
#     res.append(i ** 3)

# print(res)


# 25. reverse of a string a="programming"
# a = "programming"
# print(a[::-1])


# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
# for i in range(50):
#     if i > 7:
#         break
#     print(i)


# 27. Write a for loop that iterates through a string and prints every letter.
# s = input()

# for ch in s:
#     print(ch)


# 28. Write a for loop which print "Hello!, " plus each name in the list.
# a = ["ram", "shyam", 1, 2]

# for i in a:
#     print("Hello!, " + str(i))


# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst.
# a = ["ram", "shyam", 1, 2]
# res = []

# for i in a:
#     res.append("Dr." + str(i))

# print(res)


# 30. Write a for loop which appends the square of each number to the new list.
# lst = [1, 2, 3, 4]
# res = []

# for i in lst:
#     res.append(i ** 2)

# print(res)


# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive.
# lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
# res = []

# for i in lst1:
#     if i > 0:
#         res.append(i)

# print(res)


# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# lst = [0, 1, 2, 3, 4, 5, 6]

# for i in lst:
#     if i in (3, 6):
#         continue
#     print(i)


# 33. Write a for loop which appends the type of each element in the first list to the second list.
# lst1 = [1, 2, "a", 3.5]
# lst2 = []

# for i in lst1:
#     lst2.append(type(i))

# print(lst2)


# 34. Use else block to display a message “Done” after successful execution of for loop.
# for i in range(5):
#     print(i)
# else:
#     print("Done")


# 35. Write a for loop statement to print the following series: 105 98 ... 7
# for i in range(105, 0, -7):
#     print(i)


# 36. removal bad characters from the given string.
# bad_chars = [';', ':', '!', "*"]
# s = "py;th* o:n ! ;py * t*h:o !n"

# for ch in bad_chars:
#     s = s.replace(ch, "")

# print(s.replace(" ", ""))


# 37. Python program to count the number of even and odd numbers from a series of numbers.
# nums = [1,2,3,4,5,6,7,8,9]
# even = 0
# odd = 0

# for i in nums:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print(even, odd)


# 38. Write a for loop to find the sum of all multiples of 3 or 5 below a given number range from 3 to 99.
# total = 0
# for i in range(3, 100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)


# 39. Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.
# even = 0
# odd = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print(even, odd)

# 40. Given a list of numbers, use a loop to count how many times a specific number appears.

# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count = 0

# for i in list1:
#     if i == target:
#         count += 1

# print(count)