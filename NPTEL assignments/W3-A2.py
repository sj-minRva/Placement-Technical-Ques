#Week 3 - assignemnt 2
'''
At AeroPort-X, a futuristic logistics hub, drones are used to transport cargo based on
weight. A team of engineers is working on a system that reads incoming weight values for
parcels — often given as real numbers due to sensitive sensors. However,to fit them into
standardized cargo containers, each weight must be rounded down to the nearest whole number
— in other words, converted to the greatest integer less than or equal to it. Once converted,
the numbers are displayed on a screen, separated by commas, for the loading team to arrange
parcels efficiently.You are asked to build the logic for this conversion process.
Write a program that:
(a) Accepts a space-separated sequence of positive real numbers representing parcel
weights.
(b) Converts each number to the greatest integer less than or equal to it.
(c) Outputs the resulting integers, separated by commas.
'''

import math

cargo = input("Enter a decimal number: ").strip().split()


for x in cargo:
    weight = float(x)
    rounded = round(weight)
    print(rounded,",")
