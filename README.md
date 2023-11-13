# Flask Module Interaction Guidelines

This project contains 3 Flask modules: `simp` and `comp` and `col`. These modules have specific interaction rules that should be followed. Below are the guidelines:

## `simp` Module
- **Endpoints:** `/add`, `/subtract`
- **Functionality:** Performs basic arithmetic operations on two numbers.
- **Usage:** Ensure to call at least one function from the `simp` module before accessing functions in the `comp` module.

## `comp` Module
- **Endpoints:** `/sumofdigits`, `/ispal`
- **Functionality:** Deals with number manipulation and checks for specific number properties.
- **Restriction:** Functions in this module can only be accessed after at least one function from the `simp` module has been invoked.

## Implementation Details
- **Module Separation:** These modules are implemented in separate files.
- **Enforced Sequence:** A global variable and decorators are used to enforce the sequence of function calls. The `simp` module functions must be accessed before any `comp` module functions can be utilized. Failure to follow this sequence will result in an exception.

## Usage
1. Access the `simp` module endpoints (`/add`, `/subtract`) for basic arithmetic operations.
2. Only after calling at least one function from the `simp` module, proceed to utilize the functionalities provided in the `comp` module (`/sumofdigits`, `/ispal`).

## Exceptions
If attempting to access functions in the `comp` module before any functions in the `simp` module have been called, an exception will be raised to ensure compliance with the module interaction guidelines.

