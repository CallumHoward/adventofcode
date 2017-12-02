
def look_and_say(input):
    result = ''
    num_copies = 0
    curr_digit = input[0]
    for digit in input:
        if digit == curr_digit:
            num_copies += 1
        else:
            result += str(num_copies) + curr_digit
            curr_digit = digit
            num_copies = 1

    result += str(num_copies) + curr_digit
    return result

current = '1113222113'
for _ in xrange(50):
    current = look_and_say(current)

print len(current)

