import argparse

def string_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    print(count)
    return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Character Counter')
    parser.add_argument('--string', action='store', type=str)
    result = parser.parse_args()
    string = result.string
    
    string_length(string)