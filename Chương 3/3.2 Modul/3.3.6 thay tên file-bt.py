# Doc file input.txt va phan tich thua so nguyen to

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

# Xu ly tung dong trong file input
for line in input_file:
    line = line.strip()

    if line == "":
        continue

    number = int(line)
    divisor = 2

    # Phan tich thua so nguyen to
    while number > 1:
        if number % divisor == 0:
            output_file.write(str(divisor) + " ")

            while number % divisor == 0:
                number //= divisor
        else:
            divisor += 1

    output_file.write("\n")

input_file.close()
output_file.close()

print("Da phan tich va ghi ket qua ra output.txt!")
