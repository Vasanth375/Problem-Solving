d1, m1, y1 = 5,5,2014
d2, m2, y2 = 23,2,2014

fine = 0
if d1 < d2:
    '''If the book is returned on or before the expected return date, no fine'''
    fine = 0
if d1 > d2 and m1 == m2 and y1 == y2:
    '''If the book is returned after the expected return day but still within the same calendar month and year'''
    fine = 15 * int(d1 - d2)
if m1 > m2 and y1 == y2:
    '''If the book is returned after the expected return month but still within the same calendar year'''
    fine = 500 * int(m1 - m2)
if y1 > y2:
    '''If the book is returned after the calendar year'''
    fine = 10000
print(fine)