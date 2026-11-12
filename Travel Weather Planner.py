distance_mi = 1
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1 and is_raining != True:
    print(True)
elif distance_mi <= 1 and is_raining == True:
    print(False)
elif (distance_mi >1 and distance_mi <=6) and (is_raining != False and has_bike == False):
    print(False)
elif (distance_mi >1 and distance_mi <=6) and (has_bike != True and is_raining == False):
    print(False)
elif (distance_mi > 1 and distance_mi <= 6) and (has_bike == True and is_raining != True):
    print(True)
elif distance_mi > 6 and has_ride_share_app == True:
    print(True)
elif distance_mi >6 and has_car == True:
    print(True)
elif distance_mi > 6 and (has_car == False or has_ride_share_app == False):
    print(False)
else:
    print("Invalid Condition")