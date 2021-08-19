

# -------  Brenner Campos
# -------  Radix Sort
# -------  Using Bucket Sort to implement Radix

# --------- DIRECTIONS: Simply enter any arbitrary set of numbers separated by space ' ', and then press 'Enter' to sort.


# User Input by keyboard
def prompt():
    print("Type in a series of numbers separated by spaces. When done, hit enter: ")
    response = input("> ")
    # Split each element in the user's input
    numbers = response.split()
    # Return our new list
    return numbers


def radix_sort(number_list):

    # ---- Figuring out how many digits the max number is.
    max_number = 0
    for number in number_list:
        # Making sure to deal with non-digit input (eg. string).
        if number.isdigit():
            # max_number becomes the highest number between the iterative number and current max number.
            max_number = max(max_number, int(number))
    # num_digits becomes the length of that max number.
    num_digits = len(str(max_number))

    # ---- Making and sorting the bucket
    # For however many digits the max number has.
    for digit in range(0, num_digits):
        # Resetting bucket that we can use (creates empty 2D list) - makes 10 buckets from [0-9].
        bucket = [[] for i in range(10)]

        for number in number_list:
            # Checking again for non-digit inputs and ignoring them if not numbers.
            if number.isdigit():
                # Getting the current digit's value
                list_index = digit_value_calc(int(number), digit)
                # Adding it to the bucket of that digit's value.
                bucket[int(list_index)].append(number)

        # Resetting numberList so we can re-sort based on what digit we're at.
        number_list = []

        # For every list of numbers within each bucket...
        for number in bucket:
            # Extend builds our new numberList by adding items iteratively in bucket one at a time.
            number_list.extend(number)

    # Print("Bucket before expansion: "+(str(bucket)))  -- DEBUG

    # When we get to here, the 'number_list' should have gone through each digit and the sort should be complete.
    # Return it.
    return number_list


# Finds value for digits by floor dividing by the number's place (digit) and then modding that by 10.
def digit_value_calc(number, digit):

    # One's place
    if digit == 0:
        val = int(number) // 1 % 10
        return val

    # Ten's place
    if digit == 1:
        val = int(number) // 10 % 10
        return val

    # Hundred's place
    if digit == 2:
        val = int(number) // 100 % 10
        return val

    # Thousand's place
    if digit == 3:
        val = int(number) // 1000 % 10
        return val

    # Ten-Thousand's place
    if digit == 4:
        val = int(number) // 10000 % 10
        return val

    # Hundred-Thousand's place
    if digit == 5:
        val = int(number) // 100000 % 10
        return val

    # Million's place
    if digit == 6:
        val = int(number) // 1000000 % 10
        return val

    # Ten-Million's place
    if digit == 7:
        val = int(number) // 10000000 % 10
        return val

    # Hundred-Million's place
    if digit == 8:
        val = int(number) // 100000000 % 10
        return val

    # Billion's place
    if digit == 9:
        val = int(number) // 1000000000 % 10
        return val
    return 0

# Main
def main():

    # Asking user for input
    number_list = prompt()

    print()
    print("Unsorted number list:    " + str(number_list))
    print()
    print("         VVV         ")
    print("V....Radix Sorting....V ")
    print("       ...V...       ")
    print("        ..V..        ")
    print("         .V.         ")
    print("          V          ")
    print()

    # Getting and printing radix sorted list
    sorted_list = radix_sort(number_list)
    print("Sorted number list:      " + str(sorted_list))


main()
