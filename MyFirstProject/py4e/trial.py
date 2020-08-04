
A = int(input('Enter the \# of elements:'))
a = []
for i in range(A):
  ele = int(input('Enter the elements:').strip())
  a.append(ele)

#check if repeated element is met
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
tmp = 0
for k,v in d.items():
    if v > 1 and v > tmp :
        tmp = v
        key = k

b=[]
if tmp > 0:
    #when there is repeated element
    for i in a:
        if i%2 != 0:
            i = i + 3
            b.append(i)
        else: b.append(i)
    print('new list b is:', b)
    print('sorted b:', sorted(b))
    print(':'.join(map(str, sorted(b))))
else:
    #when there is no repeated element
    print('a is:', a)
    print('sorted a:', sorted(a))
    print(':'.join(map(str, sorted(a))))
