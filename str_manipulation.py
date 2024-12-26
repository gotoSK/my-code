# each char in string moved 2 step forward. eg.: hacker -> erhack

inp = input("Enter a string: ")

steps = 2
temp = [None] * len(inp)
str_len = len(inp)

# processing
for i in range(0, str_len):
    temp[(i+steps) % str_len] = inp[i]

inp = temp.copy()
temp = []

print("Output: ", inp)