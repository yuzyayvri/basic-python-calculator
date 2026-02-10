# Basic-Python-Calculator

## Version 0.4.0
My first project with Python. Originally made sometime in mid-2025 and forgotten about, it was originally a basic 3-line terminal calculator with very limited capability. I picked this project back up in early 2026 because I wanted to continue learning Python.

## Current features
- GUI built with tkinter and ttk
- Basic arithmetic and exponents
- Keyboard shortcuts:
    - Select operations (`+`, `-`, `*`, `/`, `^`)
    - Calculate (`Enter`)
    - Exit (`Ctrl+Q`)
- Error handling with logging
- Floating point support
- Clear function to reset all inputs and selected operation
- History log for previous calculations
- Basic settings menu
- Secret easter eggs..?? 👀
- Light and dark theme in the settings menu

## Changelog (v0.4.0)
- Added root operation (`a` is the base, `b` is the index)
- Tweaked the button layout
- Implemented bugfixes

## Future plans (so far)
- Add operations and inputs
- Implement memory functions
- Improve style and theming
- Refactor code for better efficiency and readability

# Documentation (wip)
- Numbers
    - The first input is `a`, and the second is `b`.
    - You can only input numbers
- Operations
    - You can select operations using the buttons
    - Supported operations currently:
        - Addition `+`
        - Subtraction `-`
        - Multiplication `*`
        - Division `/`
        - Exponent `^`
        - Root `√`
    - Each operation can also be selected using their respective keybinds (their symbol), except Root
- Error codes
    - `ERR:invopErr`
        - Invalid operation error. Usually means user did not select any operation.
    - `ERR:zerodivErr`
        - Zero division error. Usually means user tried to divide by zero.
    - `ERR:valErr`
        - Value error. Usually means user inputted a non-number.
    - `ERR:floatErr`
        - Floating point error. Usually means overflow or precision issues occurred. Very rare.
