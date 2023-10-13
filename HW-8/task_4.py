result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

dict_char = dict.fromkeys(set(result_link), 0)

for char in range(len(result_link)):
    dict_char[result_link[char]] += 1

print(dict_char)
