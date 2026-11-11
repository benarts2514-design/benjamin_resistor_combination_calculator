# Resistor Combination Calculator with DC Circuit Analysis Twist
# Author: BNRS, ND2 Mechatronics Engineering, YabaTech

def calculate_series(resistors):
    """Calculates total resistance in a series circuit. Returns a float."""
    return sum(resistors)

def calculate_parallel(resistors):
    """Calculates total resistance in a parallel circuit. Returns a float."""
    reciprocal_sum = sum(1 / r for r in resistors)
    return 1 / reciprocal_sum

def get_positive_float(prompt_text):
    """Safely gets a positive number from the user with error handling."""
    while True:
        try:
            value = float(input(prompt_text))
            if value <= 0:
                print("Error: Resistance or voltage must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def main():
    print("==========================================")
    print("   BNRS RESISTOR COMBINATION CALCULATOR       ")
    print("==========================================")

    while True:
        try:
            num_resistors = int(input("How many resistors do you have? "))
            if num_resistors <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    resistors = []

    # Loop to collect each resistor value
    for i in range(num_resistors):
        while True:
            val = get_positive_float(f"Enter value for resistor {i + 1} (in Ohms): ")
            resistors.append(val)
            break

    # Calculations using functions that return values
    series_total = calculate_series(resistors)
    parallel_total = calculate_parallel(resistors)

    # Display Results
    print("\n==========================================")
    print("           BNRS RESISTOR RESULTS SUMMARY              ")
    print("==========================================")
    print(f"Resistor values entered: {resistors}")
    print(f"Total Series Resistance ($R_s$): {series_total:,.2f} Ohms")
    print(f"Total Parallel Resistance ($R_p$): {parallel_total:,.2f} Ohms")

    # OWN TWIST: DC Circuit Analysis (Current & Power calculation)
    print("\n--- Custom Twist: DC Circuit Analysis ---")
    choice = input("Do you want to test this circuit with a DC voltage source? (y/n): ").strip().lower()
    
    if choice == 'y':
        voltage = get_positive_float("Enter DC supply voltage (in Volts): ")
        
        # Analyze Series Circuit
        series_current = voltage / series_total
        series_power = voltage * series_current
        
        # Analyze Parallel Circuit
        parallel_current = voltage / parallel_total
        parallel_power = voltage * parallel_current

        print(f"\nWith a {voltage}V Supply:")
        print(f"-> Series Circuit: Current = {series_current * 1000:.2f} mA | Power = {series_power:.2f} Watts")
        print(f"-> Parallel Circuit: Current = {parallel_current:.2f} A | Power = {parallel_power:.2f} Watts")
    else:
        print("Skipping circuit analysis. Good job analyzing your resistors!")

    print("\nThank you for using the BNRS Resistor Calculator!")

if __name__ == "__main__":
    main()
