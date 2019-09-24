# By Kwame Boamah on Monday, September 23, 2019

user_name = str(input("Hello. What is your name?"))
print("Hello", user_name, "my name is Randy.")

user_location = str(input("Where are you from?"))
print(user_location, "sounds like a lovely place.")
favorite_number = int(input("Whats your favorite number?"))

my_fav_number = 5

print("My favorite number is", my_fav_number, "but yours is cooler. HAHA")

user_dream_car = str(input("If you could have any car in the world, which car would you have."))

print("WOW, really? The", user_dream_car "are cool.")

dream_car_cost = float(input("How much does The", user_dream_car,"cost?" ))

print("That's a pricey set of wheels.")

possible_loan_period = int(input("How long would you take out a loan on that car?"))
possible_interest_rate = int(float("What annual interest rate do you think you will get on that?"))
monthly_interest_rate = (possible_interest_rate / 100) / 12
number_of_monthly_payments = (possible_loan_period * 12)

monthly_payment = (monthly_interest_rate * dream_car_cost) / (1 -(1 + monthly_interest_rate) ** -number_of_monthly_payments)

total_car_interest = (monthly_payment * number_of_monthly_payments) - dream_car_cost
total_car_cost = dream_car_cost + total_car_interest

print("Your monthly payment for The", user_dream_car, "is", monthly_payment, "and the car total car cost is", total_car_cost)