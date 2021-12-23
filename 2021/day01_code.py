with open('day01_input.txt', 'r') as f:
    lines = f.readlines()
    depths_array = [int(line) for line in lines]

# Part I
increased_depth_count = 0
for index, depth in enumerate(depths_array):
    if index == len(depths_array) - 1:
        break
    curr_depth = depths_array[index]
    next_depth = depths_array[index+1]
    if curr_depth < next_depth:
        increased_depth_count += 1
print(f'[!!] Sonar detected "{increased_depth_count}" depths that increased')


# Part II
def get_sum_window(start_index, depths_array):
    return depths_array[start_index] + depths_array[start_index+1] + depths_array[start_index+2]


increased_depth_count = 0
for index, depth in enumerate(depths_array):
    if index + 3 == len(depths_array):
        break
    curr_depth_sum = get_sum_window(index, depths_array)
    next_depth_sum = get_sum_window(index+1, depths_array)
    has_increased = curr_depth_sum < next_depth_sum
    if has_increased:
        increased_depth_count += 1
    print(f'[!!] {curr_depth_sum} vs {next_depth_sum}: {has_increased}')
print(f'[!!] Sonar detected "{increased_depth_count}" depths that increased')
