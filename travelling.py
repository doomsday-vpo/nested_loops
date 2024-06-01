while True:

    destination = input()
    if destination == "End":
        break

    min_budget = float(input())
    savings = 0.0

    while savings < min_budget:
        amount = float(input())
        savings += amount

    print(f"Going to {destination}!")
