<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">121. Best Time to Buy and Sell Stock</a></h2><h3>Easy</h3><hr><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


Walk Through on **why the logic of `price - min_price > max_profit` works** step by step.

---

### **Problem Context**:  
We want to **buy and sell a stock** to maximize profit. The goal is to:
- **Buy at the lowest price** possible.
- **Sell at the highest price** after buying (i.e., sell on a later day).

The tricky part is that we don’t know in advance where the minimum and maximum prices are in the list. So, we need an **on-the-go strategy** to ensure we don’t miss the best profit opportunity.

---

### **Core Idea**:  
As we iterate through the prices:
- **Track the lowest price seen so far** (`min_price`).
- **Calculate potential profit** if we sell at the current price.
- **Update the maximum profit** if the potential profit is greater than any profit found previously.

---

### **Explanation of `price - min_price > max_profit`**:

#### 1. **`min_price` stores the lowest price up to the current day**:
- At any point in the iteration, `min_price` holds the **smallest price seen so far**.
- This ensures that we’re always calculating the profit by "buying at the lowest price" up to the current day.

#### 2. **`price - min_price` calculates the potential profit**:
- For each `price` (i.e., the price on the current day), the expression `price - min_price` gives the **profit** if we:
  - Buy at `min_price` (the lowest price up to now).
  - Sell at `price` (the current day's price).

#### 3. **`price - min_price > max_profit` ensures we update max profit**:
- If the current potential profit (i.e., `price - min_price`) is greater than the **best profit** we’ve found so far (`max_profit`), we update `max_profit`.

#### 4. **Why This Works**:
- This approach ensures that:
  - We **always buy at the lowest price** available up to the current day.
  - We **maximize the profit by selling at a higher price** only when it improves the total profit.
- Because we **only move forward** in the list (no going back), we guarantee that the buy day always comes **before** the sell day.

---

### **Walkthrough Example**:  
Let’s take the prices `[7, 1, 5, 3, 6, 4]` and see how the logic works.

1. **Initial State**:
   - `min_price = ∞`
   - `max_profit = 0`

2. **Iteration**:
   - Day 1: Price = 7  
     - `min_price = min(∞, 7) = 7`
     - Potential Profit = `7 - 7 = 0`
     - No update to `max_profit`.

   - Day 2: Price = 1  
     - `min_price = min(7, 1) = 1`
     - Potential Profit = `1 - 1 = 0`
     - No update to `max_profit`.

   - Day 3: Price = 5  
     - Potential Profit = `5 - 1 = 4`
     - `4 > 0` → Update `max_profit = 4`

   - Day 4: Price = 3  
     - Potential Profit = `3 - 1 = 2`
     - `2 < 4` → No update to `max_profit`.

   - Day 5: Price = 6  
     - Potential Profit = `6 - 1 = 5`
     - `5 > 4` → Update `max_profit = 5`

   - Day 6: Price = 4  
     - Potential Profit = `4 - 1 = 3`
     - `3 < 5` → No update to `max_profit`.

3. **Final Output**:
   - The maximum profit is **5**, achieved by buying at price 1 (Day 2) and selling at price 6 (Day 5).

---

### **Why This Solution is Efficient**:
- **O(n) Time Complexity**:  
  - We only traverse the prices once, making this solution linear in time.
  
- **O(1) Space Complexity**:  
  - Only a few variables (`min_price` and `max_profit`) are used, so the space complexity is constant.

---

### **Summary**:
The condition `price - min_price > max_profit` ensures we **maximize the profit** at every step by comparing the potential profit with the best profit found so far. This ensures that:
- We **buy at the lowest price** encountered up to the current day.
- We **only update the profit** when selling at a higher price improves the total profit.
