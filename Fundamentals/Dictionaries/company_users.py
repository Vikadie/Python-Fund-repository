c = dict() # {company_name : [employee_ids]

inp = input()

while inp != 'End':
    company_name, employee_id = inp.split(' -> ')
    if company_name in c:
        if employee_id not in c[company_name]:
            c[company_name].append(employee_id)
    else:
        c[company_name] = [employee_id]

    inp =  input()

c = dict(sorted(c.items(), key = lambda x: x[0]))

for k, v in c.items():
    print(k)
    for id in v:
        print(f"-- {id}")

