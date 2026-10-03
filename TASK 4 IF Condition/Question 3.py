# Given lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two city names
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Find the country of the first city
if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"
else:
    country1 = None

# Find the country of the second city
if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"
else:
    country2 = None

# Compare the two countries
if country1 is None:
    print(f"{city1} is not in our list")
elif country2 is None:
    print(f"{city2} is not in our list")
elif country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
