side_size = float(input())
number_paper_sheets = int(input())
area_covered_by_sheet = float(input())

area_of_box = side_size * side_size * 6

area_covered = 0
for sheet in range(1, number_paper_sheets + 1):
    if sheet % 3 == 0:
        area_covered += area_covered_by_sheet * 0.25
    else:
        area_covered += area_covered_by_sheet

percentage = 100 * area_covered / area_of_box

print(f"You can cover {percentage:.2f}% of the box.")