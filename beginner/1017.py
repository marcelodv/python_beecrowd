# 1017 - Gasto de Combustível

time_of_travel_in_hours = input()
average_speed = input()   
average_gasoline_consumption = 12

result = (float(average_speed) / float(average_gasoline_consumption)) * float(time_of_travel_in_hours)

print("{:.3f}".format(result))