input_line = input()

for index_emoticon in range(len(input_line)):
    if input_line[index_emoticon] == ":" and  not input_line[index_emoticon + 1].isspace():
        print(input_line[index_emoticon : index_emoticon + 2])