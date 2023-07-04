import json
import sys
import argparse


## Check file name provided in command ++ Check for valid .json extension, if not, exit.
def read_file(input_filename, output_filename):
    if not input_filename.endswith('.json'):
        print("Invalid input file extension. Please provide a .json file.")
        exit()
        return

    with open(input_filename, 'r') as input_file:
        contents = input_file.read()
        print(contents)

## Output file name define + Success 
        if output_filename is not None:
            with open(output_filename, 'w') as output_file:
                output_file.write(contents)
                print(f"Output file '{output_filename}' created.")

## Read argument -o 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename", help="input JSON filename")
    parser.add_argument("-o", "--output_filename", help="output filename")
    args = parser.parse_args()

    input_filename = args.input_filename
    output_filename = args.output_filename

    read_file(input_filename, output_filename)

## Main convert
def export_to_csv():
    with open(input_filename) as f:
        list1 = []
        data = json.loads(f.read())
        temp = data[0]
        header_items = []
        get_header_items(header_items, temp)
        list1.append(header_items)
      
        for obj in data:
            d = []
            add_items_to_data(d, obj)
            list1.append(d)
        
        with open(output_filename, 'w') as output_file:
            for a in list1:
                output_file.write(','.join(map(str, a)) + "\r")

## Check header items
def get_header_items(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)

## Populate data
def add_items_to_data(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append("")
            add_items_to_data(items, obj[x])
        else:
            items.append(obj[x])

export_to_csv()