# Selectin Sort

music_dict = {
    'Radioned' : 156,
    'Kishore Kumar': 141,
    'The Black Eye': 35,
    'Neutral Milk Hotel': 94,
    'Beck': 88,
    'The Strikes': 61
}

print(music_dict)

# music_arr = music_dict.values[0]

# Get the first value of the dictionary
first_value = next(iter(music_dict.values()))

# Get the second value of the dictionary
second_value = list(music_dict.values())[1]
third_value = list(music_dict.values())[2]

print(first_value)
print(second_value)
print(third_value)

# sorting

music_list = list(music_dict.values())
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

music_list_sorted = selection_sort(music_list)
print(music_list_sorted)
