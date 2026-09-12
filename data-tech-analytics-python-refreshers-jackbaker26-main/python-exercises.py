#!/usr/bin/env python
# coding: utf-8

# # Python Exercises
# 
# If you're already here, chances are you can ignore this statement: Please make sure you follow the installation and setup guides on the assignment `README.md` file.
# 
# **Objectives**
# - Refresher on Python and some common libraries such as `numpy`.
# - Refresher on Jupyter Notebooks.
# - Introduction/Re-introduction to using git and GitHub.
# 
# 
# **Emojis Legend**
# - 👨🏻‍💻 - Instructions; Tells you about something specific you need to do.
# - 🦉 - Tips; Will tell you about some hints, tips and best practices
# - 📜 - Documentations; provides links to documentations
# - 🚩 - Checkpoint; marks a good spot for you to commit your code to git
# - 🕵️ - Tester; Don't modify code blocks starting with this emoji

# In[ ]:


# 🦉 Usually, the first cell in a notebook, is where'd import all modules and third-party modules.
# 🦉 Your Virtual Env need to have the request third party modules installed using a tool like, pip, or poetry, before you can import them.

# 👨🏻‍💻 Use this Code block to import the modules you will need.
import math


# ## Part 1: Python Basics

# ### Exercise - Demo
# Write a python function that takes 2 numbers `num1` and `num2` and returns the addition.

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def simple_add(num1, num2):
    return 0


# In[ ]:


# 🕵️ This code block checks your answer.
try:  
  assert simple_add(10,29) == 39, "❌ Expected 10+29=39"
except AssertionError as e:
  print(e)
print("✅ worked correctly")


# ### Exercise
# Write a python function that takes a number `num` as a function argument and returns `even` or `odd`.

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def is_even_or_odd(num):
    return "even or odd"


# In[ ]:


# 🕵️ This code block checks your answer. 
try:
  even_numbers = (2,4,6,8,10)
  odd_numbers = (1,3,5,7,9)
  for num in even_numbers:
    assert is_even_or_odd(num) == "even", "❌ Expected {} to be labelled even".format(num)
  for num in odd_numbers:
    assert is_even_or_odd(num) == "odd", "❌ Expected {} to be labelled odd".format(num)
except AssertionError as e:
  print(e)
else:
  print("✅ worked correctly")


# > 🚩 : To get into the habit of making frequent commits to git. Make a commit here

# ### Exercise
# write a python function that, given a year,:
# - returns the boolean value `True` if the year is a leap year
# - returns the boolean value `False` if it's not a leap year
# 
# Here's the criteria for a leap year:
# - If a year is evenly divisible by 4 means having no remainder, then go to the next step. If it is not divisible by 4, it is a common year.
# - If a year is divisible by 4 but not by 100, then it is a leap year. If a year is divisible by both 4 and 100, go to the next step.
# - If a year is divisible by 100 but not by 400, then it is a common year. If a year is divisible by both, then it is a leap year.

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def is_leap_year(year):
  return False


# In[ ]:


# 🕵️ This code block checks your answer. 
try:
  leap_years = (2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048)
  not_leap_years = (2005, 2009, 2013, 2017, 2021, 2025, 2029, 2033, 2037, 2041, 2045, 2049)
  for year in leap_years:
    assert is_leap_year(year) == True, "❌ Expected {} to be a leap year".format(year)
  for year in not_leap_years:
    assert is_leap_year(year) == False, "❌ Expected {} to be a not leap year".format(year)
except AssertionError as e:
  print(e)
else:
  print("✅ worked correctly")


# > 🚩 : Make a git commit here

# ### Exercise
# write a python function to convert the temperature from Celsius to Fahrenheit
# $$ F^{\circ}=C^{\circ}\times\frac{9}{5}+32 $$

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def convert_celsius_to_fahrenheit(celsius):
  return 0


# In[ ]:


# 🕵️ This code block checks your answer.
try:
  assert convert_celsius_to_fahrenheit(0) == 32, "❌ Expected 0ºC to be 32ºF"
  assert convert_celsius_to_fahrenheit(10) == 50, "❌ Expected 10ºC to be 50ºF"
  assert convert_celsius_to_fahrenheit(25) == 77, "❌ Expected 25ºC to be 72ºF"
except AssertionError as e:
  print(e)
else:
  print("✅ worked correctly")


# > 🚩 : Make a git commit here

# ### Exercise
# Write a python function that takes a `radius` as a function parameter, and returns `circumference` and `area` of a circle in that order and in the same return
# $$ Area = \pi \times radius^{2}  $$
# $$ Circumference = 2 \pi \times radius $$
# 
# - **🦉: Use the `math` package to get the true value of PI `math.pi`**
# - **🦉: check out the [following on the course website](//it4063c.github.io/course-notes/refreshers/python#returning-multiple-values-in-the-same-function) for an example**
# - **🦉: You'll need to return `area` and `circumference` in that order**

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def get_area_and_circumference_of_circle(radius):
  return 0, 0


# In[ ]:


# 🕵️ This code block checks your answer.
try:
  area2, circum2 = get_area_and_circumference_of_circle(1)
  assert (
    math.isclose(area2, 3.14, abs_tol=0.01) == True
  ), "❌ Expected area of circle of radius 1 to be 3.14 not {}".format(area2)
  assert (
    math.isclose(circum2, 6.28, abs_tol=0.01) == True
  ), "❌ Expected circumference of circle of radius 1 to be 6.28 not {}".format(
    circum2
  )

  area3, circum3 = get_area_and_circumference_of_circle(3)
  assert (
    math.isclose(area3, 28.27, abs_tol=0.01) == True
  ), "❌ Expected area of circle of radius 3 to be 28.27 not {}".format(area3)
  assert (
    math.isclose(circum3, 18.84, abs_tol=0.01) == True
  ), "❌ Expected circumference of circle of radius 3 to be 18.8 not {}".format(
    circum3
  )

except AssertionError as e:
  print(e)


# > 🚩 : Make a git commit here

# ### Exercise
# Write a function that take `n` as an argument, and RETURNS (not prints) an array of the numbers from 1 to n (where n is a function parameter). 
# - But for multiples of three (3) print “Fizz” instead of the number 
# - and for the multiples of five (5) print “Buzz”. 
# - and for numbers which are multiples of both three(3) and five(5) print “FizzBuzz”.
# 
# 🦉 For a reminder on how to loop over a range of numbers. Checkout the [course website's refresher on python](//it4063c.github.io/course-notes/refreshers/python#for-loops)

# In[ ]:


# 👨🏻‍💻 Fix the code below so it returns the correct output.
def fizz_buzz(n):
    result = []
    
    return result


# In[ ]:


# 🕵️ This code block checks your answer.
try:
    assert fizz_buzz(25) == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
        16,
        17,
        "Fizz",
        19,
        "Buzz",
        "Fizz",
        22,
        23,
        "Fizz",
    ]

except AssertionError as e:
    print(e)
else: 
    print("✅ worked correctly")



# > 🚩 : Make a git commit here

# ## Part 2: Numpy
# 🛑 Before you get started in this part, you need to make sure the library is imported 
# 
# (go back to the first cell and import `numpy` with `nb` as an alias)

# ### Exercise
# In one line and (one line only), create a numpy array that contains a range of evenly spaced intervals. Starting with number 3, ending with the number 15, with an intervals of 3
# > Output should look like `array([ 3,  6,  9, 12])`
# 
# 📜 [Here's a link to the `numpy.arange` function](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange)

# In[ ]:


np.


# > 🚩 : Make a git commit here

# ### Exercise
# Given an array `some_array` of a certain shape, create another array of the same shape(size), where instead of the current value in the array, the string `IT4063C` would be there instead. For example For the array([1,2,3]), you would get an output of `array(['IT4063C' 'IT4063C' 'IT4063C'])`
# 
# 🦉 This can be solved by either using numpy.copy and numpy.fill together OR using numpy.full_like.
# 
# **Docs**
# - 📜 numpy.copy function
# - 📜 numpy.fill function
# - 📜 numpy.full_like function

# In[ ]:


input_array = np.array([1,2,3,4,5])
result = 

print(input_array.shape)
print(result.shape)
print(result)


# In[ ]:


# 🕵️ This code block checks your answer.
# Test 1: Check if shapes are equal
try:
  assert input_array.shape == result.shape, "❌ Expected input_array.shape to be {} but got {}".format(input_array.shape, result.shape)
except AssertionError as e:
    print(e)
else: 
  print("✅ Shapes are equal!")

# Test 2: Check if each element in 'result' is 'IT4063C'
try:
  assert all(item == 'IT4063C' for item in result), "❌ Not all elements in 'result' are 'IT4063C'"
except AssertionError as e:
    print(e)
else: 
  print("✅ All elements in 'result' are 'IT4063C'!")


# > 🚩 : Make a git commit here

# ### Exercise
# To practice simple data transformation, work to concatenate 2 numpy arrays of strings. The arrays are of first names, and last names. The end results should be a single array concatenating the names into full names.
# 
# 🦉 I can't give you the answer directly. However, consider the following thought process.
# - What are the numpy functions that you can use?
#   - Check out the [Numpy Routines Documentation](https://numpy.org/doc/stable/reference/routines.html)
# - What's the difference between `numpy.concatenate` and `numpy.char.add`. and which one makes more sense to be used here?
# - you may find that a simple concatenation would look like this: array(['BobSmith' 'JaneJones' 'MalloryWilliams'])
# - Combine the previous exercises with this one, to make an array of empty spaces to be combined
# Also here are the documentation links to some `numpy` functions that, if pieced together, would solve the exercise.
# 
# - 📜 [`numpy.concatenate` function](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)
# - 📜 [`numpy.char.add` function](https://numpy.org/doc/stable/reference/generated/numpy.char.add.html)
# 

# In[ ]:


def get_full_names(first_names, last_names):
  return

sample_first_names = np.array(["Bob", "Jane", "Mallory"])
sample_last_names = np.array(["Smith", "Jones", "Williams"])
full_names = get_full_names(sample_first_names, sample_last_names);
print(full_names)


# > 🚩 : Make a git commit here

# In[ ]:


# 🕵️ This code block checks your answer.
# Test 1: Basic functionality
try:
    sample_first_names = np.array(["Bob", "Jane", "Mallory"])
    sample_last_names = np.array(["Smith", "Jones", "Williams"])
    expected_output = np.array(["Bob Smith", "Jane Jones", "Mallory Williams"])
    output = get_full_names(sample_first_names, sample_last_names)

    assert np.array_equal(output, expected_output), f"Expected {expected_output}, but got {output}"
    
except AssertionError as e:
    print(f"Test 1 Failed: {e}")
else:
    print("Test 1 Passed!")

# Test 2: Empty strings or arrays
try:
    empty_first_names = np.array(["", "Jane", ""])
    empty_last_names = np.array(["Smith", "", "Williams"])
    expected_empty_output = np.array([" Smith", "Jane ", " Williams"])
    empty_output = get_full_names(empty_first_names, empty_last_names)

    assert np.array_equal(empty_output, expected_empty_output), f"Expected {expected_empty_output}, but got {empty_output}"

except AssertionError as e:
    print(f"Test 2 Failed: {e}")
else:
    print("✅ Test 2 Passed!")


# ### 🌟 Exercise (Extra Credit 2pts)
# If the first_names and last_names are of unequal length, the function should raise a Value Error exception with a proper error message.
# 
# You can apply the changes to the previous cell, all tests should still pass normally

# In[ ]:


# 🕵️ This code block checks your answer.
# Test 3: For Extra Credit - Arrays of unequal lengths (This should raise an error)
try:
    unequal_first_names = np.array(["Bob"])
    unequal_last_names = np.array(["Smith", "Jones"])
    unequal_output = get_full_names(unequal_first_names, unequal_last_names)
    
except ValueError:
    print("✅ Test 3 Passed! ValueError raised as expected.")
except AssertionError as e:
    print(f"Test 3 Failed: {e}")
except Exception as e:
    print(f"Test 3 Failed. Expected ValueError but got {type(e).__name__}: {e}")
else:
    print("Test 3 Failed. No error was raised.")


# > 🚩 : Make a git commit here

# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.
# 

# In[ ]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python python-exercises.ipynb')

