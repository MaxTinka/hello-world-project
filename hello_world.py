"""
Hello World Program
Author: Tinka Max
Course: CSE 310
Description: A simple Hello World program with personality.
"""

def main():
    print("=" * 40)
    print("Hello World!")
    print("Welcome to CSE 310 - Applied Programming")
    print("=" * 40)
    
    # Ask for user's name
    name = input("\nWhat's your name? ")
    print(f"Nice to meet you, {name}!")
    print("Let's have a great semester!")
    
    # Simple loop
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(f"  {i}...")
    print("Done!")

if __name__ == "__main__":
    main()
