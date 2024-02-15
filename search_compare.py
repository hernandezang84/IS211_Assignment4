import time
import random

def sequential_search(lst, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos = pos + 1


    end_time = time.time()
    elapsed_time = end_time - start_time
    return found, elapsed_time

def ordered_sequential_search(lst, item):
    lst.sort()
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(lst) and not found and not stop:
        if lst[pos] == item:
            found = True
        else:
            if lst[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    return found, elapsed_time

def binary_search_iterative(lst, item):
    lst.sort()
    start_time = time.time()
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    return found, elapsed_time

def binary_search_recursive(lst, item):
    lst.sort()
    start_time = time.time()
    if len(lst) == 0:
        found = False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                return binary_search_recursive(lst[:midpoint], item)
            else:
                return binary_search_recursive(lst[midpoint + 1:], item)
            
    end_time = time.time()
    elapsed_time = end_time - start_time
    return found, elapsed_time

def main():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        total_time_seq = 0
        total_time_ord_seq = 0
        total_time_bin_iter = 0
        total_time_bin_rec = 0
        for _ in range(100):
            lst = [random.randit(1, 1000000) for _ in range(size)]
            _, time_taken = sequential_search(lst, 99999999)
            total_time_seq += time_taken
            _, time_taken = ordered_sequential_search(lst, 99999999)
            total_time_ord_seq += time_taken
            _, time_taken = binary_search_iterative(lst, 99999999)
            total_time_bin_iter += time_taken
            _, time_taken = binary_search_recursive(lst, 99999999)
            total_time_bin_rec += time_taken

        print(f"Sequential Search took {total_time_seq / 100:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_time_ord_seq / 100:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {total_time_bin_iter / 100:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {total_time_bin_rec / 100:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()