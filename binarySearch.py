#!/usr/bin/env python3

class Solution (object):
	def binarySearch(self, nums, val):
		first = 0
		last = len(nums) - 1
		index = -1
		while first <= last and index == -1:
			mid = int((first + last)/2)
			if nums[mid] == val:
				index = mid
			else:
				if nums[mid] < val:
					first = mid + 1
				else:
					last = mid - 1
		return index

s = Solution()
print(s.binarySearch([1,2,3,4,5,6,7,8,11,144,200], 11))
					