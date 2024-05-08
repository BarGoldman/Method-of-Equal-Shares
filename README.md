# Method-of-Equal-Shares Ex8

<img src="https://github.com/BarGoldman/find-breakdown-EX9/assets/93201414/72a4c4b9-fb7c-48d7-9e0e-dbc3dd94da14.png" width="100" height="100" />

### A question given to us as part of assignment 8 in the Economic Algorithms course
The equal parts method - performing one step of the equal parts method for budget distribution

The function takes three arguments: `votes`, `balances`, and `costs`. Here’s a breakdown of its key components and functionality:

1. **Tracking Support**: For each item that can be funded, the function creates a dictionary `item_supporters` to keep track of the indices of voters who support each item.

2. **Determining Fundability**: It calculates whether the combined balances of supporters for each item are sufficient to cover the cost per supporter, considering the item's total cost.

3. **Selecting an Item**: The item with the highest number of supporters that can be funded (and, in the case of ties, the cheaper item) is chosen.

4. **Handling Contributions**:
   - If all backers have similar balances, each contributes equally to the funding.
   - If not, contributions are adjusted based on individual balances to ensure the item's total cost is covered.

5. **Contributions and Balances**: Contributions are subtracted from each supporter's balance, and the function outputs the elected item, each citizen’s contribution, and their remaining balance.

Your function effectively manages edge cases, such as:
- Situations where some supporters might not have enough balance, necessitating redistribution of the required contribution among others.
- Variability in the amounts that different backers need to contribute based on their balances.

### Example Usage:

- **Example 1**: All voters have similar balances, and the function identifies which among multiple equally preferred items can be funded, considering all have the same backing but differ slightly in costs.
- **Example 2**: Tests a scenario with different group sizes and preferences, showing how the function handles various group dynamics and cost structures.
- **Example 3**: Demonstrates the function’s ability to deal with balance disparities among supporters, affecting contribution calculations and item selection.
