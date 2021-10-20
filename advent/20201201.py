# day one, advent 2020


def day_one():
    # read input for day one, calculate and print answer
    with open('20201201.txt', 'r') as f:
        data = f.read()

    result = [int(i) for i in data.split()]
    return result




def main():
    result = day_one()
    print(result)

if __name__ == "__main__":
    main()
