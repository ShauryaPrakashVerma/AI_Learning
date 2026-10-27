# Problem: Simulate an operation that randomly succeeds or fails. Retry failed operations, but stop after three retries.
# - State: attempts, success, max_retries
# - Nodes: run_operation, check_result
# - Conditional edge: Success, retry, or failure.
# Learn: Retry logic, bounded loops, failure handling.