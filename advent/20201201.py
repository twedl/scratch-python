# day one, advent 2020


def day_one():
    # read input for day one, calculate and print answer
    with open('advent/20201201.txt', 'r') as f:
        data = f.read()

    data = [int(i) for i in data.split()]

    for i in data:
        for j in data:
            if i + j == 2020:
                print(f"Day 1.1: i: {i}, j: {j}, answer: {i * j}") 
                break
        else:
            continue

        break
    
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(f"Day 1.1: i: {i}, j: {j}, k: {k}, answer: {i * j * k}") 
                    return

def main():
    day_one()

if __name__ == "__main__":
    main()
