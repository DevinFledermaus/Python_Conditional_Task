# SPEEDING
speed_limit = int(input("What is the speed limit: "))
driver_speed = int(input("What is your speed: "))

if driver_speed <= speed_limit:
    print("OK")
elif driver_speed == speed_limit + 5:
    print("Points: 1")
elif driver_speed == speed_limit + 10:
    print("Points: 2")
elif driver_speed == speed_limit + 15:
    print("Points: 3")
elif driver_speed == speed_limit + 20:
    print("Points: 4")
elif driver_speed == speed_limit + 25:
    print("Points: 5")
elif driver_speed == speed_limit + 30:
    print("Points: 6")
elif driver_speed == speed_limit + 35:
    print("Points: 7")
elif driver_speed == speed_limit + 40:
    print("Points: 8")
elif driver_speed == speed_limit + 45:
    print("Points: 9")
elif driver_speed == speed_limit + 50:
    print("Points: 10")
elif driver_speed == speed_limit + 55:
    print("Points: 11")
elif driver_speed == speed_limit + 60:
    print("Points: 12")
elif driver_speed >= speed_limit + 65:
    print("Time to go to Jail")
