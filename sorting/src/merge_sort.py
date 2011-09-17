def merge(list_1, list_2):
    new_list = []
    iter_1 = iter_2 = 0
    left = list_1[iter_1]
    right = list_2[iter_2]
    while len(new_list) < (len(list_1) + len(list_2)):
        if left <= right:
            new_list.append(left)
            iter_1 += 1
            if iter_1 < len(list_1):
                left = list_1[iter_1]
            else:
                new_list.extend(list_2[iter_2:])
                break
        else:
            new_list.append(right)
            iter_2 += 1
            if iter_2 < len(list_2):
                right = list_2[iter_2]
            else:
                new_list.extend(list_1[iter_1:])
                
    return new_list

def merge_sort(items):
    if len(items) < 2:
        return items
    middle = int(len(items) / 2)
    left, right = items[:middle], items[middle:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    merged = merge(left_sorted, right_sorted)
    return merged
    

if __name__ == "__main__":
    from timeit import Timer
    t = Timer('merge_sort("eqionvnmvjkclwjklcpwaxctwa")', 
              "from __main__ import merge_sort, merge")
    my_time = t.timeit(number=10000)
    t_2 = Timer('sorted(list("eqionvnmvjkclwjklcpwaxctwa"))')
    py_time = t_2.timeit(number=10000)
    print("My sort takes {0} times as long.".format(my_time / py_time))
