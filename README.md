# PRODIGY_CS_01 ON CAESAR CIPHER

This Python program implements a simple Caesar cipher, which is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. The program allows for both encryption and decryption of messages.

## Features

- Encrypt messages using a specified shift value.
- Decrypt previously encrypted messages using the same shift value.
- User-friendly interface with colorful output using ANSI color codes.

## Code Explanation

### ANSI Color Codes

The program uses ANSI escape sequences to print colored text in the terminal. The `Colors` class defines several color codes for use throughout the program:

```python
class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
```

### Main Functionality

#### Main Function

The `main` function orchestrates the program's flow, including:
- Displaying a stylized title.
- Offering options for encryption, decryption, or exiting the program.
  
#### Encryption and Decryption

The `encrypt` and `decrypt` functions handle the cipher operations:

- **Encrypt**: Shifts each letter in the message by the specified shift value.
- **Decrypt**: Shifts each letter back to its original position using the same shift value.

### User Interaction

The program runs in a loop, allowing the user to choose between encryption, decryption, or quitting. Input is taken for the message and shift value, and the output is displayed in a colorful format.

## Usage

1. **Run the Program**:
   Make sure Python is installed on your system. Save the code in a file named `caesar_cipher.py`. Run the program using:
   ```bash
   python caesar_cipher.py
   ```

2. **Choose an Option**:
   - Type `ENCRYPTION` to encrypt a message.
   - Type `DECRYPTION` to decrypt a message.
   - Type `QUIT` to exit the program.

3. **Input Message**:
   Enter the message you want to encrypt or decrypt, and provide the shift value when prompted.

## Example

```
Choose: Encryption, Decryption or Quit: ENCRYPTION
Enter a message: HELLO
Enter shift value: 3
Encrypted Message: KHOOR
```

## Notes

- The program only handles uppercase alphabetical characters. Non-alphabet characters (like spaces and punctuation) remain unchanged.
- Ensure to provide a valid integer for the shift value.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions for Use

- Copy the above text into a file named `README.md` in the same directory as your `caesar_cipher.py` file.
- This README provides a clear overview of your program's purpose, functionality, usage, and code structure, making it easier for others to understand and use your code. 

Let me know if you need any more information or further assistance!
