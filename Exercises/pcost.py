with open("Data/portfolio.dat") as f:
    result = 0

    for line in f:
        _, quantity, price = line.split(" ")
        result += int(quantity) * float(price)

    print(result)
