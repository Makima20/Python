temperature = int(input("Enter the current temperature in °C: "))


if temperature >= 25:
    print("It's warm! You can wear light and soft clothes.")
elif 18 <= temperature < 25:
    print("It's a bit cool. You can wear light clothes, but keep a jacket just in case.")
else:
    print("It's cold! Better to wear warm clothes like a jacket or pullover.")