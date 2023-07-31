"""
Cura Marlin G-code pauser
Author: Stephen Nielsen
Date: 7/30/23
"""


def main():

    # Ask user for the address of the gcode file
    file_address = input("Enter the name of the gcode file you want to modify: ")
    
    
    # Open the file
    with open(file_address, "r") as file:

        line_list = file.readlines()

        # Detect the number of layers
        num_layers = 0
        for line in line_list:
            if "LAYER:" in line:
                num_layers += 1
                
        print(f"There are {num_layers} layers.")

        # start loop
        while True:
            pass

            # Ask user what layer they want to insert the pause after
            pause_location = input(f"Which layer would you like to pause after? (1-{num_layers-1}): ")
            # input error handling
            pause_location = int(pause_location)
            if pause_location < 1 or pause_location > num_layers-1:
                print("Invalid input.")
                continue

            # Insert pause ---------------------------------------------------------------------
            # Find the location of the layer in line_list
            insert_index = 0
            for index in range(len(line_list)):
                if (f"LAYER:{pause_location+1}") in line_list[index]:
                    insert_index = index
            # insert pause after insert_index
            line_list.insert(insert_index+1, "M600\n")
            # Display
            print(f"Pause added between layers {pause_location} and {pause_location+1}.")
            # ----------------------------------------------------------------------------------

            # Ask user if they want to insert another pause
            exit_choice = input("Do you want to add another pause? (y/n): ")
            if exit_choice == "y":
                continue
            else: 
                # Write to file, override if already exists----------------
                new_file_address = f"p_{file_address}"

                with open(new_file_address, "w") as new_file:
                    new_file.writelines(line_list)
                
                print(f"Saved as {new_file_address}")
                # ----------------------------------------------------------
                break



if __name__ == "__main__":
    main()