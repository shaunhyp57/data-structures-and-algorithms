# O(n^2) solution using nested loops
# sample array: [2,3,4,5]
def two_sums_naive(arr, n):
  
  i = 0
  j = 0

  len_arr = len(arr)
  while i < len_arr:
    j = i+1
    while j < len_arr:
      if (n - arr[i] == arr[j]):
        return [i,j]
      j += 1
    i += 1

  print("not found")

#O(n) solution using dictionaries
def two_sums(arr, n):
  pair_n = {}

  for num in arr:
    if n-num in pair_n:
      return num, n-num
    else:
      pair_n[num] = True
  
  print("not found")
