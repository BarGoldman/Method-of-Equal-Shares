#  Bar Goldman

def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    # Initialize a dictionary to track supporters for each item.
    item_supporters = {item: [] for item in costs.keys()}

    # Populate item_supporters with indices of voters supporting each item.
    for voter_index, voter_votes in enumerate(votes):
        for item in voter_votes:
            if item in item_supporters:
                item_supporters[item].append(voter_index)

    # Determine which item can be funded.
    item_fundability = {}
    for item, supporters in item_supporters.items():
        total_balance = sum(balances[i] for i in supporters)
        if total_balance >= costs[item] * len(supporters):  # Check if total balance covers the cost per supporter
            item_fundability[item] = total_balance

    if not item_fundability:
        print("No item can be funded with the current balances.")
        return

    # Select the item with the most support that can be funded.
    next_item = max(item_fundability.keys(), key=lambda i: (len(item_supporters[i]), -costs[i]))
    supporters = item_supporters[next_item]
    total_cost = costs[next_item]

    # Pay attention to edge cases:
    # some backers may not have enough money to pay, so other backers will have to pay more.

    # Assess if all supporters' balances are similar.
    supporter_balances = [balances[i] for i in supporters]
    all_balances_similar = len(set(supporter_balances)) == 1

    if all_balances_similar:
        contribution = {i: total_cost for i in supporters}

    else:
        contribution = {}
        for i in supporters:
            contribution[i] = balances[i]

        total_contributions = sum(contribution.values())
        shortfall = total_cost - total_contributions

        # If there's a shortfall, redistribute it among backers who can afford to pay more.
        if shortfall > 0:
            for i in supporters:
                if balances[i] - contribution[i] > 0:
                    additional_payment = min(balances[i] - contribution[i], shortfall / len(supporters))
                    contribution[i] += additional_payment
                    shortfall -= additional_payment
                    if shortfall <= 0:
                        break

        # Deduct contributions from balances and update accordingly.
    for i in supporters:
        balances[i] -= contribution[i]

        # Output selected item, contributions, and new balances.
    print(f"Round 1: {next_item} is elected.")
    for i in supporters:
        print(f"Citizen {i + 1} pays {contribution[i]:.2f} and has {balances[i]:.2f} remaining balance.")


print("Example 1: ")

votes = [{'A', 'B', 'C', 'D', 'E'}] * 51 + [{'V', 'Y', 'W', 'X', 'Z'}] * 49
balances = [5] * 100
costs = {'A': 1.96, 'B': 1.96, 'C': 1.96, 'D': 1.96, 'E': 1.96, 'V': 2.04, 'Y': 2.04, 'W': 2.04, 'X': 2.04, 'Z': 2.04}

elect_next_budget_item(votes, balances, costs)

print("Example 2: ")

votes = [{'A', 'D', 'E'}] + [{'A', 'C'}] + [{'B', 'E'}] + [{'C', 'D', 'F'}]
balances = [7.5] * 4
costs = {'A': 5, 'B': 10, 'C': 5, 'D': 5, 'E': 5, 'F': 10}

elect_next_budget_item(votes, balances, costs)

print("Example 3: ")

votes = [{'A', 'D', 'E'}] + [{'A', 'C'}] + [{'B', 'E'}] + [{'C', 'D', 'F'}]
balances = [2.5, 2.5, 7.5, 7.5]
costs = {'A': 5, 'B': 10, 'C': 5, 'D': 5, 'E': 5, 'F': 10}

elect_next_budget_item(votes, balances, costs)
