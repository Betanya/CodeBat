"""
Given a string, return the count of the number of times
that a substring length 2 appears in the string and also as the
last 2 chars of the string, so "hixxxhi"
yields 1 (we won't count the end substring).
"""
def last2(a):
    counter = -1
    for i, val in enumerate(a):
        if i + 1 < len(a):
            if a[-1] == a[i+1] and a[-2] == a[i]:
                counter += 1
    if counter < 0:
        counter = 0
    return counter



'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''
a = 'iaxxai'
b = 'aaxxaaxx'

def string_match(a, b):

    counter = 0

    lenA = len(a)
    lenB = len(b)

    if lenA >= lenB:
       for i, val in enumerate(b):
            if i+1 < lenB:
                if a[i] == b[i] and a[i+1] == b[i+1]:
                    counter += 1
    elif lenA <= lenB:
       for i, val in enumerate(a):
            if i+1 < lenA:
                if a[i] == b[i] and a[i+1] == b[i+1]:
                    counter += 1
    return counter


#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


def array123(nums):
    idx1 = 0
    idx2 = 0
    idx3 = 0
    if 1 in nums:
        idx1 = nums.index(1)

    if 2 in nums:
        idx2 = nums.index(2)

    if 3 in nums:
        idx3 = nums.index(3)

    if idx1 < idx2 < idx3:
        return (True)
    else:
        return (False)

#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str2):
  ans = ""

  for ctn, val in enumerate(str2, 1):
      ans+= str2[0:ctn]
  return(ans)

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str2):
  li = list(str2)
  new_li = []
  for counter, val in enumerate(li):
    if counter % 2 == 0:
        new_li.append(val)

  str2 = ''.join(map(str, new_li))
  return (str2)

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[0:3] * n
