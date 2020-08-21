nr_films = int(input())

highest, lowest, sum = 0, 0, 0

for _ in range(nr_films):
    film_name = input()
    film_rating = float(input())

    if film_rating > highest:
        highest = film_rating
        highest_name = film_name
    if lowest == 0 or film_rating < lowest:
        lowest = film_rating
        lowest_name = film_name
    sum += film_rating

print(f"{highest_name} is with highest rating: {highest:.1f}")
print(f"{lowest_name} is with lowest rating: {lowest:.1f}")
print(f"Average rating: {(sum/nr_films):.1f}")
