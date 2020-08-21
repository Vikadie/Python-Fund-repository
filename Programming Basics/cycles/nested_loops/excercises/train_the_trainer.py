count_jury = int(input())
presentation_name = input()

total_score = 0
pres_count = 1

while presentation_name != 'Finish':
    pres_score = 0
    for each_jury in range(count_jury):
        score = float(input())
        pres_score += score
    print(f'{presentation_name} - {(pres_score / count_jury):.2f}.')

    total_score += pres_score
    presentation_name = input()
    if presentation_name != 'Finish':
        pres_count += 1

print(f"Student's final assessment is {(total_score / (pres_count * count_jury)):.2f}.")