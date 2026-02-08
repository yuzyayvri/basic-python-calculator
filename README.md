# Basic-Python-Calculator

## Version 0.3.4
My first project with Python. Originally made sometime in mid 2025, I picked this project back up in early 2026 because I wanted to continue learning Python.

## Current features
- GUI built with tkinter and ttk
- Basic arithmetic and exponents
- Keyboard shortcuts for selecting operations, calculating (ENTER), and exiting (CTRL+Q)
- Error handling and error logging
- Floating point support
- Clear function to reset all inputs and selected operation
- History log for previous calculations
- Basic settings menu
- Secret easter eggs..?? 👀

## Changelog (v0.3.4)
- Added theme toggle (light/dark) in settings menu
- Fixed bug where error messages didn't autoclear after 5 seconds
- Fixed bug where ERR:invopErr didn't show in the error log
- Refactored error logging to be compatible across operating systems

## Future plans (so far)
- More operations and inputs
- Memory functions
- More style and theming
- Better and more efficient code

# Documentation (wip)

## Error codes
- ERR:invopErr
    - Invalid operation error. Usually means user did not select any operation.
- ERR:zerodivErr
    - Zero division error. Usually means user tried to divide by zero.
- ERR:valErr
    - Value error. Usually means user inputted a non-number.
- ERR:floatErr
    - Floating point error. Usually means overflow or precision issues occurred.
