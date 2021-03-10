# outer loop
value = 65
for i in range (value,70):
    # inner loop
    for j in range(value,i+1):
        print(chr(j),end="")
    print()
