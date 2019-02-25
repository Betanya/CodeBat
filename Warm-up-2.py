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