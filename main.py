min_number = int(input())#number digits starts from
max_number = int(input())#number digits ends
for a in range(min_number, max_number+1):
    for b in range(min_number, max_number+1):
        for c in range(min_number, max_number+1):
            for d in range(min_number, max_number+1):
                if a % 2 == 0 and d % 2 != 0 or a % 2 != 0 and d % 2 == 0:
                    if (b + c) % 2 == 0:
                        if a>d:
                            print(f"{a}{b}{c}{d}", end=" ")
