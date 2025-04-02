--

# Simple C Interpreter (SCI)

The Simple C Interpreter (SCI) is a lightweight interpreter for a subset of the C programming language. It processes C-like source code by lexing, parsing, performing semantic analysis, and executing the program directly using a custom memory model. This project is designed for educational purposes or as a starting point for building a more complex compiler or interpreter.

## Features
- **Lexical Analysis**: Tokenizes C-like source code into a stream of tokens.
- **Syntax Analysis**: Parses tokens into an Abstract Syntax Tree (AST).
- **Semantic Analysis**: Checks for semantic correctness (e.g., type checking, symbol resolution).
- **Symbol Table**: Manages variable and function scopes.
- **Memory Management**: Simulates runtime memory with global and stack-based scoping.
- **Interpreter**: Executes the program directly from the AST, supporting variables, functions, expressions, and control flow.

## Requirements
- **Python**: 3.8 or higher
- **Dependencies**: None (pure Python implementation)


## Usage
Run the interpreter with a C-like source file:

```bash
python3 __main__.py  -f example.kk
```



### Example
Create a file `example.c`:
```c
int main() {
    int x = 5;
    int y = 10;
    return x + y;
}
```

Execute it:
python3 __main__.py  -f example.kk
```

**Output:**
```
Process terminated with status 15
```



The interpreter will:
1. Lex and parse the source code.
2. Perform semantic analysis.
3. Execute the program and return the result of `main`.

### Error Handling
Errors (e.g., syntax errors, undeclared variables) are reported with colored output:
```
[SyntaxError] Expected token <EOF> but found <ID> Process terminated with status -1
```
```

### Key Files
- **`lexer.py`**: Converts source code into tokens (e.g., `int`, `+`, `ID`).
- **`parser.py`**: Builds an AST from tokens using recursive descent parsing.
- **`tree.py`**: Defines AST node classes (e.g., `Program`, `BinOp`).
- **`analyzer.py`**: Ensures semantic correctness (e.g., type checking, scope validation).
- **`table.py`**: Implements a scoped symbol table for variables and functions.
- **`memory.py`**: Manages runtime memory with global and stack-based scopes.
- **`interpreter.py`**: Executes the AST, supporting expressions, functions, and control flow.

## Supported Language Features
- **Types**: `int`, `float`, `double`, `char`
- **Variables**: Declaration and assignment (e.g., `int x = 5;`)
- **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `%`), relational (`<`, `>`, etc.), logical (`&&`, `||`, `!`), bitwise (`&`, `|`, `^`), increment/decrement (`++`, `--`)
- **Control Flow**: `if`, `while`, `for`
- **Functions**: User-defined functions and basic built-in support (e.g., `scanf`)
- **Statements**: Compound statements (`{}`), return statements

## Limitations
- No support for pointers, arrays, or structs.
- Limited built-in library functions (depends on `interpreter.__builtins__`).
- No intermediate code generation or optimization—direct interpretation only.
- Type safety is enforced during semantic analysis but not fully at runtime.
## License
This project is unlicensed—use it freely for educational or personal purposes.

## Acknowledgments
- Built with inspiration from classic compiler design principles.
- Uses the visitor pattern for AST traversal.

---


# C_Interpreter
# C_Interpreter
