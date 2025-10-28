[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21297781)

# Hexorcist

The Hexorcist is a base converter that lets you transform numbers from one base to another. This works whether that’s binary, decimal, hexadecimal, or even base 36.

## Features
- Convert numbers from any base between 2 and 36 to any other base between 2 and 36.
- Supports digits 0-9 and letters A-Z for digits above 9.

## Requirements
- Python 3

## Usage
1. Open a terminal (zsh on macOS is supported).
2. Run the script:

    python3 hexorcist.py

3. Follow the prompts:
    - Enter the number to convert (letters are case-insensitive).
    - Enter the number's current base
    - Enter the target base 

## Tests
- A test file `test_hexorcist.py` is included. 
- To run type pytest in your terminal and it will run anything starting with test_

## How it flows
![alt text](image.png)
