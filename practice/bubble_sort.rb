## Bubble Sort Practice
## Making repeated passes through an array until fully sorted. One pass involves looping through each array index,
## comparing the value at index to the value at the next index. Swapping the two elements if they are out of order.
## The array is sorted when in a single pass you have not swapped any items.

## 1. Write the sort algorithm
## 2. Explain/prove why the condition "no swaps were made this pass" is sufficient to know you don't need another pass.
##  a) You only need one pass with Bubble Sort to ensure order because the algorithm will only swap items if it finds that a value is greater than the number adjacent.
##  If the algorithm makes it through a pass without swapping you imagine that 'checking' pass alternatively as a long list of less than comparisons joined by "AND" operators.
##  i.e.: Where 'a' is an array with 'n' items: (a0 < a1 && a1 < a2 && a2 < a3 ... && an-1 < an) == true
## 3. Algorithmic Performance:
##  a) For an array of size n that is badly sorted (complete reverse order):
##     how many comparisons are needed (n, log(n), n*log(n), n^2, 2^n) to finish the sort and why?
##      O(n^2), if every number is out of its correct position, the sort will need to pass through the array for every out of order number.
##      That means the sort algorithm will make n(out of order numbers) x n(items to check in the array for each pass) = n^2
##  b) What if the array is already sorted?:
##      O(n), it takes one pass through the array to ensure that all items in the array are sorted
##  c) Only one element out of order?:
##      O(2n), it takes two passes through the array to ensure sorting.
##      Once to 'bubble' the out-of-order number to its correct position, and another pass to ensure the array is sorted.

[4,3,2,1]


def bubble_sort!(arr)
    begin
        ii = 0
        swapped = false
        arr.each do |item|
            if arr[ii+1] && item > arr[ii+1]
                ## swap
                temp = item
                arr[ii] = arr[ii+1]
                arr[ii+1] = temp
                swapped = true
            end
            ii+=1
        end
    end while swapped
    arr
end

a = *(1..100)
a.shuffle!
puts "unsorted: #{a}"
bubble_sort!(a)
puts "sorted: #{sorted_array}"
