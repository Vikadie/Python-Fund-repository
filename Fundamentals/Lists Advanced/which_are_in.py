list1 = input().split(', ')
list2 = input()

new_list = []
# for word1 in list1:
#     for word2 in list2:
#         if word1 in word2 and word1 not in new_list:
#             new_list.append(word1)
new_list = [word for word in list1 if word in list2]


print(new_list)