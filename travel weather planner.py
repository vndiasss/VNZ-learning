distance_mi = 10
is_raining = False
has_car = False
has_bike = True
has_ride_share_app = True

if not distance_mi:
    print(bool(distance_mi))

elif distance_mi <= 1 and not is_raining:
    print(bool(distance_mi))

elif distance_mi <= 1 and is_raining:
    print(False)

elif distance_mi <= 6 and is_raining and not has_bike:
    print(False)

elif distance_mi > 1 and distance_mi <= 6 and not is_raining and not has_bike:
    print(False)

elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print(True)

elif distance_mi > 6 and has_ride_share_app:
    print(True)

elif distance_mi > 6 and has_car:
    print(True)

elif distance_mi > 6 and not has_car and not has_ride_share_app:
    print(False)