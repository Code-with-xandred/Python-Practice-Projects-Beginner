

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file('sample.txt')