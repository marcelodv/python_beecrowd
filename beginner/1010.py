# 1010 - Cálculo Simples

# Input > Part Number | Quantity | Unit Value

first_user_input = input().split(" ")
second_user_input = input().split(" ")

first_part_value = float(first_user_input[1]) * float(first_user_input[2])
second_part_value = float(second_user_input[1]) * float(second_user_input[2])

final_value = first_part_value + second_part_value

formatted_final_value = round(final_value, 2)

print("VALOR A PAGAR: R$ {:.2f}".format(formatted_final_value))