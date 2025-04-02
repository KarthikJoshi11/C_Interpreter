"""
This module file supports basic functions from stdio.h library
"""

from ..utils.utils import definition
from ..interpreter.number import Number

@definition(return_type='int', arg_types=None)
def printf(*args):
    """ basic printf function
    example:
        printf("%d %s", 1, "Hello");
    """
    fmt, *params = args
    # Handle both Number objects and raw values
    values = [param.value if hasattr(param, 'value') else param for param in params]
    message = fmt % tuple(values)
    result = len(message)
    print(message, end='')
    return result

@definition(return_type='int', arg_types=None)
def scanf(*args):
    """ basic scanf function
        example:
            scanf("%d %s", &n, &str);
    """
    import re
    def cast(flag):
        if flag[-1] == 'd':
            return 'int'
        elif flag[-1] == 'c':
            return 'char'
        elif flag[-1] == 'f':
            return 'float'
        elif flag[-1] == 's':
            return 'char*'
        raise Exception('You are not allowed to use \'{}\' other type'.format(flag))

    fmt, *params, memory = args
    fmt = re.sub(r'\s+', '', fmt)
    all_flags = re.findall('%[^%]*[dfcs]', fmt)
    if len(all_flags) != len(params):
        raise Exception('Format of scanf function takes {} positional arguments but {} were given'.format(
            len(all_flags),
            len(params)
        ))
    elements = []
    while len(elements) < len(all_flags):
        str = input()
        elements.extend(str.split())
    for flag, param, val in zip(all_flags, params, elements):
        if flag[-1] == 'c':
            # For character input, use the first character and convert to ASCII value
            memory[param] = Number('char', ord(val[0]))
        elif flag[-1] == 's':
            # For string input, store the entire string
            if isinstance(param, tuple):
                # Handle array access for strings
                array_name, index = param
                if array_name not in memory.stack.current_frame.current_scope._values:
                    memory.stack.current_frame.current_scope._values[array_name] = []
                array = memory.stack.current_frame.current_scope._values[array_name]
                # Store the entire string in the array
                for i, char in enumerate(val):
                    while len(array) <= i:
                        array.append(Number('char', 0))
                    array[i] = Number('char', ord(char))
                # Pad remaining elements with 0
                while len(array) <= index:
                    array.append(Number('char', 0))
            else:
                memory[param] = val
        else:
            # For numeric inputs
            if isinstance(param, tuple):
                # Handle array access for numbers
                array_name, index = param
                if array_name not in memory.stack.current_frame.current_scope._values:
                    memory.stack.current_frame.current_scope._values[array_name] = []
                array = memory.stack.current_frame.current_scope._values[array_name]
                while len(array) <= index:
                    array.append(Number(cast(flag), 0))
                array[index] = Number(cast(flag), int(val))
            else:
                memory[param] = Number(cast(flag), val)

    return len(elements)


@definition(return_type='char', arg_types=[])
def getchar():
    import sys
    return ord(sys.stdin.read(1))


