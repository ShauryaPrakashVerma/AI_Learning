# Problem: Given a number, choose an operation based on its properties.
# - If even, divide by 2.
# - If odd, multiply by 3 and add 1.
# - Repeat until the number reaches 1.
# - State: number, steps
# - Nodes: check_number, divide_by_two, multiply_and_add
# - Conditional edges: Route to the appropriate operation.
# Learn: Multiple conditional branches, graph cycles, shared state.

# This is based on the Collatz sequence. Add a step limit to prevent unbounded execution.