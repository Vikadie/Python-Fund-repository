income = float(input())
aver_score = float(input())
min_salary = float(input())

from math import floor

#scolarship s1 for aver_score, s2 for income < min_salary
s1, s2 = 0, 0

if aver_score >= 5.5:
    s1 = aver_score * 25
if (income < min_salary) and (aver_score >= 4.5):
    s2 = min_salary * 0.35

if s1 >= s2 and s1 != 0:  # s1 != s2 != 0
    print(f"You get a scholarship for excellent results {floor(s1)} BGN")
elif s1 < s2:
    print(f"You get a Social scholarship {floor(s2)} BGN")
else:
    print("You cannot get a scholarship!")