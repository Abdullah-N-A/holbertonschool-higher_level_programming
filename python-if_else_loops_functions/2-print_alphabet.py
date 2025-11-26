#!/usr/bin/python3

# Iterate through the ASCII codes for 'a' (97) up to 'z' (122).
# The range function goes up to, but does not include, the second number,
# so we use 123 to include the code for 'z'.
for i in range(97, 123):
    # Use the print function only once.
    # "{:c}".format(i) converts the ASCII integer (i) into its corresponding character.
    # end="" ensures no newline is printed, keeping the output on a single line.
    print("{:c}".format(i), end="")
