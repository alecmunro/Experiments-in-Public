'''
Created on 2011-09-16

@author: Alec
'''

def bubble_sort(items):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
    
if __name__ == "__main__":
    from timeit import Timer
    t = Timer('bubble_sort(list("eqionvnmvjkclwjklcpwaxctwa"))', 
              "from __main__ import bubble_sort")
    my_time = t.timeit(number=10000)
    t_2 = Timer('sorted(list("eqionvnmvjkclwjklcpwaxctwa"))')
    py_time = t_2.timeit(number=10000)
    print("My sort takes {0} times as long.".format(my_time / py_time))