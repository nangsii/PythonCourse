# # my_list = [3, 6, 1, 9, 5]

# # # 1. create a function to swap two elements in a list
# # # input list: [3, 5]
# # # output list: [5, 3]
# def my_swap(my_list):
#     y = my_list[0]
#     my_list[0] = my_list[1]
#     my_list[1] = y
#     return my_list
    
# swap_test = [3, 5]
# result_after_swap = my_swap(swap_test)
# print(result_after_swap)

# # # 2. find the max element in a list 
# # # output int:9
# # def my_max(my_list):
# #     my_list = [3, 9, 5]

     
# def my_max(my_list):
#   maxnum = my_list[0]  
#   for x in my_list:
#     if x > maxnum:
#       maxnum = x
#   return maxnum


# list_test = [3, 9, 5]
# result_my_max = my_max(list_test)
# print(result_my_max)
    
   
    


# 3. find the nth max element in a list 
# input list: [3, 9, 5] with nth_max = 1
# output int: 9
# input list: [3, 9, 5] with nth_max = 2
# output int: 5


# def nth_max(my_list, n):
#     count = 0
#     # extend the life scope of the variable
#     nth_max
#     while count < n:
#         count = count + 1
#         nth_max = my_list[0]
#         for x in my_list:
#             if x > nth_max:
#                 nth_max = x        
#         my_list.remove(nth_max)
#     return nth_max    
            
# my_list = [3, -5, -2, -2000, -150] 
# n = 2
# result_nth_max = nth_max(my_list, n)
# print(result_nth_max)

# option 2 move the nth_max to my_list[0]



# 4. sort the list in ascending order
# input list : [3, 6, 1, 9, 5]
# output list: [1, 3, 5, 6, 9]

def my_sort(my_list):
    innitial_lenth = len(my_list)
    count = 0
    new_list = []
    while count < innitial_lenth:
        count = count + 1
        min_num = my_list[0]
        for x in my_list:
            if x < min_num: 
                min_num = x  
        new_list.append(min_num)
        my_list.remove(min_num)       
    return new_list
        
# test_list = [3, 6, 1, 9, 5, 4, 8, 10, -1, -4, 0,-500, 993456, 9, 3, 9]
test_list = [3]
result_my_sort =  my_sort(test_list)
print(result_my_sort)