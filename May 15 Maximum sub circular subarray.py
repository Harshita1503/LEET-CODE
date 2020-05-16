'''Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.'''






def maxCircularSum(a): 
  
    n = len(a) 
  
    # Case 1: get the maximum sum using standard kadane's 
    # algorithm 
    max_kadane = kadane(a) 
  
    # Case 2: Now find the maximum sum that includes corner 
    # elements. 
    max_wrap = 0
    for i in range(0,n): 
        max_wrap += a[i] 
        a[i] = -a[i] 
  
    # Max sum with corner elements will be: 
    # array-sum - (-max subarray sum of inverted array) 
    max_wrap = max_wrap + kadane(a) 
  
    # The maximum circular sum will be maximum of two sums 
    if max_wrap > max_kadane: 
        return max_wrap 
    else: 
        return max_kadane
