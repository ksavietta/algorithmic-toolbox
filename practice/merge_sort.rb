## Merge Sort
def merge_sort(arr)
  return arr if arr.length <= 1
  arr_len = arr.length
  mid = arr_len.to_i/2
  ## divide given array into two
  left_arr = arr.slice(0..mid)
  right_arr = arr.slice(mid+1..arr_len)
  ## recursively split arrays into arrays of one item and then recombine
  left_arr = merge_sort(left_arr)
  right_arr = merge_sort(right_arr)

  merge(left_arr, right_arr)
end

def merge(arr1, arr2)
  merged_arr = []
  ## there are numbers in each array to compare to each other
  while arr1.length > 0 && arr2.length > 0
    ## take smallest number from front of each array and add it to merged_arr
    ## remove number from comparison arrays to prevent infinte loop
    num = arr1.first < arr2.first ? arr1.shift : arr2.shift
    merged_arr << num
  end

  ## since we've broken out of the first while loop, we know that at least one array has zero items
  ## and that we don't need to compare the two arrays anymore
  ## arr1 has numbers left
  while arr1.length > 0
    merged_arr << arr1.shift
  end
  ## arr2 has numbers left
  while arr2.length > 0
    merged_arr << arr2.shift
  end
  merged_arr
end

a = *(1..100)
a.shuffle!
puts "unsorted: #{a}"
merge_sort(a)
puts "sorted: #{a}"
