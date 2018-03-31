input_file = sys.argv[1]
print("Output #140:")
with open(input_file, 'r', newline='')as filereader:
    for row in filereader:
        print("{}".format(row.strip()))
