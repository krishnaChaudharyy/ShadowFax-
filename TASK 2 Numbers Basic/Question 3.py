distance = 490          # in meters
time_minutes = 7        # in minutes

time_seconds = time_minutes * 60    
speed = distance / time_seconds     

print("Distance        :", distance, "meters")
print("Time            :", time_seconds, "seconds")
print("Speed           :", int(speed), "m/s")
