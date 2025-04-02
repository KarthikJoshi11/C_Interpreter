import random
from .number import Number

class Scope(object):
    def __init__(self, scope_name, parent_scope=None):
        self.scope_name = scope_name
        self.parent_scope = parent_scope
        self._values = dict()

    def __setitem__(self, key, value):
        self._values[key] = value

    def __getitem__(self, item):
        return self._values[item]

    def __contains__(self, key):
        return key in self._values

    def __repr__(self):
        lines = [
            '{}:{}'.format(key, val) for key, val in self._values.items()
        ]
        title = '{}\n'.format(self.scope_name)
        return title + '\n'.join(lines)


class Frame(object):
    def __init__(self, frame_name, global_scope):
        self.frame_name = frame_name
        self.current_scope = Scope(
            '{}.scope_00'.format(frame_name),
            global_scope
        )
        self.scopes = [self.current_scope]

    def new_scope(self):
        self.current_scope = Scope(
            '{}{:02d}'.format(
                self.current_scope.scope_name[:-2],
                int(self.current_scope.scope_name[-2:]) + 1
            ),
            self.current_scope
        )
        self.scopes.append(self.current_scope)

    def del_scope(self):
        current_scope = self.current_scope
        self.current_scope = current_scope.parent_scope
        self.scopes.pop(-1)
        del current_scope

    def __contains__(self, key):
        return key in self.current_scope

    def __repr__(self):
        lines = [
            '{}\n{}'.format(
                scope,
                '-' * 40
            ) for scope in self.scopes
        ]

        title = 'Frame: {}\n{}\n'.format(
            self.frame_name,
            '*' * 40
        )

        return title + '\n'.join(lines)


class Stack(object):
    def __init__(self):
        self.frames = list()
        self.current_frame = None

    def __bool__(self):
        return bool(self.frames)

    def new_frame(self, frame_name, global_scope=None):
        frame = Frame(frame_name, global_scope=global_scope)
        self.frames.append(frame)
        self.current_frame = frame

    def del_frame(self):
        self.frames.pop(-1)
        self.current_frame = len(self.frames) and self.frames[-1] or None

    def __repr__(self):
        lines = [
            '{}'.format(frame) for frame in self.frames
        ]
        return '\n'.join(lines)


class Memory(object):
    def __init__(self):
        self.global_frame = Frame('GLOBAL_MEMORY', None)
        self.stack = Stack()

    def declare(self, key, value=None):
        ins_scope = self.stack.current_frame.current_scope if self.stack.current_frame else self.global_frame.current_scope
        if isinstance(value, list):
            # For array declarations, store as a list of Number objects
            ins_scope[key] = [val if isinstance(val, Number) else Number('int', val) for val in value]
        else:
            # For regular variables, use random value if none provided
            ins_scope[key] = value if value is not None else Number('int', random.randint(0, 2**32))

    def __setitem__(self, key, value):
        ins_scope = self.stack.current_frame.current_scope if self.stack.current_frame else self.global_frame.current_scope
        curr_scope = ins_scope
        while curr_scope and key not in curr_scope:
            curr_scope = curr_scope.parent_scope
        ins_scope = curr_scope if curr_scope else ins_scope
        
        # Handle array access
        if isinstance(key, tuple) and len(key) == 2:
            array_name, index = key
            if array_name not in ins_scope:
                # Initialize array if it doesn't exist
                ins_scope[array_name] = []
            array = ins_scope[array_name]
            # Ensure array is large enough and contains Number objects
            while len(array) <= index:
                array.append(Number('int', 0))
            # Convert value to Number if it isn't already
            array[index] = value if isinstance(value, Number) else Number('int', value)
        else:
            ins_scope[key] = value

    def __getitem__(self, item):
        curr_scope = self.stack.current_frame.current_scope if self.stack.current_frame else self.global_frame.current_scope
        while curr_scope and item not in curr_scope:
            curr_scope = curr_scope.parent_scope
            
        # Handle array access
        if isinstance(item, tuple) and len(item) == 2:
            array_name, index = item
            if array_name not in curr_scope:
                # Initialize array if it doesn't exist
                curr_scope[array_name] = []
            array = curr_scope[array_name]
            # Ensure array is large enough and contains Number objects
            while len(array) <= index:
                array.append(Number('int', 0))
            return array[index]
            
        return curr_scope[item]

    def new_frame(self, frame_name):
        self.stack.new_frame(frame_name, self.global_frame.current_scope)

    def del_frame(self):
        self.stack.del_frame()

    def new_scope(self):
        self.stack.current_frame.new_scope()

    def del_scope(self):
        self.stack.current_frame.del_scope()

    def __repr__(self):
        return "{}\nStack\n{}\n{}".format(
            self.global_frame,
            '=' * 40,
            self.stack
        )

    def __str__(self):
        return self.__repr__()


