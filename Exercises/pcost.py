def portfolio_cost(filename):
    result = 0

    with open(filename) as f:
        for line in f:
            try:
                _, quantity, price = line.split(" ")
                result += int(quantity) * float(price)
            except ValueError:
                continue

    return result


if __name__ == "__main__":
    with open("Data/portfolio.dat") as f:
        result = 0

        for line in f:
            _, quantity, price = line.split(" ")
            result += int(quantity) * float(price)

        print(result)

        print(portfolio_cost("Data/portfolio.dat"))

        print(portfolio_cost("Data/portfolio3.dat"))
