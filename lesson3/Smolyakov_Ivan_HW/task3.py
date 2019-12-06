initial_list = [ int(i) for i in input().split()]
sum_list = []

left_index = -1
right_index = -len(initial_list) + 1
middle_index = 0

while middle_index < len(initial_list):
    sum_list.append(initial_list[left_index] + initial_list[right_index])
    left_index += 1
    right_index += 1
    middle_index += 1

print(sum_list)
