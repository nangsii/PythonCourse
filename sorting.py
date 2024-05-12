my_list = [3, 6, 1, 9, 5]

# 1. create a function to swap two elements in a list
# input list: [3, 5]
# output list: [5, 3]
def my_swap(my_list):
    y = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = y
    return my_list
    
swap_test = [3, 5]
result_after_swap = my_swap(swap_test)
print(result_after_swap)

# 2. find the max element in a list 
# output int:9
def my_max(my_list):
    my_list = [3, 9, 5]

        
my_list = [3, 9, 5]

maxnum = my_list[0]
for x in my_list:
  if x > maxnum:
    maxnum = x
print(maxnum)
    
   
    


# 3. find the nth max element in a list 
# input list: [3, 9, 5] with nth_max = 1
# output int: 9
# input list: [3, 9, 5] with nth_max = 2
# output int: 5
my_list = [3, 9, 5] 
#2
nth_max = my_list[0]
for x in my_list:
  if x > nth_max:
    nth_max = x
    
print()


def my_nth_max(my_list, nth_max):
    pass

# 4. sort the list in ascending order
# input list : [3, 6, 1, 9, 5]
# output list: [1, 3, 5, 6, 9]
def my_sort(my_list):
    for x in my_list:
        print(x)
