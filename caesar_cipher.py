# ANSI color codes
class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

def main():
    letters = {chr(i + 65): i for i in range(26)}  # Create a dictionary for A-Z
    print(Colors.BLUE + " _____       ___   _____   _____       ___   _____   __    __ " + Colors.RESET)
    print(Colors.BLUE + "/  ___|     /   | | ____| /  ___/     /   | |  _  \\  \\ \\  / /" + Colors.RESET)
    print(Colors.BLUE + "| |        / /| | | |__   | |___     / /| | | |_| |   \\ \\/ /  " + Colors.RESET)
    print(Colors.BLUE + "| |       / / | | |  __|  \\___  \\   / / | | |  _  /    }  {   " + Colors.RESET)
    print(Colors.BLUE + "| |___   / /  | | | |___   ___| |  / /  | | | | \\ \\   / /\\ \\  " + Colors.RESET)
    print(Colors.BLUE + "\\_____| /_/   |_| |_____| /_____/ /_/   |_| |_|  \\_\\ /_/  \\_\\" + Colors.RESET)

    def encrypt(message, shift):
        encrypted_message = ""
        for char in message:
            if char in letters:
                sum = (letters[char] + shift) % 26
                encrypted_message += list(letters.keys())[sum]
            else:
                encrypted_message += char  # Non-alphabet characters remain unchanged
        return encrypted_message

    def decrypt(message, shift):
        decrypted_message = ""
        for char in message:
            if char in letters:
                sum = (letters[char] - shift) % 26
                decrypted_message += list(letters.keys())[sum]
            else:
                decrypted_message += char  # Non-alphabet characters remain unchanged
        return decrypted_message

    while True:
        choice = input(Colors.GREEN + "Choose: Encryption, Decryption or Quit: " + Colors.RESET).upper()
        if choice == "ENCRYPTION":
            message = input(Colors.YELLOW + "Enter a message: " + Colors.RESET).upper().replace(" ", "")
            shift = int(input(Colors.YELLOW + "Enter shift value: " + Colors.RESET))
            encrypted = encrypt(message, shift)
            print(Colors.GREEN + "Encrypted Message: " + encrypted + Colors.RESET)
        elif choice == "DECRYPTION":
            message = input(Colors.YELLOW + "Enter a message: " + Colors.RESET).upper().replace(" ", "")
            shift = int(input(Colors.YELLOW + "Enter shift value: " + Colors.RESET))
            decrypted = decrypt(message, shift)
            print(Colors.GREEN + "Decrypted Message: " + decrypted + Colors.RESET)
        elif choice == "QUIT":
            print(Colors.RED + "Thank You" + Colors.RESET)
            break
        else:
            print(Colors.RED + "Error: Invalid choice. Please try again." + Colors.RESET)

if __name__ == '__main__':
    main()
