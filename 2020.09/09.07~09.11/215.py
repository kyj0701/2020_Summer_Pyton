# nums = [3, 2, 1, 5, 6, 4]

def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort(reverse = True)
    return nums[k-1]