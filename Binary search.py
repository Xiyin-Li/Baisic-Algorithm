def binary_search(List,target):
    # The List argument must be a sorted list
    first_index = 0
    last_index = len(List)
    while (last_index > first_index +1) or last_index == first_index:
        middle_index = (last_index + first_index) //2
        if target == List[middle_index]:
            return True

        elif target > List[middle_index]:
            first_index = middle_index
            
        else:
            last_index = middle_index
            
    return False
    
List = [2,4,6,8,10,12,14,16,18,20]
print(binary_search(List, 15))
print(binary_search(List, 8))
