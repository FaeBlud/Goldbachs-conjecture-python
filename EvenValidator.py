input_filename = 'primenumbers.txt'
output_filename = 'primefinished.txt'
start_number = 0
increment = 2


try:
    with open(input_filename, 'r') as file:
        numbers_list = [int(line.strip()) for line in file]

    with open(output_filename, 'w') as output_file:
        for target_number in range(start_number, max(numbers_list) + 1, increment):
            found = False
            for i in range(len(numbers_list)):
                for j in range(i+1, len(numbers_list)):
                    if numbers_list[i] + numbers_list[j] == target_number:
                        result = f"Found: {numbers_list[i]} + {numbers_list[j]} = {target_number}"
                        print(result)
                        output_file.write(result + "\n")
                        found = True
                        break
                if found:
                    break

            if not found:
                result = f"No two numbers sum up to {target_number}"
                print(result)
                output_file.write(result + "\n")
except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
except IOError:
    print(f"Error: Unable to write to output file '{output_filename}'.")
