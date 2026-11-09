# Resistor Combination Calculator
# Calculates total resistance in Series and Parallel

def calculate_series(resistors):
    """Function that returns a value - calculates series total"""
    total = 0
    for r in resistors:  # loop through list
        total += r
    return total

def calculate_parallel(resistors):
    """Function that returns a value - calculates parallel total"""
    total_inverse = 0
    for r in resistors:  # loop through list
        if r != 0:  # decision to avoid division by zero
            total_inverse += 1 / r
    
    if total_inverse == 0:  # decision
        return 0
    else:
        return 1 / total_inverse

def main():
    # Main program
    resistors = []  # at least one list to store values
    
    print("=== Resistor Combination Calculator ===")
    
    # Get number of resistors with error handling
    try:
        # Input converted with int()
        num = int(input("How many resistors do you have? "))
        
        if num <= 0:  # decision
            print("Error: Please enter a number greater than 0.")
            return
        elif num == 1:  # decision
            print("Note: You have only 1 resistor, series and parallel will be the same.")
        
        # Loop to get each resistor value
        for i in range(num):
            try:
                # Input converted with float()
                value = float(input(f"Enter value for resistor {i+1} (in Ohms): "))
                
                if value < 0:  # decision
                    print("Error: Resistance cannot be negative. Skipping this one.")
                    continue
                elif value == 0:
                    print("Warning: 0 Ohm resistor added (short circuit).")
                
                resistors.append(value)
                
            except ValueError:
                print("Error: Invalid input! Please enter a number. Skipping this resistor.")
        
        # Check if list is empty
        if len(resistors) == 0:
            print("No valid resistors entered. Cannot calculate.")
            return
        
        # Calculate using functions
        series_total = calculate_series(resistors)
        parallel_total = calculate_parallel(resistors)
        
        # Print results
        print("\n--- Results ---")
        print(f"Resistors entered: {resistors}")
        print(f"Total in Series: {series_total:.2f} Ohms")
        print(f"Total in Parallel: {parallel_total:.2f} Ohms")
        
    except ValueError:
        print("Sensible Error Message: You did not enter a valid whole number for count. Please restart and enter e.g., 3")

# Run the program
if _name_ == "_main_":
    main()