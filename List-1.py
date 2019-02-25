#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  if nums[-1] == 6 or nums[0] == 6:
    return True
  else:
    return False
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[-1]:
    return True
  else:
    return False
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}
def make_pi():
  return [3, 1, 4]

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  if a[-1] == b[-1] or a[0] == b[0]:
    return True
  else:
    return False

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    ans = 0
    for n in nums:
        ans += n
    return ans
#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  rotate_left = []
  for counter, i in enumerate(nums):
    rotate_left.append(nums[counter-2])
  return rotate_left

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  for counter, i in enumerate(nums):
    nums = nums[::-1]
  return nums

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
    largest_num = 0
    if nums[0] < nums[-1]:
        largest_num = nums[-1]
    if nums[0] > nums[-1]:
        largest_num = nums[0]
    if nums[0] == nums[-1]:
        largest_num = nums[0]
    for counter, i in enumerate(nums):
        nums[counter] = largest_num
    return nums

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
  if len(nums) == 0:
     return 0
  if len(nums) < 2:
    return nums[0]

  else:
    ans = nums[0] + nums[1]
    return ans

#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    new_array = []
    new_array.append(a[1])
    new_array.append(b[1])

    return new_array

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

def make_ends(nums):
  new_array = []
  new_array.append(nums[0])
  new_array.append(nums[-1])
  return new_array

#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  if 2 in nums:
    return True
  if 3 in nums:
    return True
  else:
    return False

