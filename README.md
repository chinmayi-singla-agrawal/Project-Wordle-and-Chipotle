**Project Wordle and Chipotle** 

**Wordle Game:** An interactive word-guessing game that challenges players to find a hidden 5-letter word within 6 attempts. 

**Chipotle Order System:** A restaurant order processing system that calculates prices, applies discounts, and generates detailed invoices. 

**1. Wordle Game Application**:  
The Wordle implementation allows players to interactively guess a randomly selected 5-letter word. 
The game provides visual feedback using colored circles to indicate whether each letter in the guess matches the solution word at that exact position.

**Key Features:**<brk> 

1. Random Word Selection: Uses Python's random module to select a different word each game

3. Position-Based Comparison: Evaluates each letter independently at its exact position

4. Interactive Gameplay: Prompts for player input and displays formatted feedback

5. Case-Insensitive Input: Automatically converts guesses to uppercase

6. Game Termination: Exits immediately upon successful guess with congratulations message

**Core Functions (5 total):**
1. get_guess() - Prompts player for a word guess and returns it in uppercase
2. print_word(word) - Displays word with spaces between letters (no trailing space)
3. exact_match_compare(solution, guess) - Compares letters position-by-position, returns emoji string (🟢🔴...)
4. one_turn(solution) - Executes one game round; calls previous functions and exits if guess is correct
5. make_solution() - Randomly selects and returns a word from the pool


**Learning Objectives** 
1. String manipulation (.upper(), concatenation, indexing)
2. Random selection using random.choice()
3. Conditional logic for position comparison
4. Program control flow (exit())
5. Function composition

**CHIPOTLE ORDER PROCESSING SYSTEM** 

**Overview:** 
A restaurant order processing system that calculates meal prices based on ingredient selection, applies discount codes, estimates delivery times by location, and generates professional invoices. Orders are represented as tuples containing customer info, protein, rice, beans, burrito/bowl choice, and toppings. 

**Core Functions (8 total)**
1. get_protein(order) - Returns protein price
2. get_rice(order) - Returns rice price
3. get_beans(order) - Returns beans price
4. get_burrito(order) - Returns burrito/bowl price
5. get_toppings(order) - Returns total topping price (handles vegan discounts)
6. apply_discount(order, total_price) - Applies discount code and returns final price
7. approximate_time(order) - Returns delivery time based on location
8. generate_invoice(order) - Prints formatted invoice with itemized pricing and savings

   
**Learning Objectives**
1. Tuple indexing and iteration
2. Conditional pricing logic (if-elif-else)
3. Arithmetic operations (addition, percentages, subtraction)
4. String formatting with f-strings
5. Special case handling (vegan pricing)
6. Function composition for complex workflows



