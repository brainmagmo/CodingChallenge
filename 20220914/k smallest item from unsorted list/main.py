#author: trevor kleinstuber
# written on Online Python - IDE, Editor, Compiler, Interpreter

def k_biggest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
    
#actually less efficient
def k_biggest_optimise(arr, k):
    l = len(arr)
    if k < 1 or k > l:
        raise IndexError
    if l == 1:
        return arr[0]
    bigs = [float('-inf')] * k
    t = 0
    while(t < l):
        test = arr[t]
        insert_sorted_small_to_big(bigs, test)
        t = t+1
    return bigs[0]

def insert_sorted_small_to_big(arr, num):
    for i in range(len(arr)):
        #print(f'arr:{arr}, i:{i}, num:{num}')
        if num <= arr[i]:
            break
        else:
            if i > 0:
                arr[i-1] = arr[i]
                arr[i] = num
            else:
                arr[0] = num
    
    
arr_test = [10, 100, 1, 1000, -1, 50, 33, 66, 77]
print(f"1-th biggest input is {k_biggest_optimise(arr_test, 1)} [correct answer:{k_biggest(arr_test, 1)}]")
print(f"2-th biggest input is {k_biggest_optimise(arr_test, 2)} [correct answer:{k_biggest(arr_test, 2)}]")
print(f"3-th biggest input is {k_biggest_optimise(arr_test, 3)} [correct answer:{k_biggest(arr_test, 3)}]")
print(f"4-th biggest input is {k_biggest_optimise(arr_test, 4)} [correct answer:{k_biggest(arr_test, 4)}]")
print(f"5-th biggest input is {k_biggest_optimise(arr_test, 5)} [correct answer:{k_biggest(arr_test, 5)}]")
print(f"6-th biggest input is {k_biggest_optimise(arr_test, 6)} [correct answer:{k_biggest(arr_test, 6)}]")
print(f"7-th biggest input is {k_biggest_optimise(arr_test, 7)} [correct answer:{k_biggest(arr_test, 7)}]")
print(f"8-th biggest input is {k_biggest_optimise(arr_test, 8)} [correct answer:{k_biggest(arr_test, 8)}]")
print(f"9-th biggest input is {k_biggest_optimise(arr_test, 9)} [correct answer:{k_biggest(arr_test, 9)}]")


