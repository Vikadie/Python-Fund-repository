exam_h = int(input())
exam_min = int(input())
arrival_h = int(input())
arrival_min = int(input())

# transform both times in minutes
arrival_time = arrival_h * 60 + arrival_min
exam_time = exam_h * 60 + exam_min

diff_minutes = arrival_time - exam_time

# working on the first line
state = 'Early'
if diff_minutes > 0:
    state = 'Late'
elif diff_minutes >= -30:
    state = 'On time'

# working on the second line (explanation_text)
explanation_text = ''
if diff_minutes != 0:
    hour_diff = abs(diff_minutes) // 60
    minutes_diff = abs(diff_minutes) % 60

    # printing the time
    if hour_diff > 0:
        if minutes_diff < 10:
            explanation_text = f'{hour_diff}:0{minutes_diff} hours'
        else:
            explanation_text = f'{hour_diff}:{minutes_diff} hours'
    else:
        explanation_text = f'{minutes_diff} minutes'

    # addition of the 'before/after' sentence
    if diff_minutes < 0:
        explanation_text += ' before the start'
    elif diff_minutes > 0:
        explanation_text += ' after the start'

print(state)
if explanation_text:
    print(explanation_text)