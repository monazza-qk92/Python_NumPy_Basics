# Python_NumPy_Basics

The role of a data scientist primarily involves exploring and analyzing data. The results of an analysis might form the basis of a report or a machine learning model, but it all begins with data, with Python being the most popular programming language for data scientists.

After decades of open-source development, Python provides extensive functionality with powerful statistical and numerical libraries:

* NumPy and Pandas simplify analyzing and manipulating data
* Matplotlib provides attractive data visualizations
* Scikit-learn offers simple and effective predictive data analysis
* TensorFlow and PyTorch supply machine learning and deep learning capabilities
Usually, a data analysis project is designed to establish insights around a particular scenario or to test a hypothesis.

In this notebook we will use some basic commands of NumPy package and a brief introduction to Pandas. We will use an example to understand this. Suppose a university professor collects data from their students, including the number of lectures attended, the hours spent studying, and the final grade achieved on the end of term exam. The professor could analyze the data to determine if there is a relationship between the amount of studying a student undertakes and the final grade they achieve. The professor might use the data to test a hypothesis that only students who study for a minimum number of hours can expect to achieve a passing grade.

## Lists and NumPy Arrays
In this exercise we will see some basic commands of python language related to NumPy package. We will see how lists and arrays works. The data has been loaded into a Python list structure, which is a good data type for general data manipulation, but not optimized for numeric analysis. For that, we're going to use the NumPy package, which includes specific data types and functions for working with Numbers in Python.

## Difference between List and NumPy array
Just in case you're wondering about the differences between a list and a NumPy array, let's compare how these data types behave when we use them in an expression that multiplies them by 2. Multiplying a list by 2 creates a new list of twice the length with the original sequence of list elements repeated. Multiplying a NumPy array on the other hand performs an element-wise calculation in which the array behaves like a vector, so we end up with an array of the same size in which each element has been multiplied by 2. The key takeaway from this is that NumPy arrays are specifically designed to support mathematical operations on numeric data - which makes them more useful for data analysis than a generic list.

## Shape of Array
To find the number of elements in array we use the keyword shape It returs a tuple(,), where the first number tells the number of elements in first axis or dimension and the second axis or dimension tells the number of elemnents in the second axis. The shape confirms that this array has only one dimension, which contains 22 elements (there are 22 grades in the original list).

To access the individual elements in the array by their zero-based ordinal position. To get the first element (the one in position 0) we use grades[0], It returns the first element.

## Mean or Average 
To find simple averages we use grades.mean().

We can add a second set of data for the same students, this time recording the typical number of hours per week they devoted to studying. To find shape of our new array we use student_data.shape, this time it's a 2D array.

## Navigate through 2D Array
To navigate the new 2D, we need to specify the position of each element in the hierarchy. So to find the first value in the first array (which contains the study hours data), we can use student_data[0][0].

## Mean of each Array
We can also find average of each array as following:
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

## Introduction to Pandas
While NumPy provides a lot of the functionality you need to work with numbers, and specifically arrays of numeric values; when you start to deal with two-dimensional tables of data, the Pandas package offers a more convenient structure to work with - the DataFrame.

![This is an image](https://github.com/monazza-qk92/Python_NumPy_Basics/blob/main/pandaaa.png)

Note that in addition to the columns you specified, the DataFrame includes an index to unique identify each row. We could have specified the index explicitly, and assigned any kind of appropriate value (for example, an email address); but because we didn't specify an index, one has been created with a unique integer value for each row.

