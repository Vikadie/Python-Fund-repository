line_1 = list(map(int, input().split()))
line_2 = list(map(int, input().split()))
line_3 = list(map(int, input().split()))

draw = 1
# for first player
# for horizontal and diags
if (line_1.count(1) == 3 or line_3.count(1) == 3 or line_2.count(1) == 3 or
        line_1[0] == line_2[1] == line_3[2] == 1 or
        line_1[2] == line_2[1] == line_3[0] == 1):
    print("First player won")
    draw = 0
elif (sum(line_1) == 6 or sum(line_3) == 6 or sum(line_2) == 6 or
      (line_1[0] + line_2[1] + line_3[2] == 6) or
      (line_1[2] + line_2[2] + line_3[0] == 6)):
    print("Second player won")
    draw = 0
# for vertical
if draw:
    for i in [0, 1, 2]:
        if line_1[i] == line_2[i] == line_3[i] == 1:
            print("First player won")
            draw = 0
            break
        elif line_1[i] + line_2[i] + line_3[i] == 6:
            print("Second player won")
            draw = 0
            break
if draw:
    print("Draw!")
