# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation bundles product data like name, price, and stock together with behavior methods inside a single class, using 
private attributes to restrict direct outside access. The private stock and price data, along with methods like selling or 
restocking, are involved in keeping records safe. Applying this improves system design by preventing accidental data corruption,
ensuring that inventory counts can only be changed through controlled procedures.

### 2. Abstraction
Abstraction hides the complex inner workings of the inventory system and exposes only simple, high-level features for the user. 
It involves high-level methods like a checkout process that hide background database updates and complex mathematical 
calculations, This improves program design by keeping the interface clean and preventing store operators from being overwhelmed 
by unecessary technical details.

### 3. Inheritance
Inheritance lets us create a general base class for products and derive specialized categories, such as drinks or snacks, that 
inherit common features automatically. It involves shared product properties combined with subclass-specific attributes like 
expiration dates for perishable goods. This improves organization by promoting code reusability, meaning we don't have to 
rewrite basic inventory logic for every single new item type.

### 4. Polymorphism
Polymorphism allows different types of products to share the exact same method name while performing tasks tailored to their 
specific type. It involves shared method names implemented across various product subclasses to handle actions like generating 
price labels uniformly. This improves program design by making the codebase flexible, allowing the inventory system to handle 
all products through a single, consistent interface.

## Reflection
I believe encapsulation is the most useful pillar because a sari-sari store heavily relies on accurate daily tracking of stock 
and money. By hiding sensitive attributes like price and quantity behind controlled methods, it prevents accidental errors or 
data tampering by anyone using the system. This ensures data integrity, making it the most critical foundation for a reliable 
small-scale retail inventory.