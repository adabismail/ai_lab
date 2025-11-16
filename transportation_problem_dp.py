# Define a class for the Transportation Problem
class TransportationProblem(object):
    def __init__(self, N):
        # Save the number of blocks (destination)
        self.N = N

    def startState(self):
        # We always start from block number 1
        return 1

    def isEnd(self, state):
        # Check if we have reached the final block (destination)
        return state == self.N

    def succAndCost(self, state):
        # This function gives us possible moves (actions) from the current block
        # Each move is returned as (action, new block, cost of move)
        result = []

        # Option 1: Walk → move forward by 1 block, cost = 1
        if state + 1 <= self.N:  
            result.append(('walk', state + 1, 1))

        # Option 2: Tram → move forward by doubling the block number, cost = 2
        if state * 2 <= self.N:
            result.append(('tram', state * 2, 2))

        # Return all possible moves
        return result


# Function to find the best (cheapest) way to reach the goal using backtracking
def backtrackingSearch(problem):
    # Store the best solution found so far
    best = {
        'cost': float('+inf'),  # Initially set cost to infinity (very large)
        'history': None         # No moves taken yet
    }

    # Recursive function to explore all possible paths
    def recurse(state, history, totalCost):
        # If we have reached the destination
        if problem.isEnd(state):
            # If this path is cheaper than the best found so far → update best
            if totalCost < best['cost']:
                best['cost'] = totalCost
                best['history'] = history
            return  # Stop going further down this path

        # If not at the destination → explore all possible next moves
        for action, newState, cost in problem.succAndCost(state):
            # Add this move to the history and update total cost
            recurse(newState, history + [(action, newState, cost)], totalCost + cost)

    # Start recursion from the start state (block 1), with empty history and 0 cost
    recurse(problem.startState(), history=[], totalCost=0)

    # Return the best cost and the path that achieved it
    return best['cost'], best['history']


### Main Program
if __name__ == "__main__":
    # Ask user: where do you want to go? (final block number)
    N = int(input("Enter the block number you want to reach: "))

    # Create a problem with that destination
    problem = TransportationProblem(N)

    # Run backtracking search to find cheapest path
    cost, history = backtrackingSearch(problem)

    # Show results
    print("\nBest Cost:", cost)  # Total cheapest cost
    print("Path taken:")         # Show the moves
    for step in history:
        print(step)
