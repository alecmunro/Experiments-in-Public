'''
Created on 2011-09-17

@author: Alec
'''

def insertion_sort(items):
    sorted_items = [items.pop()]
    while items:
        item = items.pop()
        for index, sorted_item in enumerate(sorted_items):
            if item < sorted_item:
                sorted_items.insert(index, item)
                break
        else:
            sorted_items.append(item)
                
    return sorted_items

if __name__ == "__main__":
    from timeit import Timer
    t = Timer('insertion_sort(list("eqionvnmvjkclwjklcpwaxctwa"))', 
              "from __main__ import insertion_sort")
    my_time = t.timeit(number=10000)
    t_2 = Timer('sorted(list("eqionvnmvjkclwjklcpwaxctwa"))')
    py_time = t_2.timeit(number=10000)
    print("My sort takes {0} times as long.".format(my_time / py_time))