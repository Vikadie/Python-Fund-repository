n = int(input())

bracket = []
unbalanced = 0
for i in range(n):
    inp = input()
    if inp == ')' :
        if len(bracket) > 0 and bracket[-1] == '(':
            bracket.pop()
        else:
            unbalanced = 1
    if inp == '(' :
        if len(bracket) == 0:
            bracket.append(inp)
        else:
            unbalanced = 1


if unbalanced:
    print("UNBALANCED")
else:
    print("BALANCED")