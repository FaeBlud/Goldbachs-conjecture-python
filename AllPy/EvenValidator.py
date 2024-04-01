input_filename = 'primenumbers.txt'
output_filename = 'primefinished.txt'
start_number = 10
increment = 2

try:
    with open(input_filename, 'r') as file:
        numbers_set = {int(line.strip()) for line in file}

    with open(output_filename, 'w') as output_file:
        for target_number in range(start_number, max(numbers_set) + 1, increment):
            found = False
            for prime in numbers_set:
                if (target_number - prime) in numbers_set:
                    result = f"F: {target_number} = {prime} + {target_number - prime}"
                    print(result)
                    output_file.write(result + "\n")
                    found = True
                    break
            if not found:
                result = f"No: {target_number}"
                print(result)
                output_file.write(result + "\n")
except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
except IOError:
    print(f"Error: Unable to write to output file '{output_filename}'.")
