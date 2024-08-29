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
from typing import List

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


# s = "abcabcbb"
# a = []
# b = []
# for i in range(len(s)):
#     b.append(s[i])
#     if len(b) != len(set(b)):
#         b.remove(b[-1])
#         a.append(b)
#         b = []
#     for j in range(i + 1, len(s)):
#         b.append(s[j])
#         if len(b) != len(set(b)):
#             b.remove(b[-1])
#             a.append(b)
#             b = []
# b = []
# for i in a:
#     b.append("".join(i))
# max_len = 1
# for i in b:
#     if len(i) > max_len:
#         max_len = len(i)
# print(max_len)

# word = "abcdefd"
# ch = "d"
# f = word.index(ch)
# a = word[:f+1]
# b = word[f:]
# print(a[::-1]+b)

# nums = [-1, 10, 6, 7, -7, 1]
# positives = []
# negatives = []
# for i in nums:
#     if i > 0:
#         positives.append(i)
#     negatives.append(i)
# positives = sorted(positives)[::-1]
# for i in positives:
#     if -abs(i) in negatives:
#         print(i)
#         break
# print(-1)


# text = "leet code"
# brokenLetters = "e"
# a = [i for i in text.split()]
# b = [i for i in brokenLetters]
# c = 0
# for i in a:
#     l = 0
#     for j in b:
#         if j not in i:
#             l += 1
#     if l == len(b):
#         c += 1
# print(c)


# s = "zaz"
# a = []
# for i in range(len(s) - 1):
#     a.append(abs(ord(s[i]) - ord(s[i + 1])))
# print(sum(a))

# s = ["h", "e", "l", "l", "o"]
# h = [i for i in s]
# for i in h:
#     s.insert(0, i)
#     s.pop(-1)
# print(s)
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# for i in range(k):
#     nums.insert(0, nums.pop(-1))
# print(nums)
#
# words = ["cool", "lock", "cook"]
# chs = []
# a = ""
# for i in words:
#     a += i
# a = list(a)
# mxlen = max(len(i) for i in words)
# for i in range(mxlen):
#     if a.count(a[i]) >= len(words):
#         chs.append(a[i])
#         a.remove(a[i])
#         a.remove(a[i])
#         a.remove(a[i])
# print(chs)

# strs = ["flower", "flow", "flight"]
# s = 0
# for i in zip(*strs):
#     if len(set(i)) > 1:
#         break
#     s += 1
# return strs[0][:s]


# nums = [3, 3, 4]
# s = list(set(nums))
# j = {}
# for i in s:
#     j[nums.count(i)] = i
# a = max(j)


# haystack = "sadbutsad"
# needle = "sad"
# print(haystack.find(needle))

# numbers = [2, 3, 4]
# target = 6
# for i in range(len(numbers) - 1):
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] + numbers[i] == target:
#             print([i + 1, j + 1])
#             break


# nums = [1, 2, 1, 3, 5, 6, 4]
# for i in range(1, len(nums) - 1):
#     if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
#         print(i)
#         break
#
# nums1 = [1, 2, 4, 5, 6]
# nums2 = [3, 5, 7, 9]
# k = 3


# arr1 = [28, 6, 22, 8, 44, 17]
# arr2 = [22, 28, 8, 6]
# a = []
# f = []
# for i in arr2:
#     if i in arr1:
#         l = 0
#         for j in range(arr1.count(i)):
#             a.append(i)
# for i in arr1:
#     if i not in a:
#         a.append(i)
#
# print(a)


# nums = [4, 5, 0, -2, -3, 1]
# k = 5
# a = 0
# for i in range(len(nums) + 1):
#     for j in range(i, len(nums) + 1):
#         if sum(nums[i:j]) % k == 0 and nums[i:j] != []:
#             a += 1
# print(a)

#
# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# s = sentence.split(" ")
# print(s)
# for i in s:
#     for j in dictionary:
#         if i.find(j) == 0:
#             sentence = sentence.replace(i, j)
# print(sentence)

#
# s = "abcd"
# indices = [0, 2]
# sources = ["a", "cd"]
# targets = ["eee", "ffff"]
# for i, j in zip(sources, targets):
#     s = s.replace(i, j)
# print(s)

# nums = [1, 2, 4, 6]
# operations = [[1, 3], [4, 7], [6, 1]]
# nums = "".join([str(i) for i in nums])
# for i in operations:
#     nums = nums.replace(str(i[0]), str(i[1]))
# operations = [int(i) for i in nums]
# print(operations)

# seats = [12, 14, 19, 19, 12]
# students = [19, 2, 17, 20, 7]
# c = 0
# a = []
# seats, students = sorted(seats), sorted(students)
# for i, j in zip(students, seats):
#     a.append([i, j])
# print(a)

# grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0], [1, 1, 1]]
# a = 0
# for i in range(len(grid)):
#     if sum(grid[i]) > sum(grid[a]):
#         a = i
# print(a)

#
# mountain = [1, 4, 3, 8, 5]
# a = []
# for i in range(1, len(mountain) - 1):
#     if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
#         a.append(i)
# print(a)

# nums = [23,2,6,4,7]
# k = 13
# bl = False
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if len(nums[i:j]) != 0:
#             a = sum(nums[i:j])
#             if a % k == 0:
#                 bl = True
#                 break
# print(bl)

# nums = [1, 2, 3, 4]
# g = []
# l = "".join(map(str, nums))
# for i in l:
#     g.append(int(i))
# a = sum(g)
# b = sum(nums)
# print(abs(a - b))

# nums = [76, 24, 96, 82, 97]
# s = 0
# a = []
# for i in range(0, len(nums) + 1):
#     for j in range(i + 1, len(nums) + 1):
#         a += [nums[i:j]]
#
# for i in range(0, len(nums)):
#     for j in range(i + 2, len(nums)):
#         a.append([nums[i], nums[j]])
#
# for i in a:
#     s += max(i) ** 2 * min(i)
# print(a)
# print(s)


# edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
# a = []
# b = {}
# for i in edges:
#     for j in i:
#         a.append(j)
# for i in a:
#     if i not in b:
#         b[i] = a.count(i)
# for i in b.items():
#     if i[1] == len(edges):
#         print(i[0])

# nums = [8, 1, 2, 2, 3]
# a = []
# b = 0
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)):
#         if nums[i] > nums[j]:
#             b += 1
#     a.append(b)
#     b = 0
# print(a)

# words = ["leetcode", "et", "code"]
# words.sort(key=len)
# a = []
# for i in range(0, len(words)):
#     for j in range(i + 1, len(words)):
#         if words[i] in words[j]:
#             a.append(words[i])
#         if words[j] in words[i]:
#             a.append(words[j])
# print(a)


# nums1 = [1, 2]
# nums2 = [1, 1]
# y = []
# max_len = max(len(nums1), len(nums2))
# min_len = min(len(nums1), len(nums2))
# smax_len = max(len(list(set(nums1))), len(list(set(nums2))))
# smin_len = min(len(list(set(nums1))), len(list(set(nums2))))
# if max_len != min_len:
#     maximum = nums1 if len(nums1) == max_len else nums2
#     minimum = nums1 if len(nums1) == min_len else nums2
# else:
#     maximum = list(set(nums1)) if len(list(set(nums1))) == smax_len else list(set(nums2))
#     minimum = list(set(nums1)) if len(list(set(nums1))) == smin_len else list(set(nums2))
# for i in minimum:
#     if i in maximum:
#         y.append(i)
# print(y)

# nums1 = [1, 2, 3, 3]
# nums2 = [1, 1, 2, 2]
# a = []
# b = []
# c = []
# for i in nums1:
#     if i not in nums2:
#         b.append(i)
# for i in nums2:
#     if i not in nums1:
#         c.append(i)
# a.append(list(set(b)))
# a.append(list(set(c)))
# print(a)

#
# arr1 = [2, 1, 100, 3]
# arr2 = [-5, -2, 10, -3, 7]
# d = 6
# c = 0
# for i in arr1:
#     for j in arr2:
#         if abs(i - j) <= d:
#             print(i, j)
#             c += 1
# print(c)

# s = "abacbc"
# a = list(set(s))
# b = []
# for i in a:
#     b.append(s.count(i))
# if len(list(set(b))) == 1:
#     print(True)

# text = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"
# if " " in text:
#     while "," in text:
#         text = text.replace(",", "")
#         a = [i for i in text.split(" ")]
# else:
#     a = [i for i in text.split(",")]
# word = a[0]
# for i in a:
#     if len(i) > len(word):
#         word = i
# print(word)

#
# def format_text(input_text):
#     words = input_text.split()
#     text = input_text
#     if " " in text:
#         while "," in text:
#             text = text.replace(",", "")
#             a = [i for i in text.split(" ")]
#     else:
#         a = [i for i in text.split(",")]
#     word = a[0]
#     for i in a:
#         if len(i) > len(word):
#             word = i
#     max_line_length = len(word) * 3
#     print(len(word))
#     print(max_line_length)
#     lines = []
#     current_line = ""
#
#     for word in words:
#         # Обрабатываем запятые
#         if word.endswith(','):
#             word += " "
#
#         if len(current_line) + len(word.strip()) <= max_line_length:
#             if current_line:
#                 current_line += " "
#             current_line += word.strip()
#         else:
#             lines.append(current_line.strip())
#             current_line = word.strip()
#
#     if current_line:
#         lines.append(current_line.strip())
#
#     return "\n".join(lines)
#
#
# # Test 1
# input_text1 = "once upon a time, in a land far far away lived a princess, whose beauty was yet unmatched"
# formatted_text1 = format_text(input_text1)
# print(formatted_text1)
# test2 = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"
# print(len(test2))
# formatted_text2 = format_text(test2)
# print(formatted_text2)
#
# details = ["1313579440F2036", "2921522980M5644"]
# ages = []
# for i in details:
#     ages.append(int(i[11:13]))
# ages = [i for i in ages if i > 60]
# print(len(ages))


# s = "ab-cd"
# d = {}
# a = []
# for i in range(0, len(s)):
#     if s[i].isalpha() == False:
#         d[i] = s[i]
#         s = s.replace(s[i], '-')
#     else:
#         a.append(s[i])
# a = a[::-1]
# for i in d.items():
#     a.insert(i[0], i[1])
# print("".join(a))
#
# s = "fvokzonyhukpwbnkomdianhirsvdulhsfseaqzktupyeverfsd"
# indices = [26, 30, 38, 2, 41, 10, 8, 44, 19, 4, 13, 28, 21, 35, 23, 16]
# sources = ["vd", "hsfs", "ktu", "ok", "pye", "kp", "hu", "verfs", "ia", "zon", "bnk", "ul", "nh", "aqz", "irs", "om"]
# targets = ["h", "gdlf", "nl", "sr", "xhn", "ax", "arf", "ifuax", "a", "mk", "vwqe", "fdl", "n", "miyr", "ibh", "den"]
# a = {}
# for i, j in zip(indices, sources):
#     if s[i:i + len(j)] == j:
#         a[j] = targets[sources.index(j)]
# for i in a.items():
#     s = s.replace(i[0], i[1])
# print(s)


# text = "alice is a good girl she is a good student"
# first = "a"
# second = "good"
# a = []
# text = [i for i in text.split()]
# for i in range(len(text)):
#     if text[i] == first and text[i + 1] == second:
#         a.append(text[i + 2])
# print(a)
#
# nums = [1, 2, 3, 4]
# n = 4
# left = 1
# right = 5
# a = []
# for i in range(len(nums)):
#     a.append(nums[i])
#     for j in range(i + 1, len(nums)):
#         a.append(sum(nums[i:j + 1]))
# a = sorted(a)
# print(sum(a[left - 1:right]))

# s = "loveleetcode"
# for i in range(0, len(s)):
#     if s.count(s[i]) == 1:
#         print(i)

# num = 13423
# while len(str(num)) != 1:
#     s = 0
#     for i in str(num):
#         s += int(i)
#     num = s
#     s = 0
# print(num)

# nums = [-1, -1]
# a = []
# for i in range(0, len(nums)):
#     c = 0
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[i]:
#             c += 1
#     a.append(c)
# print(a)

# s1 = "apple apple"
# s2 = "banana"
# a = [i for i in s1.split()]
# b = [i for i in s2.split()]
# a = a + b
# b = []
# for i in a:
#     if a.count(i) == 1:
#         b.append(i)
# print(b)


# s = "(u(love)i)"
# g = []
# a = []
# b = []
# c = []
# for i in range(len(s)):
#     if s[i] == "(":
#         a.append(i)
# for j in range(len(s)):
#     if s[-j] == ")":
#         b.append(len(s) - j + 1)
# a, b = a[::-1], b[::-1]
# for i, j in zip(a, b):
#     c.append(s[i:j].replace("(", "").replace(")", ""))
# a = [i+1 for i in a]
# b = [i-1 for i in b]
# c = c[::-1]
# if c[1]:
#     c[0] = c[0].replace(c[1], c[1][::-1])
#     c.pop(1)
# if c:
#     c[0] = c[0][::-1]
#     c[0] = c[0].replace(c[1], c[1][::-1])
#     c.pop(1)
# print(c)

# s = "abcd"
# if s == "".join(s[::-1]):
#     print(True)

# def gett(s):
#     for i in range(0, len(s)):
#         for j in range(len(s), i + 1, -1):
#             if s[i:j] == s[i:j][::-1]:
#                 return s[i:j]
#                 break
#     return False
#
#
# if gett(s) is not False:
#     print(True)
# else:
#     s = s[::-1] + s[::]
#     if gett(s) is not False:
#         print(True)
#     print(False)

# s = "abcd"
# t = "abcde"
# a = list(s) + list(t)
# for i in a:
#     if a.count(i) >= 2:
#         a.remove(i)
#         a.remove(i)
# print(a)
#
# nums = [1, 3, 5, 4, 7]
# g = []
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums) - 1):
#         a = nums[i:j+1]
#         for h in range(len(a) - 1, 0, -1):
#             if nums[h] >= nums[h + 1]:
#                 g.append(a[:h])
#                 continue
#             else:
#                 continue
# print(g)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# c = 1
# for i in a[-k:]:
#     c = c * i
# print(c)

# operations = ["--X", "X++", "X++"]
# c = 0
# for i in operations:
#     if sorted(i) == ['+', '+', 'X']:
#         c += 1
#     else:
#         c -= 1
# print(c)
#
# bills = [5, 5, 5, 10, 20]
# a = []
# for i in bills:
#     a.append(i)
#     if i == 5:
#         continue
#     elif i == 10:
#         if 5 in a:
#             a.remove(5)
#             continue
#         else:
#             print(False)
#     elif i == 20:
#         if 5 in a and 10 in a:
#             a.remove(5)
#             a.remove(10)
#             continue
#         else:
#             print(False)
# print(True)


# nums = [1, 1]
# a = []w\
# for i in range(1, max(nums)):
#     if i not in nums:
#         a.append(i)
# print(a)

# nums = [5, 4, -1, 7, 8]
# c = 0
# for i in range(0, len(nums) + 1):
#     for j in range(i + 1, len(nums) + 1):
#         if sum(nums[i:j]) > c:
#             c = sum(nums[i:j])
# print(c)


# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# a = ["", ""]
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i:j] in wordDict and s[i:j] not in a[0]:
#             a[0] += s[i:j]
#             a[0] += " "
#         else:
#             a[1] += s[i:j]
# print(a)
