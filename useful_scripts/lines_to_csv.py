# Sebastian Raschka 2014
# converts a 1-col input file into csv file
#
# Example input:
# 123
# 245
# 453
#
# Example output:
# 123,245,453
#



with open('new.csv', 'w') as out_file:
    with open('in.txt', 'r') as in_file:
        for line in in_file:
            line = line.strip()
            out_file.write(f'{line},')

