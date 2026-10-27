# Problem: Start with a number and increment it until it reaches a target.
# - State: number, target, attempts
# - Node: increment_number
# - Conditional edge: Continue while number < target; otherwise finish.
# Learn: State updates, loops, termination conditions.

# Extension: Stop after a maximum of 10 attempts.

from typing import TypedDict
from langgraph.graph import END, StateGraph

