# 1013 - O Maior

# Input > A (int), B (int), C (int)

user_input = input().split(" ")

value_1 = int(user_input[0])
value_2 = int(user_input[1])
value_3 = int(user_input[2])

maior = [value_1, value_2, value_3]

print(f"{max(maior)} eh o maior")
