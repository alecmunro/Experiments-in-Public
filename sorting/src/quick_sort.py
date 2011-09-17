'''
Created on 2011-09-17

@author: Alec
'''

def quick_sort(items):
    pivot_point = len(items) // 2
    if not pivot_point:
        return items
    pivot = items.pop(pivot_point)
    more = []
    less = []
    for item in items:
        (more if item > pivot else less).append(item)
    return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == "__main__":
    from timeit import Timer
    t = Timer('quick_sort(list("eqionvnmvjkclwjklcpwaxctwa"))', 
              "from __main__ import quick_sort")
    my_time = t.timeit(number=10000)
    t_2 = Timer('sorted(list("eqionvnmvjkclwjklcpwaxctwa"))')
    py_time = t_2.timeit(number=10000)
    print("My sort takes {0} times as long.".format(my_time / py_time))