def quick_sort(a_list):
    if len(a_list) <= 1: return a_list
    temp = a_list[0]
    return quick_sort([i for i in a_list[1:] if i<temp]) + [temp] + quick_sort([i for i in a_list[1:] if i>=temp])


if __name__ == "__main__":
    print quick_sort([2, 5, 6, 8, 7])
