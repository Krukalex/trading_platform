# Trading Platform Backend

This project contains the backend code for a trading platform application. The platform enables users to manage their accounts, place trades, and monitor their portfolios. Below is the general object hierarchy of the system, describing how key components relate to one another.

---

## Object Hierarchy

### **1. User**
The `User` represents an individual using the platform. Each user can have the following:
- **Account**: The financial account associated with the user, used for deposits, withdrawals, and transactions.
- **Portfolio**: A collection of the user's investments, including orders and stocks.

---

### **2. Account**
The `Account` is directly tied to a `User` and manages the following:
- **Transactions**: Records of all financial activities, such as deposits, withdrawals, and trades.

---

### **3. Portfolio**
The `Portfolio` holds the user's investments and active orders. It contains:
- **Orders**: Pending or completed buy/sell instructions submitted by the user.

---

### **4. Order**
An `Order` represents a request to buy or sell a stock and can result in one or more executed trades. Key types include:
- **Market Orders**: Buy or sell at the current market price.
- **Limit Orders**: Buy or sell at a specified price or better.
- **Stop Orders**: Trigger a market order once the stock reaches a specified price.

Each `Order` is associated with:
- **Trades**: The actual transactions executed to fulfill the order.

---

### **5. Trade**
A `Trade` represents an executed transaction resulting from an order. Each trade is linked to:
- **Stock**: The specific stock being bought or sold during the transaction.

---

### **6. Stock**
A `Stock` represents a publicly traded security, including:
- **Ticker Symbol**: The stock's unique identifier (e.g., AAPL for Apple Inc.).
- **Price**: The current market price of the stock.

---

### **7. Order Processor**
The `Order Processor` handles all pending orders in the portfolio. It processes and executes:
- **Market Orders**
- **Stop Orders**
- **Limit Orders**

---

## Example Hierarchy Overview

User
 ├── Account
 │    └── Transaction
 └── Portfolio
      ├── Order
      │    └── Trade
      │         └── Stock
      └── Order Processor