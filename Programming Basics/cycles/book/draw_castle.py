n = int(input())

colsize = n // 2
midsize = 2 * n - 2 * (colsize + 2)
castle_column_top = '/'+'^' * colsize + '\\'
mid_top = '_' * midsize
top = castle_column_top + mid_top + castle_column_top
middle = '|' + ' ' * (2 * (n - 1)) + '|'
print(top)
for i in range(n - 3):
    print(middle)
castle_column_bottom = '\\' + '_' * colsize + '/'
mid_bottom = ' ' * midsize
a_row_before_bottom = '|' + ' ' * (colsize + 1) + mid_top + ' ' * (colsize + 1) + '|'
print(a_row_before_bottom)
bottom = castle_column_bottom + mid_bottom + castle_column_bottom
print(bottom)
