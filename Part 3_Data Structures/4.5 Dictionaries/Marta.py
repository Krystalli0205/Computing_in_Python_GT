#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:

marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')

#You may add whatever code you want from here on to answer those three
#questions.
#
#HINT: although there are six items on each line of the file, you only
#need one of them: station ID. If you use split(",") to split up each
#line, station ID will be at index 3 on the list.
#
#HINT 2: You'll probably want to use a dictionary, with station IDs as
#the keys and 

station_tap_counts = {}

for line in marta_file:
    list = line.strip().split(',')
    station_id = list[3]

    if station_id in station_tap_counts:
        station_tap_counts[station_id] += 1
    else:
        station_tap_counts[station_id] = 1

marta_file.close()

total_taps = sum(station_tap_counts.values())
number_of_stations = len(station_tap_counts)
average_taps = total_taps / number_of_stations

print(f"Average number of taps per station: {average_taps}")

closest_station = None
closest_diff = float('inf')

for station_id, tap_count in station_tap_counts.items():
    diff = abs(tap_count - average_taps)
    if diff < closest_diff:
        closest_diff = diff
        closest_station = station_id

print(f"Station closest to the average number of taps: {closest_station}")

least_traffic_station = min(station_tap_counts, key=station_tap_counts.get)
least_traffic_count = station_tap_counts[least_traffic_station]

print(f"Station with the least overall traffic: {least_traffic_station} with {least_traffic_count} taps")






