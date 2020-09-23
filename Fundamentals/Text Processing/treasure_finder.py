keys = list(map(int, input().split()))

line = input()

while line != "find":
    decoded = ""
    count,index = 0, 0
    for ch in line:
        if count % len(keys) == 0:
            index = 0
        decoded += chr(ord(ch) - keys[index])
        count += 1
        index += 1

    decoded = decoded.split("&")
    at_coordinate = decoded[2]
    start_index = at_coordinate.index("<") + 1
    end_index = at_coordinate.index(">")
    coordinate = at_coordinate[start_index: end_index]
    print(f"Found {decoded[1]} at {coordinate}")
    line = input()
