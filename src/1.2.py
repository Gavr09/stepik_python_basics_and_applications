def compare_elements(obj, list_with_diff_obj):
    ans = False
    for obj2 in list_with_diff_obj:
        if id(obj) == id(obj2):
            ans = True

    return ans

def calc_num_of_diff_elem(objects):
    list_with_diff_obj = []
    for obj in objects:
        if compare_elements(obj, list_with_diff_obj) == False:
            list_with_diff_obj.append(obj)
    # print(list_with_diff_obj)
    print(len(list_with_diff_obj))

# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]] # 9
objects = [1, [1, 2]]
calc_num_of_diff_elem(objects)