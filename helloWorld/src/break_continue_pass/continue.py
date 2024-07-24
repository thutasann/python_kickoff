# Loop Control Statements = change a loops execution from its normal sequence

# breaks = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder


phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
