"""
Question 3:


The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.


Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.


(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def find_sum(n):
  sum_p = 0
  for i in range(n):
    if str(i) != str(i)[::-1]:
      continue
    if format(i, 'b') == format(i, 'b')[::-1]:
      sum_p += i
  return sum_p

print("sum of all palendromic numbers", find_sum(1000000))