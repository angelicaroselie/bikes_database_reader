import bikes #importing bikes.py module

print()
print("Distance sum for user555:", bikes.distance_of_user("user555")) #printing distance sum of user555
print()
print("AVG Speed for user555:", bikes.speed_of_user("user555")) #printing average speed of user555
print()
print("Duration sum for each city for 2021-06-15:", bikes.duration_in_each_city("2021-06-15")) #printing duration sum of each city on 2021-06-15
print()
print("User amount for city7", bikes.users_in_city("city7")) #printing users in city7
print()
print("Daily trip amount for city7:", bikes.trips_on_each_day("city7")) #printing trips on each day in city7
print()
print("Most popular station and number of trips for city7:", bikes.most_popular_start("city7")) #printing most popular start station and number of trips in city7
print()
