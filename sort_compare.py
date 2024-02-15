import time
import random

def insertion_sort(lst):
    start_time = time.time()
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position = position - 1
        lst[position] = current_value
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def shell_sort(lst):
    start_time = time.time()
    sublist_count = len(lst) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(lst, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_value = lst[i]
        position = i
        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position = position - gap
        lst[position] = current_value

def python_sort(lst):
    start_time = time.time()
    lst.sort()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def main():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python = 0
        for _ in range (100):
            lst = [random.randint(1, 1000000) for _ in range(size)]
            total_time_insertion += insertion_sort(lst)
            total_time_shell += shell_sort(lst)
            total_time_python += python_sort(lst)
        print(f"Insertion Sort took {total_time_insertion / 100:10.7f} seconds to run, on average")
        print(f"Shell sort tool {total_time_shell / 100:10.7f} seconds to run, on average")
        print(f"Python Sort took {total_time_python / 100:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()