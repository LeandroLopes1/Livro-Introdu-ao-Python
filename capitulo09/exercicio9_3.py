with open("pareseimpares.txt", "w") as pareseimpares:
    for i in range(1, 101):
        if i % 2 == 0:
            pareseimpares.write(f"{i}\n")
        else:
            pareseimpares.write(f"{i}\n")
