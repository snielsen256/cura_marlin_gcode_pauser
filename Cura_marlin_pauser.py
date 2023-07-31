"""
Cura Marlin G-code pauser
Author: Stephen Nielsen
Date: 7/30/23
"""

import os

def main():

    # Ask user for the address of the gcode file
    file_address = input("Enter the name of the gcode file you want to modify: ")
    
    
    # Open the file
    with open(file_address, "r") as file:

        # Detect the number of layers
        
        num_layers = 0

        for line in file:
            if "LAYER:" in line:
                num_layers += 1

        print(f"There are {num_layers} layers.")

        # start loop
        """
        while True:
            pass

            # Ask user what layer they want to insert the pause after

            # Insert pause

            # Ask user if they want to insert another pause
            exit_choice = input("Do you want to add another pause? (y/n): ")
            if exit_choice == "y":
                continue
            else:
                break"""



if __name__ == "__main__":
    main()