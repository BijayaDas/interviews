"""
Question 2:

Egyptian fractions, were mentioned in the Rhind Papyrus of 500BC as an “ancient method” and are thought to date to the time of the pyramids; they survived in use until the 17th or 18th century. Leonardo de Pisa’s famous book Liber Abaci of 1215AD, which introduced to European mathematicians the concept of zero, the Hindu-Arabic system of numeration, and the famous rabbit sequence (Leonardo’s nickname was Fibonacci).

An Egyptian fraction was written as a sum of unit fractions, meaning the numerator is always 1; further, no two denominators can be the same. As easy way to create an Egyptian fraction is to repeatedly take the largest unit fraction that will fit, subtract to find what remains, and repeat until the remainder is a unit fraction. For instance, 7 divided by 15 is less than 1/2 but more than 1/3, so the first unit fraction is 1/3 and the first remainder is 2/15. Then 2/15 is less than 1/7 but more than 1/8, so the second unit fraction is 1/8 and the second remainder is 1/120. That’s in unit form, so we are finished: 7 ÷ 15 = 1/3 + 1/8 + 1/120. There are other algorithms for finding Egyptian fractions, but there is no algorithm that guarantees a maximum number of terms or a minimum largest denominator; for instance, the greedy algorithm leads to 5 ÷ 121 = 1/25 + 1/757 + 1/763309 + 1/873960180913 + 1/1527612795642093418846225, but a simpler rendering of the same number is 1/33 + 1/121 + 1/363.

Your task is to write a program that calculates the ratio of two numbers as an Egyptian fraction
"""

import math 
  
def calculate_egyptian_fraction(n, d):
  print("The Egyptian Fraction Representation of {0}/{1} is".format(n, d))
  list_dr = []
  while n != 0: 
    a = math.ceil(d / n)
    list_dr.append(a) 
    n = a * n - d 
    d = d * a
  
  for i in list_dr:
    print(" 1/{0}".format(i))

calculate_egyptian_fraction(6, 14)