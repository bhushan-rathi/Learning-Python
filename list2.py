#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  num =1
  index = []
  while num<len(nums):
  	if nums[num] == nums[num-1]:
  		index.append(num)
  	num += 1
  
  i=0
  i2=0
  newnums = []
  while i<len(nums):
  	try:
  		i2 = index.index(i)
  	except ValueError:
  		pass
  	if i != index[i2]:
  		newnums.append(nums[i])
  	i = i + 1	
  return newnums

#nums.remove(nums[num])
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

#linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
#['aa', 'xx'], ['bb', 'cc', 'zz']
#['aa', 'aa'], ['aa', 'bb', 'bb']
def linear_merge(list1, list2):
  # +++your code here++
  list3 = []
  a1 = len(list1)
  b1 = len(list2)
  a = list1.pop(-1)
  b = list2.pop(-1)

  while len(list2)!=0 or len(list1)!=0:
  	if a>b:
  		list3.append(a)
  		if len(list1)>0:
  			a = list1.pop(-1)
  		else:
  			list3 = myfn(list2, list3, b)
  	else:
  		list3.append(b)
  		if len(list2)>0:
  			b = list2.pop(-1)
  		else: 	
  			list3 = myfn(list1, list3, a)
  if len(list3)!= a1+b1:
  	if a>b :
  		list3.append(a)
  		list3.append(b)
  	else:
  		list3.append(b)
  		list3.append(a)
  	list3.reverse()
  return list3
def myfn(list11, list3, ab):
	list11.append(ab)
	list3.reverse()
	list11.reverse()
	list4 = []
  	while len(list11)>0:
  		c = list11.pop(-1)
  		if c>list3[-1]:
  			list3.append(c)
  		else:
  			list4.append(c)
  			list3 = list4+list3
  			list4 = []
 	return list3

#Above solution is have strictly linear time as we have
#used list.pop(-1)
# 
#list.pop(0)
# is not constant time with the standard python list implementation, so
# the slolution with pop(0) is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
