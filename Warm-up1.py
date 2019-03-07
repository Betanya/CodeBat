

#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


def front3(str):
  first_3 = str[0:3]

  ans = first_3 * 3
  return ans

#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) > 1:
    str_list = list(str)


    str_list[0], str_list[-1] = str_list[-1], str_list[0]

    retur n(''.join(str_list))
  else:
    return str

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  newstr = str.replace(str[n], "")
  return newstr


#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  first_three_letters = str[0:3]
  if first_three_letters == 'not':
    return (str)
  else:
    new_word = [x for x in str]
    new_word = ['n', 'o', 't', ' '] + new_word

    return (''.join(new_word))

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  return (a == 10 or b == 10 or ( a + b == 10))

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if 7 > hour and talking == True:
    return True
  if hour > 20 and talking == True:
    return True
  else:
    return False


#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
  if 0 < n > 21:
    return abs(n-21) * 2
  else:
    return abs(n-21)


#Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.

def sum_double(a, b):
    if a == b:
        return (a + b) * 2

    else:
        return a + b


#The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are
# on vacation.
# We sleep in if it is not a weekday
# or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  if weekday == True and vacation == False:
    return False
  if weekday == False and vacation == True:
    return True
  if weekday == True and vacation == True:
    return True

  """
  We have two monkeys, a and b, 
  and the parameters a_smile and b_smile 
  indicate if each is smiling. We are in trouble 
  if they are both smiling or if neither of them 
  is smiling. 
  Return True if we are in trouble.
  """
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  if a_smile == False and b_smile == False:
    return True
  else:
    return False
