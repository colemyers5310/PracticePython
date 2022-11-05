#!/usr/bin/env python3

class Solution(object):
	
	def searchRange(self, nums, target):
		first, last, rnums, index = 0, len(nums) -1, [-1,-1], -1
		while first <= last and index == -1:
			mid = (first + last) // 2
			if target == nums[mid]:
				rnums[0] = self.findStart(nums, target, first, mid)
				rnums[1] = self.findEnd(nums, target, last, mid)
				index = 1
			elif target > nums[mid]:
				first = mid + 1
			else:
				last = mid - 1
		return rnums
	
	def findStart(self, nums, target, first, mid):
		while nums[mid] == target and first <= mid:
			mid -= 1
		return mid + 1
	
	def findEnd(self, nums, target, last, mid):
		while nums[mid] == target and mid <= last:
			mid += 1
		return mid - 1

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([1,1,2,3,3,3,3,3,3,4,4,5,5,6,7,7,8,8,10], 3))
#print(s.searchRange([], 0))


			
				