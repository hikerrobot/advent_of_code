with open("sample", "rb") as binary_file:
    # Read the whole file at once
    # data = binary_file.read()
    # print(data)


    for data in binary_file:
        print(data)
        print(type(data))
        print(data[0])
        print(data[1])


# iterate through length of string
# process each report line

# dict[pos]=dict[value]=count

# compare dict[pos] 0 & 1 for greatest

# can we use int?
# e.g. can get bit 