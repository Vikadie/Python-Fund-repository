command = input()

store_list = []
items_per_store_index = []

while(command != "END"):

    commands_list = command.split('->')

    if commands_list[0] == 'Add':
        store, items = commands_list[1], commands_list[2]
        item_list = items.split(',')
        if store not in store_list:
            store_list.append(store)
            items_per_store_index.append(item_list)
        else:
            index = store_list.index(store)
            for item in item_list:
                items_per_store_index[index].append(item)

    elif commands_list[0] == 'Remove':
        if commands_list[1] in store_list:
            index = store_list.index(commands_list[1])
            del store_list[index]
            del items_per_store_index[index]

    command = input()

print("Stores list:")

zipped_before_sort = list(zip(store_list, items_per_store_index))
# print(zipped_before_sort)
zipped_list = sorted(zipped_before_sort, key = lambda x: x[0], reverse = True)
# print(zipped_list)
# print("="*30)
for items in sorted(zipped_list, key= lambda items : len(items[1]), reverse = True):
    print(items[0])
    for item in items[1]:
        print(f"<<{item}>>")

# print(zipped_list)