
def rotate(nums, k):
    print(nums[k:] + nums[:k])
    """ for i in range(k):
        result = nums.pop(-1)
        nums.insert(0,result)
    return nums """



print(rotate([1,2,3,4,5,6,7],3))
""" Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4] """

def containsDuplicate(nums):
    #true' if True else 'false'
    True if len(set(nums)) != len(nums) else False




print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

