def is_end(state, N):
    """Checks if we have reached the final block (destination)."""
    return state == N

def get_successors(state, N):
    """Gives us possible moves (actions) from the current block."""
    result = []
    # Option 1: Walk -> move forward by 1 block, cost = 1
    if state + 1 <= N:
        result.append(('walk', state + 1, 1))
    # Option 2: Tram -> move forward by doubling the block number, cost = 2
    if state * 2 <= N:
        result.append(('tram', state * 2, 2))
    return result

# --- Main Dynamic Programming Logic ---

def dynamic_programming_search(N):
    """Finds the cheapest path to N using dynamic programming."""
    start_state = 1
    # cache will store the optimal solution from a given state to the end.
    # Key: state (block number), Value: (cost, action, next_state)
    cache = {}

    def dp_solve(state):
        # Base Case: If we are at the destination, the cost is 0.
        if is_end(state, N):
            return (0, None, None)

        # Memoization: If we already solved for this state, return the cached result.
        if state in cache:
            return cache[state]

        # --- Recursive Step: Calculate the best move from the current state ---
        best_cost = float('+inf')
        best_move = None

        # Explore all possible next moves from the current state
        for action, newState, cost in get_successors(state, N):
            # Recursively find the cost from the *next* state to the end
            future_cost, _, _ = dp_solve(newState)
            total_cost = cost + future_cost

            # If this path is better, update our best choice
            if total_cost < best_cost:
                best_cost = total_cost
                best_move = (action, newState, cost)
        
        # Cache the result for this state before returning
        cache[state] = (best_cost, best_move[0], best_move[1])
        return cache[state]

    # Start the process from the beginning to populate the cache
    dp_solve(start_state)

    # --- Path Reconstruction ---
    history = []
    total_cost = cache[start_state][0]
    current_state = start_state

    while not is_end(current_state, N):
        # Look up the best move from the current state in our cache
        _, action, next_state = cache[current_state]
        step_cost = 1 if action == 'walk' else 2
        history.append((action, next_state, step_cost))
        current_state = next_state

    return total_cost, history

### Main Program
if __name__ == "__main__":
    # Ask user where they want to go
    N = int(input("Enter the block number you want to reach: "))

    # Directly call the search function with N
    cost, history = dynamic_programming_search(N)

    # Show results
    print("\nBest Cost:", cost)
    print("Path taken:")
    current_block = 1
    print(f"Start at block {current_block}")
    for action, next_block, step_cost in history:
        print(f" -> {action} to block {next_block} (cost: {step_cost})")