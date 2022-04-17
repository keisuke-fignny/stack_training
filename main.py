from myStack import MyStack

stack = MyStack()

print(f'stacked {stack.push("hello")}')
print(f'stacked {stack.push("good-evening")}')
print(f'stacked {stack.push("zzzzz")}')

print(f'-----------------------------------')

print(f'popped {stack.pop()}')
print(f'popped {stack.pop()}')
print(f'popped {stack.pop()}')

