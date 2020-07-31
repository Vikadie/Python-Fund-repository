from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(fracs)
    print(result)
    print(*result)
    print(*product(fracs))
# def fun(s):
#     # return True if s is a valid email, else return False
#     if '@' in s:
#         l = s.split('@')
#         if len(l) > 2:
#             return (False)
#         if l[0]:
#             for i in l[0]:
#                 if not i.isalnum() and i not in '_-':
#                     return (False)
#         else:
#             return(False)
#         if '.' in l[1]:
#             mail = l[1].split('.')
#             if len(mail) > 2 or len(mail[1]) > 3 or len(mail[1]) == 0:
#                 return (False)
#             if not mail[0].isalnum():
#                 return (False)
#         else:
#             return(False)
#         return (True)
#     else:
#         return (False)
#
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)