## Smart Vending Machine

Annex B
Computational Thinking Exercise: "Smart Vending Machine"
Section: 9-Beryllium       Score:____________

C# / Name: Andrew G. Alcantara           Date: 08/19/26


## Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

## Step 1: Identify the Big Problem

### Main Problem: 

The school's current vending machine is unreliable, inefficient, 
and prone to user errors due to mechanical, computational, and interface shortcomings, 
leading to incorrect transactions, stockouts, and processing delays.


## Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Incorrect Change Calculation: The machine fails to calculate or dispense 
the exact change owed to the student after a transaction.

2. Inventory Management & Monitoring: The machine lacks a system to track 
stock levels, causing items to run out without alerting administrators or staff.

3. User Interface & Input Errors: The selection interface is confusing or poorly 
designed, causing students to press the wrong buttons and receive unwanted items.

4. Transaction Processing Speed: The machine's system lags or freezes when multiple 
students attempt to use it consecutively in a short period.


## Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem

1. Incorrect Change Calculation
2. Inventory Management
3. User Interface Errors
4. Processing Speed

CT Skill

1. Algorithm Design & Logic
2. Abstraction & Pattern Recognition
3. Design/Decomposition
4. Efficiency & Optimization

Example Solution

1. Program a precise mathematical module that subtracts item cost from inserted cash, then calculates the optimal breakdown of coins/bills to dispense.
2. Install digital weight or optical sensors for each slot to track item quantities and send an automated notification email/SMS when stock falls below a threshold.
3. Replace physical membrane buttons with a clear touchscreen graphical user interface (GUI) featuring image confirmations and a "Cancel/Back" option.
4. Upgrade the microcontroller/hardware processing unit and optimize the software code to handle asynchronous inputs and clear transaction queues faster.

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)

### Identified sub-problem

1. Incorrect Change Calculation: The machine fails to calculate or dispense 
the exact change owed to the student after a transaction.

START
  INPUT item_price
  INPUT cash_inserted
  
  IF cash_inserted < item_price THEN
    PRINT "Insufficient funds. Please insert more money."
  ELSE IF cash_inserted == item_price THEN
    DISPENSE item
    PRINT "Exact amount received. No change."
  ELSE
    change = cash_inserted - item_price
    DISPENSE item
    DISPENSE change
    PRINT "Dispensing change: ", change
  END IF
END