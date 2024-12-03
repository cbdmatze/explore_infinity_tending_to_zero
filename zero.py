import matplotlib.pyplot as plt
import numpy as np

# Function to simulate large number tending to zero through its reciprocal
def simulate_large_numbers_tending_to_zero(limit):
    x_values = np.linspace(1, limit, 10000)  # Large range of numbers
    y_values = 1 / x_values  # Their reciprocals
    
    # Plot the behavior
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="Reciprocal of Large Numbers (1/n)")
    plt.title("Reciprocal of Large Numbers Tending to Zero")
    plt.xlabel("n (Large Numbers)")
    plt.ylabel("1/n (Tending to Zero)")
    plt.ylim(0, 0.1)  # Limit y-axis for clarity
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print out a few values to illustrate how large numbers tend to zero
    print("n values and their reciprocals (1/n):")
    for n in [10**i for i in range(1, 10)]:
        print(f"n = {n}, 1/n = {1/n}")

# Function to explore how large numbers tend to zero in their reciprocal
def explore_infinity_and_zero():
    print("Exploring the relationship between infinity and zero:")
    
    # Start by simulating numbers getting larger
    limit = 10**6  # Set a very large limit for numbers
    simulate_large_numbers_tending_to_zero(limit)
    
    # As n increases towards infinity, 1/n approaches zero
    print("\nAs numbers increase towards infinity, their reciprocals approach zero.")
    print("This demonstrates the connection between the largest numbers and zero.")

# Main function
if __name__ == "__main__":
    explore_infinity_and_zero()
