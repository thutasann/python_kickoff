for i in range(10):
    if i == 2:
        pass  # Does nothing, just a placeholder
    elif i == 4:
        continue  # Skip the rest of the loop when i is 4
    elif i == 7:
        break  # Exit the loop when i is 7
    print(i)

print("Loop completed!")
