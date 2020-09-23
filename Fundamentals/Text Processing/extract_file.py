input_path = input().split('\\')

print(f"File name: {input_path[-1].split('.')[0]}")
print(f"File extension: {input_path[-1].split('.')[-1]}")