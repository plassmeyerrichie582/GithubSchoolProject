import os
import sys
from time import sleep

def main():
    while True:
        if not os.path.exists("lesson1"):
            os.makedirs("lesson1")
            print("Created lesson1 directory successfully.")
        
        # Sleep for 1 second before starting the next question
        sleep(1)
        print("Starting new lesson...")
        
        # Ask user input
        input(f"Ready to begin? (y/n): ")
        if input.lower() != 'n':
            break
        
if __name__ == "__main__":
    main()
