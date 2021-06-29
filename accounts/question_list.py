# class questions(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     ques=models.CharField(max_length=300,blank=True,None=True)
#     ques_link=models.URLField(max_length=500,blank=True,None=True)
#     video=models.URLField(max_length=500,blank=True,None=True)
#     gfg=models.URLField(max_length=500,blank=True,None=True)
#     status=models.BooleanField(default=False)

from .models import *

# ['ques','editor','video_link,'gfg_lnk'],

questions_list = [

	# 					*********************************************************************DAY-1*********************************************************************

	['Sort an array of 0’s 1’s 2’s without using extra space or sorting algo',
	 'https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1',
	 'https://www.youtube.com/watch?v=oaVa-9wmpns&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=2',
	 'https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/'],
	['Repeat and Missing Number', 'https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1',
	 'https://www.youtube.com/watch?v=5nMGY4VUoRY&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=3',
	 'https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/'],
	['Merge two sorted Arrays without extra space',
	 'https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1',
	 'https://www.youtube.com/watch?v=hVl2b3bLzBw&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=4',
	 'https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/'],
	['Kadane’s Algorithm', 'https://leetcode.com/problems/maximum-subarray/',
	 'https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=5',
	 'https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/'],
	['Merge Overlapping Subintervals', 'https://leetcode.com/problems/merge-intervals/', 'https://youtu.be/2JzRBPFYbKE',
	 'https://www.geeksforgeeks.org/merging-intervals/'],  # sub intervals kaadhu gfg link
	['Find the duplicate in an array of N+1 integers',
	 'https://leetcode.com/problems/find-the-duplicate-number/solution/', 'https://youtu.be/32Ll35mhWg0',
	 'https://www.geeksforgeeks.org/find-duplicates-constant-array-elements-0-n-1-o1-space/'],

	# 					*********************************************************************DAY-2*********************************************************************

	['Set Matrix Zeros', 'https://leetcode.com/problems/set-matrix-zeroes/', 'https://youtu.be/M65xBewcqcI', None],
	['Pascal Triangle', 'https://leetcode.com/problems/pascals-triangle/', 'https://youtu.be/6FLvhQjZqvM',
	 'https://www.geeksforgeeks.org/pascal-triangle/'],
	['Next Permutation', 'https://leetcode.com/problems/next-permutation/', 'https://youtu.be/LuLCLgMElus', None],
	# no gfg link
	['Inversion of Array (Using Merge Sort)',
	 'https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1', 'https://youtu.be/kQ1mJlwW-c0',
	 'https://www.geeksforgeeks.org/counting-inversions/'],
	['Stock Buy and Sell', 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
	 'https://youtu.be/eMSfBgbiEjk', None],
	['Rotate Matrix', 'https://leetcode.com/problems/rotate-image/', 'https://youtu.be/Y72QeX0Efxw', None],

	# 					*********************************************************************DAY-3*********************************************************************

	['Search in a 2D matrix', 'https://leetcode.com/problems/search-a-2d-matrix/', 'https://youtu.be/ZYpYur0znng',
	 'https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/'],
	['Pow(X,n)', 'https://leetcode.com/problems/powx-n/', 'https://youtu.be/l0YC3876qxg', None],
	['Majority Element (>N/2 times)', 'https://leetcode.com/problems/majority-element/', 'https://youtu.be/AoX3BPWNnoE',
	 'https://www.geeksforgeeks.org/majority-element/'],
	['Majority Element (>N/3 times)', 'https://leetcode.com/problems/majority-element-ii/',
	 'https://youtu.be/yDbkQd9t2ig', None],
	['Grid Unique Paths', 'https://leetcode.com/problems/unique-paths/', 'https://youtu.be/t_f0nwwdg5o',
	 'https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/'],
	['Reverse Pairs', 'https://leetcode.com/problems/reverse-pairs/', 'https://youtu.be/S6rsAlj_iB4', None],

	# 					*********************************************************************DAY-4*********************************************************************

	['2 Sum problem', 'https://leetcode.com/problems/two-sum/', 'https://youtu.be/dRUpbt8vHpo',
	 'https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/'],
	['4 Sum problem', 'https://leetcode.com/problems/4sum/', 'https://youtu.be/4ggF3tXIAp0',
	 'https://www.geeksforgeeks.org/find-four-numbers-with-sum-equal-to-given-sum/'],
	# gfg doesnot give all pairs but only gives 1
	['Longest Consecutive Sequence', 'https://leetcode.com/problems/longest-consecutive-sequence/',
	 'https://youtu.be/qgizvmgeyUM', 'https://www.geeksforgeeks.org/longest-consecutive-subsequence/'],
	['Largest Subarray with 0 sum', 'https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1',
	 'https://youtu.be/xmguZ6GbatA', 'https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/'],
	['Count number of subarrays with given XOR', None, 'https://youtu.be/lO9R5CaGRPY',
	 'https://www.geeksforgeeks.org/count-number-subarrays-given-xor/'],
	['Longest substring without repeat',
	 'https://leetcode.com/problems/longest-substring-without-repeating-characters/', 'https://youtu.be/qtVh-XEpsJo',
	 'https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/'],

	# 					*********************************************************************DAY-5*********************************************************************

	['Reverse a LinkedList', 'https://leetcode.com/problems/reverse-linked-list/', 'https://youtu.be/iRtLEoL-r-g',
	 'https://www.geeksforgeeks.org/reverse-a-linked-list/'],
	['Find middle of LinkedList', 'https://leetcode.com/problems/middle-of-the-linked-list/',
	 'https://youtu.be/sGdwSH8RK-o',
	 'https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/'],
	['Merge two sorted Linked List', 'https://leetcode.com/problems/merge-two-sorted-lists/',
	 'https://youtu.be/Xb4slcp1U38', 'https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/'],
	['Remove N-th node from back of LinkedList', 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/',
	 'https://youtu.be/Lhu3MsXZy-Q',
	 'https://www.geeksforgeeks.org/delete-nth-node-from-the-end-of-the-given-linked-list/'],
	['Delete a given Node when a node is given. (0(1) solution)',
	 'https://leetcode.com/problems/delete-node-in-a-linked-list/', 'https://youtu.be/icnp4FJdZ_c',
	 'https://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/'],
	['Add two numbers as LinkedList', 'https://leetcode.com/problems/add-two-numbers/', 'https://youtu.be/LBVsXSMOIk4',
	 'https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/'],

	# 					*********************************************************************DAY-6*********************************************************************

	['Find intersection point of Y LinkedList', 'https://leetcode.com/problems/intersection-of-two-linked-lists/',
	 'https://youtu.be/u4FWXfgS8jw',
	 'https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/'],
	['Detect a cycle in Linked List', 'https://leetcode.com/problems/linked-list-cycle/',
	 'https://youtu.be/354J83hX7RI', 'https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/'],
	['Reverse a LinkedList in groups of size k', 'https://leetcode.com/problems/reverse-nodes-in-k-group/',
	 'https://youtu.be/Of0HPkk3JgI', 'https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/'],
	['Check if a LinkedList is palindrome or not', 'https://leetcode.com/problems/palindrome-linked-list/',
	 'https://youtu.be/-DtNInqFUXs',
	 'https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/'],
	['Find the starting point of the Loop of LinkedList', 'https://leetcode.com/problems/linked-list-cycle-ii/',
	 'https://youtu.be/QfbOhn0WZ88', 'https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/'],
	['Flattening of a LinkedList', 'https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1',
	 'https://youtu.be/ysytSSXpAI0', 'https://www.geeksforgeeks.org/flattening-a-linked-list/'],
	['Rotate a LinkedList', 'https://leetcode.com/problems/rotate-list/description/', 'https://youtu.be/9VPm6nEbVPA',
	 'https://www.geeksforgeeks.org/clockwise-rotation-of-linked-list/'],

	# 					*********************************************************************DAY-7*********************************************************************

	['Clone a Linked List with random and next pointer', 'https://leetcode.com/problems/copy-list-with-random-pointer/',
	 'https://youtu.be/VNf6VynfpdM', 'https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/'],
	['3 Sum', 'https://leetcode.com/problems/3sum/', 'https://youtu.be/onLoX6Nhvmg',
	 'https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/'],
	['Trapping rainwater', 'https://leetcode.com/problems/trapping-rain-water/', 'https://youtu.be/m18Hntz4go8',
	 'https://www.geeksforgeeks.org/trapping-rain-water/'],
	['Remove Duplicate from Sorted array', 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/',
	 'https://youtu.be/Fm_p9lJ4Z_8', 'https://www.geeksforgeeks.org/remove-duplicates-sorted-array/'],
	['Max consecutive ones', 'https://leetcode.com/problems/max-consecutive-ones/', 'https://youtu.be/Mo33MjjMlyA',
	 'https://www.geeksforgeeks.org/maximum-consecutive-ones-or-zeros-in-a-binary-array/'],

	# 					*********************************************************************DAY-8*********************************************************************

	['N meeting in one room', 'https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1',
	 'https://youtu.be/II6ziNnub1Q', 'https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/'],
	['Minimum number of platforms required for a railway',
	 'https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#', 'https://youtu.be/dxVcMDI7vyI',
	 'https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/'],
	['Job sequencing Problem', 'https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#',
	 'https://youtu.be/LjPx4wQaRIs', 'https://www.geeksforgeeks.org/job-sequencing-problem/'],
	['Fractional Knapsack Problem', 'https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1',
	 'https://youtu.be/F_DDzYnxO14', 'https://www.geeksforgeeks.org/fractional-knapsack-problem/'],
	['Greedy algorithm to find minimum number of coins', 'https://practice.geeksforgeeks.org/problems/coin-piles/0',
	 'https://youtu.be/mVg9CfJvayM', 'https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/'],
	['Activity Selection', 'https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1',
	 'https://youtu.be/II6ziNnub1Q', 'https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/'],

	# 					*********************************************************************DAY-9*********************************************************************

	['Subset Sums', 'https://practice.geeksforgeeks.org/problems/subset-sums2234/1', 'https://youtu.be/rYkfBRtMJr8',
	 'https://www.geeksforgeeks.org/print-sums-subsets-given-set/'],
	['Subset-II', 'https://leetcode.com/problems/subsets-ii/', 'https://youtu.be/RIn3gOkbhQE', None],
	['Combination sum-1', 'https://leetcode.com/problems/combination-sum/', 'https://youtu.be/OyZFFqQtu98',
	 'https://www.geeksforgeeks.org/combinational-sum/'],
	['Combination sum-2', 'https://leetcode.com/problems/combination-sum-ii/', None,
	 'https://www.geeksforgeeks.org/all-unique-combinations-whose-sum-equals-to-k/'],
	['Palindrome Partitioning', 'https://leetcode.com/problems/palindrome-partitioning/',
	 'https://youtu.be/WBgsABoClE0', 'https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/'],
	['K-th permutation Sequence', 'https://leetcode.com/problems/permutation-sequence/', 'https://youtu.be/wT7gcXLYoao',
	 'https://www.geeksforgeeks.org/find-the-k-th-permutation-sequence-of-first-n-natural-numbers/'],

	# 					*********************************************************************DAY-10********************************************************************

	['Print all Permutations of a string/array', 'https://leetcode.com/problems/permutations/',
	 'https://youtu.be/f2ic2Rsc9pU',
	 'https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/'],
	['N queens Problem', 'https://leetcode.com/problems/n-queens/', 'https://youtu.be/i05Ju7AftcM',
	 'https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/'],
	['Sudoku Solver', 'https://leetcode.com/problems/sudoku-solver/', 'https://youtu.be/FWAIf_EVUKE',
	 'https://www.geeksforgeeks.org/sudoku-backtracking-7/'],
	['M coloring Problem', 'https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#',
	 'https://youtu.be/wuVwUK25Rfc', 'https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/'],
	['Rat in a Maze', 'https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1',
	 'https://youtu.be/bLGZhJlt4y0', 'https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/'],

	# 					*********************************************************************DAY-11*********************************************************************

	['N-th root of an integer', None, 'https://youtu.be/WjpswYrS2nY',
	 'https://www.geeksforgeeks.org/calculating-n-th-real-root-using-binary-search/'],
	['Matrix Median', 'https://www.interviewbit.com/problems/matrix-median/', 'https://youtu.be/63fPPOdIr2c',
	 'https://www.geeksforgeeks.org/mean-median-matrix/'],
	['Find the element that appears once in sorted array, and rest element appears twice',
	 'https://leetcode.com/problems/single-element-in-a-sorted-array/', 'https://youtu.be/PzszoiY5XMQ',
	 'https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/'],
	['Search element in a sorted and rotated array/ find pivot where it is rotated',
	 'https://leetcode.com/problems/search-in-rotated-sorted-array/', 'https://youtu.be/r3pMQ8-Ad5s',
	 'https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/'],
	['Median of 2 sorted arrays', 'https://leetcode.com/problems/median-of-two-sorted-arrays/',
	 'https://youtu.be/NTop3VTjmxk',
	 'https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/'],
	['K-th element of two sorted arrays',
	 'https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1',
	 'https://youtu.be/nv7F4PiLUzo', 'https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/'],
	['Allocate Minimum Number of Pages', 'https://www.interviewbit.com/problems/allocate-books/',
	 'https://youtu.be/gYmWHvRHu-s', None],
	['Aggressive Cows', None, 'https://youtu.be/wSOfYesTBRk', None],

	# 					*********************************************************************DAY-12*********************************************************************

	['Check if a number is a power of 2 or not in O(1)', 'https://leetcode.com/problems/power-of-two/',
	 'https://youtu.be/4cqHahxFTYw', 'https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/'],
	['Count total set bits', 'https://leetcode.com/problems/counting-bits/', 'https://youtu.be/awxaRgUB4Kw',
	 'https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n/'],
	['Divide Integers without / operator', 'https://leetcode.com/problems/divide-two-integers/',
	 'https://youtu.be/m4L_5qG4vG8', 'https://www.geeksforgeeks.org/division-without-using-operator/'],
	['Power Set', 'https://leetcode.com/problems/subsets/', 'https://youtu.be/b7AYbpM5YrE',
	 'https://www.geeksforgeeks.org/power-set/'],
	['Find MSB in o(1)', None, 'https://youtu.be/2-zmWlM5XSE',
	 'https://www.geeksforgeeks.org/find-significant-set-bit-number/'],
	['Find square of a number without using multiplication or division operators.', None,
	 'https://youtu.be/OIgpvFAew6k',
	 'https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/'],

	# 					*********************************************************************DAY-13*********************************************************************

	['Implement Stack Using Arrays', 'https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1',
	 'https://youtu.be/GYptUgnIM_I', 'https://www.geeksforgeeks.org/stack-data-structure-introduction-program/'],
	['Implement Queue Using Arrays', 'https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1',
	 'https://youtu.be/M6GnoUDpqEE', 'https://www.geeksforgeeks.org/array-implementation-of-queue-simple/'],
	['Implement Stack using Queue (using single queue)', 'https://leetcode.com/problems/implement-stack-using-queues/',
	 'https://youtu.be/jDZQKzEtbYQ', 'https://www.geeksforgeeks.org/implement-stack-using-queue/'],
	['Implement Queue using Stack (0(1) amortised method)',
	 'https://leetcode.com/problems/implement-queue-using-stacks/', 'https://youtu.be/3Et9MrMc02A',
	 'https://www.geeksforgeeks.org/queue-using-stacks/'],
	['Check for balanced parentheses', 'https://leetcode.com/problems/valid-parentheses/', None,
	 'https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/'],
	['Next Greater Element', 'https://leetcode.com/problems/next-greater-element-ii/', 'https://youtu.be/Du881K7Jtk8',
	 'https://www.geeksforgeeks.org/next-greater-element/'],

	# 					*********************************************************************DAY-14*********************************************************************

	['Next Smaller Element', None, 'https://youtu.be/85LWui3FlVk', 'geeksforgeeks.org/next-smaller-element/'],
	['LRU cache', 'https://leetcode.com/problems/lru-cache/', None,
	 'https://www.geeksforgeeks.org/lru-cache-implementation/'],
	['Largest rectangle in histogram', 'https://leetcode.com/problems/largest-rectangle-in-histogram/',
	 'https://youtu.be/vcv3REtIvEo', 'https://www.geeksforgeeks.org/largest-rectangle-under-histogram/'],
	['Sliding Window maximum', 'https://leetcode.com/problems/sliding-window-maximum/', 'https://youtu.be/LiSdD3ljCIE',
	 'https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/'],
	['Implement Min Stack', 'https://leetcode.com/problems/min-stack/', 'https://youtu.be/8UegNFCUQks',
	 'https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/'],
	['Rotten Orange (Using BFS)', 'https://leetcode.com/problems/rotting-oranges/', 'https://youtu.be/CxrnOTUlNJE',
	 'https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/'],

	# 					*********************************************************************DAY-15*********************************************************************

	['Reverse Words in a String', 'https://leetcode.com/problems/reverse-words-in-a-string/',
	 'https://youtu.be/vhnRAaJybpA', 'https://www.geeksforgeeks.org/reverse-words-in-a-given-string/'],
	['Longest Palindrome in a string', 'https://leetcode.com/problems/longest-palindromic-substring/',
	 'https://youtu.be/UflHuQj6MVA', 'https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/'],
	['Roman Number to Integer', 'https://leetcode.com/problems/roman-to-integer/', 'https://youtu.be/dlATMslQ6Uc',
	 'https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/'],
	['Integer to Roman', 'https://leetcode.com/problems/integer-to-roman/', 'https://youtu.be/f_F9ItFyiEg',
	 'https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/'],
	['Implement ATOI/STRSTR', 'https://leetcode.com/problems/string-to-integer-atoi/', 'https://youtu.be/FyTpsuWAoc8',
	 'https://www.geeksforgeeks.org/write-your-own-atoi/'],
	['Longest Common Prefix', 'https://leetcode.com/problems/longest-common-prefix/', 'https://youtu.be/fhyIORFDD0k',
	 'https://www.geeksforgeeks.org/longest-common-prefix-using-character-by-character-matching/'],
	['Rabin Karp', 'https://leetcode.com/problems/implement-strstr', 'https://youtu.be/BQ9E-2umSWc',
	 'https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/'],

	# 					*********************************************************************DAY-16*********************************************************************

	['Prefix Function/Z-Function', 'https://leetcode.com/problems/repeated-substring-pattern/',
	 'https://youtu.be/CpZh4eF8QBw', 'geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/'],
	['KMP algo', 'https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1',
	 'https://youtu.be/V5-7GzOfADQ', 'https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/'],
	['Minimum characters needed to be inserted to make it palindromic',
	 'https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/',
	 'https://youtu.be/AEcRW4ylm_c',
	 'https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/'],
	['Check for Anagrams', 'https://leetcode.com/problems/valid-anagram/', 'https://youtu.be/QZmh8-Auqo8',
	 'https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/'],
	['Count and Say', 'https://leetcode.com/problems/count-and-say/', 'https://youtu.be/-wB1xj-kOe0',
	 'https://www.geeksforgeeks.org/look-and-say-sequence/'],
	['Compare version numbers', 'https://leetcode.com/problems/compare-version-numbers/',
	 'https://youtu.be/MTSetP6kcRI', 'https://www.geeksforgeeks.org/compare-two-version-numbers/'],

	# 					*********************************************************************DAY-17*********************************************************************

	['Inorder Traversal', 'https://leetcode.com/problems/binary-tree-inorder-traversal/',
	 'https://youtu.be/gm8DUJJhmY4', 'https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/'],
	['Preorder Traversal', 'https://leetcode.com/problems/binary-tree-preorder-traversal/',
	 'https://youtu.be/gm8DUJJhmY4', 'https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/'],
	['Postorder Traversal', 'https://leetcode.com/problems/binary-tree-postorder-traversal/',
	 'https://youtu.be/gm8DUJJhmY4', 'https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/'],
	['LeftView Of Binary Tree', 'https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1',
	 'https://youtu.be/bToZH9pGP5Y', 'https://www.geeksforgeeks.org/print-left-view-binary-tree/'],
	['Bottom View of Binary Tree', 'https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1',
	 'https://youtu.be/fPhgtqKdG5k', 'https://www.geeksforgeeks.org/bottom-view-binary-tree/'],
	['Top View of Binary Tree', 'https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1',
	 'https://youtu.be/KXfok9IiVHQ', 'https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/'],

	# 					*********************************************************************DAY-18*********************************************************************

	['Level order Traversal', 'https://leetcode.com/problems/binary-tree-level-order-traversal/',
	 'https://youtu.be/86g8jAQug04', 'https://www.geeksforgeeks.org/level-order-tree-traversal/'],
	['Height of a Binary Tree', 'https://leetcode.com/problems/maximum-depth-of-binary-tree/',
	 'https://youtu.be/_pnqMz5nrRs',
	 'https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/'],
	['Diameter of Binary Tree', 'https://leetcode.com/problems/diameter-of-binary-tree/',
	 'https://youtu.be/zmPj_Ee3B8c', 'https://www.geeksforgeeks.org/diameter-of-a-binary-tree/'],
	['Check if Binary tree is height balanced or not', 'https://leetcode.com/problems/balanced-binary-tree/',
	 'https://youtu.be/LU4fGD-fgJQ', 'https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/'],
	['LCA in Binary Tree', 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/',
	 'https://youtu.be/6POfA8fruxI', 'https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/'],
	['Check if two trees are identical or not', 'https://leetcode.com/problems/same-tree/',
	 'https://youtu.be/kL5Gs1YTwMM',
	 'https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/'],

	# 					*********************************************************************DAY-19*********************************************************************

	['Maximum path sum', 'https://leetcode.com/problems/binary-tree-maximum-path-sum/', 'https://youtu.be/Osz-Vwer6rw',
	 'https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/'],
	['Construct Binary Tree from inorder and preorder',
	 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/',
	 'https://youtu.be/PoBGyrIWisE',
	 'https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/'],
	['Construct Binary Tree from Inorder and Postorder',
	 'https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/',
	 'https://youtu.be/s5XRtcud35E',
	 'https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/'],
	['Symmetric Binary Tree', 'https://leetcode.com/problems/symmetric-tree/', 'https://youtu.be/-5E5Jt_HKLc',
	 'https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/'],
	['Flatten Binary Tree to LinkedList', 'https://leetcode.com/problems/flatten-binary-tree-to-linked-list/',
	 'https://youtu.be/pCtXQ9XI7As', 'https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/'],
	['Check if Binary Tree is mirror of itself or not', 'https://practice.geeksforgeeks.org/problems/symmetric-tree/1',
	 'https://youtu.be/UaZtKuaVNp0',
	 'https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/'],

	# 					*********************************************************************DAY-20*********************************************************************

	['Populate Next Right pointers of Tree',
	 'https://leetcode.com/problems/populating-next-right-pointers-in-each-node/', 'https://youtu.be/yl-fdkyQD8A',
	 'https://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space/'],
	['Search given Key in BST', 'https://leetcode.com/problems/search-in-a-binary-search-tree/',
	 'https://youtu.be/Lr2oxJlnLMM', 'https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/'],
	['Construct BST from given keys.', 'https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/',
	 'https://youtu.be/9sw8RRsBw6s', 'https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/'],
	['Check is a BT is BST or not', 'https://leetcode.com/problems/validate-binary-search-tree/',
	 'https://youtu.be/yEwSGhSsT0U',
	 'https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/'],
	['Find LCA of two nodes in BST', 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/',
	 'https://youtu.be/3MmWkR04n_8', 'https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/'],
	['Find the inorder predecessor/successor of a given Key in BST.',
	 'https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1', 'https://youtu.be/lQIXz5NJYLs',
	 'https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/'],

	# 					*********************************************************************DAY-21*********************************************************************

	['Floor and Ceil in a BST', None, 'https://youtu.be/5cx0xerA8XY',
	 'https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/'],
	['Find K-th smallest element in BST', 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/',
	 'https://youtu.be/KqMm81Y7j9M',
	 'https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/'],
	['Find K-th largest element in BST', 'https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1',
	 'https://youtu.be/KqMm81Y7j9M',
	 'https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/'],
	['Find a pair with a given sum in BST', 'https://leetcode.com/problems/two-sum-iv-input-is-a-bst/',
	 'https://youtu.be/zSg6yfLduro', 'https://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/'],
	['BST iterator', 'https://leetcode.com/problems/binary-search-tree-iterator/', 'https://youtu.be/C8iHdhXjKC4',
	 'https://www.geeksforgeeks.org/implementing-forward-iterator-in-bst/'],
	['Size of the largest BST in a Binary Tree', 'https://practice.geeksforgeeks.org/problems/largest-bst/1',
	 'https://youtu.be/YgC-IXiMrRM', 'https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/'],
	['Serialize and deserialize Binary Tree', 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/',
	 'https://youtu.be/lUnNK9jPg2Y', 'https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/'],

	# 					*********************************************************************DAY-22*********************************************************************

	['Binary Tree to Double Linked List', 'https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1',
	 'https://youtu.be/WVFk9DwRgpY',
	 'https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/'],
	['Find median in a stream of running integers', 'https://leetcode.com/problems/find-median-from-data-stream/',
	 'https://youtu.be/1LkOrc-Le-Y', 'https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/'],
	['K-th largest element in a stream', 'https://leetcode.com/problems/kth-largest-element-in-a-stream/',
	 'https://youtu.be/G5CVOjWDAmY', 'https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/'],
	['Distinct numbers in Window',
	 'https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1',
	 'https://youtu.be/caVVRK1AUXM',
	 'https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/'],
	['K-th largest element in an unsorted array.', 'https://leetcode.com/problems/kth-largest-element-in-an-array/',
	 'https://youtu.be/aXJ-p3Qa4TY', 'https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/'],
	['Flood-fill Algorithm', 'https://leetcode.com/problems/flood-fill/', 'https://youtu.be/RwozX--B_Xs',
	 'https://www.geeksforgeeks.org/flood-fill-algorithm/'],

	# 					*********************************************************************DAY-23*********************************************************************

	['Clone a graph', 'https://leetcode.com/problems/clone-graph/', 'https://youtu.be/f2EfGComRKM',
	 'https://www.geeksforgeeks.org/clone-an-undirected-graph/'],
	['DFS', 'https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1',
	 'https://youtu.be/9RHO6jU--GU', 'https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/'],
	['BFS', 'https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1', 'https://youtu.be/9RHO6jU--GU',
	 'https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/'],
	['Detect A cycle in Undirected Graph',
	 'https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1',
	 'https://youtu.be/L0DcePeWHnM', 'https://www.geeksforgeeks.org/detect-cycle-undirected-graph/'],
	['Detect A cycle in directed Graph',
	 'https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1', 'https://youtu.be/0dJmTuMrUZM',
	 'https://www.geeksforgeeks.org/detect-cycle-in-a-graph/'],
	['Topo Sort', 'https://practice.geeksforgeeks.org/problems/topological-sort/1', 'https://youtu.be/dis_c84ejhQ',
	 'https://www.geeksforgeeks.org/topological-sorting/'],
	['Number of islands', 'https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1/',
	 'https://youtu.be/__98uL6wst8', 'https://www.geeksforgeeks.org/find-number-of-islands/'],
	['Bipartite Check', 'https://leetcode.com/problems/is-graph-bipartite/', 'https://youtu.be/0ACfAqs8mm0',
	 'https://www.geeksforgeeks.org/bipartite-graph/'],

	# 					*********************************************************************DAY-24*********************************************************************

	['SCC', None, 'https://youtu.be/V8qIqJxCioo', 'https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/'],
	['Djisktra’s Algorithm', 'https://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0',
	 'https://youtu.be/smHnz2RHJBY', 'https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/'],
	['Bellman Ford Algo', 'https://practice.geeksforgeeks.org/problems/negative-weight-cycle/0',
	 'https://youtu.be/KudAWAMiQog', 'https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/'],
	['Floyd Warshall Algorithm', 'https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0',
	 'https://youtu.be/Gc4mWrmJBsw', 'https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/'],
	['MST using Prim’s Algo', 'https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1',
	 'https://youtu.be/ZtZaR7EcI5Y', 'https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/'],
	['MST using Kruskal’s Algo',
	 'https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree',
	 'https://youtu.be/EjVHtpWkIho',
	 'https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/'],

	# 					*********************************************************************DAY-25*********************************************************************

	['Max Product Subarray', 'https://leetcode.com/problems/maximum-product-subarray/', 'https://youtu.be/hJ_Uy2DzE08',
	 'https://www.geeksforgeeks.org/maximum-product-subarray/'],
	['Longest Increasing Subsequence', 'https://leetcode.com/problems/longest-increasing-subsequence/',
	 'https://youtu.be/mouCn3CFpgg', 'https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/'],
	['Longest Common Subsequence', 'https://leetcode.com/problems/longest-common-subsequence/',
	 'https://youtu.be/jHGgXV27qtk', 'https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/'],
	['0-1 Knapsack', 'https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0',
	 'https://youtu.be/PfkBS9qIMRE', 'https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/'],
	['Edit Distance', 'https://leetcode.com/problems/edit-distance/', 'https://youtu.be/AuYujVj646Q',
	 'https://www.geeksforgeeks.org/edit-distance-dp-5/'],
	['Maximum sum increasing subsequence', 'https://leetcode.com/problems/longest-continuous-increasing-subsequence/',
	 'https://youtu.be/R7DrJsTkK8w', 'https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/'],
	['Matrix Chain Multiplication', 'https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication/0',
	 'https://youtu.be/XrB_MWPjHHc', 'https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/'],

	# 					*********************************************************************DAY-26(DP)*********************************************************************

	['Maximum sum path in matrix', None, 'https://youtu.be/OCz6rm9Nh1o',
	 'https://www.geeksforgeeks.org/maximum-sum-path-in-a-matrix/'],
	['Coin change', 'https://leetcode.com/problems/coin-change/', 'https://youtu.be/L27_JpN6Z1Q',
	 'https://www.geeksforgeeks.org/coin-change-dp-7/'],
	['Subset Sum', 'https://practice.geeksforgeeks.org/problems/subset-sum-problem/0', 'https://youtu.be/dJmyfFC3-3A',
	 'https://www.geeksforgeeks.org/subset-sum-problem-dp-25/'],
	['Rod Cutting', 'https://practice.geeksforgeeks.org/problems/cutted-segments/0', 'https://youtu.be/SZqAQLjDsag',
	 'https://www.geeksforgeeks.org/cutting-a-rod-dp-13/'],
	['Egg Dropping', 'https://leetcode.com/problems/super-egg-drop/', 'https://youtu.be/KVfxgpI3Tv0',
	 'https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/'],
	['Word Break', 'https://leetcode.com/problems/word-break/', 'https://youtu.be/yr77dVf1RQA',
	 'https://www.geeksforgeeks.org/word-break-problem-dp-32/'],
	['Palindrome Partitioning (MCM Variation)', 'https://leetcode.com/problems/palindrome-partitioning-ii/',
	 'https://youtu.be/WPr1jDh3bUQ', 'https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/'],
	['Maximum profit in Job scheduling', 'https://leetcode.com/problems/maximum-profit-in-job-scheduling/',
	 'https://youtu.be/XJp-aOn35y4', 'https://www.geeksforgeeks.org/weighted-job-scheduling/']
]


def create_questions(user,questions_list):
	try:
		objs=[questions(user=user,ques=obj[0],ques_link=obj[1],video=obj[2],gfg=obj[3],status=False) for obj in questions_list]
		print(objs)
		questions.objects.bulk_create(objs)
		return True
	except:
		return False


