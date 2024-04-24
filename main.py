# prices = [7,1,5,3,6,4]
#
# if not prices:
#     return 0
#
# mini = prices[0]
# maxi = 0
#
# for i in prices:
#     if i < mini:
#         mini = i
#     else:
#         maxi = max(maxi, (i - mini))
#
# return maxi
import math
import random

#
# s = "bcabc"
# a = []
# for i in s:
#     if i not in a:
#         a.append(i)
# a = "".join(a)
# print(a)
#
#
# s = "aa"
# t = "a"
# s, t = sorted(s), sorted(t)
# i, j = 0, 0
#
# while i < len(s) and j < len(t):
#     if s[i] != t[j]:
#         return t[j]
#     i += 1
#     j += 1
#
# return t[-1]


# nums = [1, 2, 3, 34, 54, 54, 5, 8]
#
# if len(nums) != len(set(nums)):
#     a = []
#     b = set()
#
#     for i in nums:
#         if i in b:
#             a.append(i)
#         else:
#             b.append(i)
#
# return a

# nums = [1, 3, 4, 2, 2]
#
# a = []
# for i in nums:
#     if i not in a:
#         a.append(i)
#     else:
#         return i
#         break

# words = ["wk", "xf", "ot", "je", "hd", "kw", "fx", "to", "ej"]
# a = []
# c = 0
# for i in words:
#     a.append("".join(sorted(i)))
# # for i in a:
# #     if a.count(i) >= 2:
# #         c += 1
# #         a.remove(i)
# #         a.remove(i)
# print(len(a) - len(set(a)))
#
# import math
#
# n = 10
# c = 0
#
#
# def primeCheck(x):
#     sta = 1
#     for i in range(2, int(math.sqrt(x)) + 1):  # range[2,sqrt(num)]
#         if x % i == 0:
#             sta = 0
#             break
#         else:
#             continue
#     return sta
#
#
# for i in range(2, n):
#     if primeCheck(i) == 1:
#         print(i)
#         c += 1
# print(c)
#
#
# n = 135
# c = 0
# g = []
# for i in range(1, n + 1):
#     if i < 11:
#         print(i)
#         c += 1
#     else:
#         # if len(list(str(i))) == len(list(set(list(str(i))))):
#         #     c += 1
#         #     print(list(str(i)) == list(set(list(str(i)))), i)
#         # else:
#         #     g.append(i)
#         for o in str(i):
#             if str(i).count(o) >= 2:
#                 continue
#             else:
#                 c += 1
#
#
# print("Count", c)
# print(g)

# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# return "".join(word1) == "".join(word2)
#
# nums = [2, 2, 1, 1, 1, 2, 2]
#
# maxim = [0, 0]
#
# for i in nums:
#     if nums.count(i) > maxim[1]:
#         maxim[0] = 0
#         maxim[0] += i
#         maxim[1] = 0
#         maxim[1] += nums.count(i)
#
# print(maxim[1])
#
#
# nums1 = [1, 1, 2]
# nums2 = [1, 2, 3]
# k = 2
# a = []
#
# for i in range(k):
#     g = [min(nums1), min(nums2)]
#     a.append(g)
#     nums2.remove(min(nums2))
# print(a)

#
# n = 7
# f = math.factorial(n)
# print(f)
# f = str(f).count('0')
# print(f)

# nums = [1,2,3,1]
# s = 0
#
# for i in range(0, len(nums), 2):
#     s += i
# print(s)
#
# nums = []
# nums2 = sorted(nums)
# a = 0
# 
# for i in range(0, len(nums)):
#     if nums[i] != nums2[i]:
#         a += 1
# print(a)

# num = "3200014888"
# large = []
# for i in range(1, len(num) - 1):
#     if num[i - 1] == num[i] and num[i] == num[i + 1]:
#         large.append(f'{num[i]}{num[i]}{num[i]}')
#
# if large:
#     print(max(large))
# else:
#     print(""
#
# nums = [0, 1]
#
# a = 0
#
# while a in nums:
#     a += 1
#
# print(a)

# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
#
# nums = nums1 + nums2
# nums = list(set(nums))
# nums = sorted(nums)[::-1]
#
# a = [i for i in nums[:k]]
# print(a)
#
#
# matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
# k = 8
# a = []
#
# for i in matrix:
#     for j in i:
#         a.append(j)
# print(sorted(a))
# print(sorted(a)[k - 1])
#

#
# nums = [1, 2, 3, 5]
# nums = sorted(nums)  # 1, 5, 5, 11
# a1 = []
# a2 = []
# for i in nums:
#     if i != max(nums):
#         a1.append(i)
#     else:
#         a2.append(i)
# if sum(a1) == sum(a2):
#     print(True)
# else:
#     if sum(a1) > sum(a2):
#         for i in a1:
#             if sum(a1) - i == sum(a2) + i:
#                 print(True)
#         print(False)


# s = "spacing"
# o = ""
# spaces = [0, 1, 2, 3, 4, 5, 6]
# a = []
# for i in range(len(spaces)):
#     if spaces[i] != spaces[0]:
#         g = s[spaces[i - 1] : spaces[i]]
#         a.append(g)
#     else:
#         a.append(s[:spaces[i]])
# for k in a:
#     o += k
# print(o)
#
# s = "abbaca"
# s = list(s)
# for i in s:
#     if s.count(i) >= 2:
#         s.remove(i)
#         s.remove(i)
# print("".join(s))


# arr = [1, 1]
#
# maxim = [0, 0]
#
# for i in range(len(arr)):
#     if arr.count(arr[i]) > maxim[1]:
#         maxim[0] = arr[i]
#         maxim[1] = arr.count(i)

# s = "lEetcOde"
# v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# a = []
# l = 0
# for i in s:
#     if i in v:
#         a.append(i)
#
# a = a[::-1]
# s = list(s)
# a = sorted(a)
# for i in range(len(s)):
#     if s[i] in v:
#         s[i] = a[l]
#         l += 1
# print("".join(s))

#
# words = ["mass", "as", "hero", "superhero"]
# a = []
# for i in words:
#     for j in words:
#         if i in j and j != i and len(i) != len(j):
#             a.append(i)
# print(a)


# s = "-4193 with words"
# a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
# s1 = ""
# for i in s:
#     if i in a:
#         s1 += i
# print(int(s1))


# s = "dfa12321afd"
# n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# for i in s:
#     if i in n:
#         a.append(int(i))
# l = list(set(a))
# if len(l) != 1:
#     print(sorted(l)[-2])
# else:
#     print(-1)

# word1 = "abc"
# word2 = "pqr"
# a = ""
# for i, j in zip(word1, word2):
#     a += i
#     a += j
# print(a)

# s = "is2 sentence4 This1 a3"
# s = s.split(' ')
# a = {}
# n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# for i in s:
#     for j in n:
#         if j in i:
#             i = i.replace(j, "")
#             a[j] = i
# a = sorted(a.items())
# s = ""
# for i in a:
#     s += i[1]
#     s += " "
# print(s)
#
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# a = {}
# for i in range(len(s)):
#     a[indices[i]] = s[i]
# g = sorted(a.items())
# s = ""
# for i in g:
#     s += i[1]
#     s += ""
# print(s)
#
# low = 2
# high = 7
# c = 0
#
# if low % 2 != 0:
#     for i in range(low, high + 1, 2):
#         c += 1
# else:
#     for i in range(low+1, high + 1, 2):
#         c += 1
# print(c)


# num = [2, 1, 5]
# k = 806
#
# a = ""
# b = ""
# for i in num:
#     a += str(i)
# for j in str(k):
#     b += str(j)
#
# g = int(a) + int(b)
# l = []
# for i in str(g):
#     l.append(int(i))
# print(l)

# words = ["leet","code"]
# x = "e"
# a = []
#
# for i in range(len(words)):
#     if x in words[i]:
#         a.append(i)
# print(a)
#
# words = ["never", "gonna", "give", "up", "on", "you"]
# s = "ngguoy"
# a = ""
# for i in words:
#     a += i[0]
# print(a)
# print(a == s)

# nums1 = [1,2,3]
# nums2 = [2,4]
# if min(nums1) in nums2 and min(nums1) < min(nums2) and min(nums2) not in nums1:
#     print(min(nums1))
# else:
#     print(min(nums2))

# nums = [13, 25, 83, 77]
# a = []
# for i in nums:
#     for j in str(i):
#         a.append(int(j))
# print(a)


# num = 30
# c = 0
# for i in range(2, num):
#     if i % 2 == 0:
#         c += 1
#         print(i)
# print(c)

# names = ["Alice", "Bob", "Bob"]
# heights = [155, 185, 150]
# a = {}

# for i in zip(names, heights):
#     a[i[1]] = i[0]
# a = sorted(a.items())[::-1]
# names = []
# for i in a:
#     names.append(i[1])
# print(names)

# nums = [8, 1, 2, 2, 3]
# ans = []
# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if nums[j] < nums[i]:
#             count += 1
#     ans.append(count)
# return ans

# nums = [-4, -1, 0, 3, 10]
# a = []
#
# for i in nums:
#     if i < 0:
#         a.append(abs(i * i))
#     else:
#         a.append(i * i)
# print(sorted(a))

#
# nums = [-4, -2, 1, 4, 8]
# a = nums[0]
# for i in nums:
#     if i < a:
#         a = 0
#         a += i
# print(a)


# s = "Hello how are you Contestant"
# k = 4
#
# a = [i for i in s.split()[:k]]
# s = ""
# for i in a:
#     s += i
#     s += " "


# text = "Keep calm and code on"
# y = [i for i in text.split()]
# a = {}
# for i in y:
#     a[i] = len(i)
# y = sorted(a.items())[::-1]
# text = ""
# for i in y:
#     text += i[0].lower()
#     text += " "
# return text.capitalize()


# address = "1.1.1.1"
# a = [i for i in address.split('.')]
# l = ""
# for i in a:
#     l += i
#     l += "[.]"
# print(l[:len(l) - 3])

# n = 10
# m = 3
# ns = [i for i in range(1, n + 1)]
# c = 0
# for i in ns:
#     if i % m == 0:
#         c += i
# print(sum(ns) - c - c)
#
# n = 234
# n = str(n)
# c1 = 1
# c2 = 0
# for i in n:
#     c1 *= int(i)
#     c2 += int(i)
# print(c1 - c2)
#
# str1 = "ABABAB"
# str2 = "ABAB"
#
# minim = min(str1, str2)
# maxim = max(str1, str2)
#
# for i in range(len(minim), 0, -1):
#     j = minim[0:i]
#     if i in maxim:
#         return j


# hours = [0, 1, 2, 3, 4]
# target = 4
# c = 1
# if target not in hours:
#     print(0)
# else:
#     for i in hours:
#         if i == target:
#             print(c)
#             break
#         else:
#             c += 1

#
# accounts = [[1,2,3],[3,2,1]]
# a = []
# for i in accounts:
# #     a.append(sum(i))
# # print(max(a))
#
# nums = [-6, 2, 5, -2, -7, -1, 3]
# target = -2
# c = 0
# for i in range(len(nums) - 1):
#     print(nums[i], nums[i + 1])
#     if sum([nums[i], nums[i + 1]]) > target:
#         c += 1
# print(c)

#
# nums = [0, 1, 2, 3, 4]
# index = [0, 1, 2, 2, 1]
# a = []
# for i in range(0, len(nums)):
#     a.insert(index[i], nums[i])
# print(a)


# nums = [1, 15, 6, 3]
# su = sum(nums)
# s = []
# a = ""
# for i in nums:
#     a += str(i)
# for i in a:
#     s.append(int(i))
# s = su - sum(s)
# print(s)


# title = "First leTTeR of EACH Word"
# a = [i for i in title.split()]
# b = ""
# for i in a:
#     if len(i) >= 3:
#         b += i.capitalize()
#         b += " "
#     else:
#         b += i.lower()
#         b += " "
# print(b)

#
# nums = [3, 3]
# target = 6
# a = []
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             a.append(i)
#             a.append(j)
#             break

# print(a)

#
# nums1 = [1]
# nums2 = [2, 3, 4, 5, 6, 7, 8]
# nums = nums1 + nums2
# nums.sort()
# print(nums[len(nums) // 2 - 1])

# a = ""
# s = "     42"
# nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# s = s.strip()
# for i in s:
#     if i in nums:
#         a += i
# if '-' in s:
#     print(int(a) - int(a) * 2)
# else:
#     print(int(a)


# x = 121
# x = str(x)
# print(list(x))
# print(list(x)[::-1])


# nums = [1, 3, 5, 6]
# target = 7
# if target in nums:
#     print(nums.index(target))
# else:
#     nums.append(target)
#     nums = sorted(nums)
#     print(nums.index(target))

# s = "the sky is blue"
# s = s.strip()
# s = [i for i in s.split()][::-1]
# a = ""
# for i in s:
#     a += i
#     a += " "
# return a

# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 13
# a = []
# for i in matrix:
#     for j in i:
#         a.append(j)
# print(target in a)
# #
# s = "abcd"
# t = "abcde"

