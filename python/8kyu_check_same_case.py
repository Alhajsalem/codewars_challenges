def same_case(a, b):   
    if (a.isalpha() and b.isalpha()):
        if ((a.islower() and b.islower()) or (a.isupper() and b.isupper())):
            return 1;
        else:
            return 0;
    return -1;

        
class Solution_1(object):
    def fizzBuzz(self, n):
        result = [];
        for i in range(1,n+1):
            if ((i % 3 == 0) and (i % 5 == 0)):
                result.append("FizzBuzz")
            elif (i % 3 == 0):
                result.append("Fizz")
            elif (i % 5 == 0):
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

""" a = Solution_1();
a.fizzBuzz(5) """


class Solution_2(object):
    def numberOfSteps(self, num):
        counter = 0;
        while num != 0:
            counter += 1;
            if num % 2 == 0:
                num/=2;
            else:
                num-=1;
        return counter
# b = Solution_2();
# result = b.numberOfSteps(8);
# print(result)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ln = 0;
        for i in head:
           ln+=1
        return(head[int(ln/2):])

def removeDuplicates(nums):
    i = 1;
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i-=1;
        i+=1
    return len(nums)

#print(removeDuplicates([0,1,1,1,2,2,3,3,4]))

def maxProfit(prices):
    max_value = 0
    result = []
    for i in range(1,len(prices)):
        if (prices[i] > prices[i-1]):
            max_value = prices[i]
            result.append(max_value-prices[i-1])
    return sum(result)
#print(maxProfit([7,1,5,3,6,4]))

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_n = {}
        for i in nums:
            try:
                dict_n.pop(i)
            except:
                dict_n[i] = 1

        return dict_n.popitem()[0]

            
#print(singleNumber([4,1,1,2,1,2,9,9]))

def moveZeroes(nums):
    nums.sort(key=lambda num: num == 0)
    
#print(moveZeroes([0,1,0,3,12]))


def plusOne(digits):
    return [int(x) for x in str(int("".join([str(i) for i in digits]))+1)]
    
#print(plusOne([1,2,3]))


def intersect(nums1, nums2):
    return [nums2.pop(nums2.index(n)) for n in nums1 if n in nums2]

#print(intersect([2,2,4,4,4,4],[1,2,2,1,4]))

def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for ii in range(i+1,len(nums)):
            if (nums[i] + nums[ii]) == target:
                result.append(i)
                result.append(ii)
                return result
#print(twoSum([3,2,4],6))

def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
       

#print(reverseString(["h","e","l","l","o"]))

def reverse(x):

    return int(str(x)[::-1])
#print(reverse(-123))

def firstUniqChar(s):
        """
        :type s: str
        :rtype: int        """
        for i in range(len(s)):
            if s.index(s[i]) == s.rfind(s[i]):
                return i;
        return -1
         
#print(firstUniqChar("loveleetcode"))

def oddNumbers(l, r):
    result = []
    for i in range(l,r+1):
        if i % 2 != 0:
            result.append(i)
    return result;
#print(oddNumbers(3,9))


def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
       
#print(isAnagram("anagram","nagaramlm"))

def isPalindrome(s):

    """
    :type s: str
    :rtype: bool
    """
    ss= "";
    for letter in s:
        if letter.isalpha():
            ss += letter.lower()
    return ss == ss[::-1]

s = "0P";
#print(isPalindrome(s));

def strStr(haystack, needle):
    try:
       return haystack.index(needle)
    except:
        return -1
haystack = "sadbutsad";
needle = "m";
#print(strStr(haystack,needle))

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length_of_items = [len(i) for i in strs];
        world = strs.pop(length_of_items.index(min(length_of_items)))
        
        result = "flower,flow"
        x = result.replace("f","",5)
        print(x)
        for i in range(len(world)+1):
            compare = world[0:i+1]
            for ii in range(len(strs)):
                if compare in strs[ii]:
                    result = result + compare
                    print(result)

                



strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        for i in range(n):
            first = first.next
        
        while first.next is not None:
            first = first.next
            second = second.next
        else:
            second.next = second.next.next
        
        return dummy.next

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)
  

#print(same_structure_as([1,[1,1]],[2,[2,2,1]]))


def squares(x, n):
    result = [x];
    for i in range(n-1):
        result.append(result[i]**2)
    return result


squares(2, 5)#, [2, 4, 16, 256, 65536]
from itertools import accumulate, repeat
def squares(x, n):
    return list(accumulate(repeat(x, n), lambda a, _: a * a))