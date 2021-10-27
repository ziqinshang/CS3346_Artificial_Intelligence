# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    fringe = util.Stack()  # for DFS, the fringe acts like a stack
    fringe.push(
        (problem.getStartState(), [], []))  # creating a tuple of list that contains state, action and visited nodes
    while not fringe.isEmpty():  # when the fringe is not empty,perform following search task
        state, action, visited = fringe.pop()  # take out a state from the fringe, which is the processed state
        if problem.isGoalState(state):  # terminate the task and return the current path if we found the goal
            return path
        # for every child of the current node
        for successor, step, stepcost in problem.getSuccessors(state):
            if not successor in visited:
                fringe.push((successor, action + [step], visited + [state]))
                path = action + [step]

    return []

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()  # for BFS, the fringe acts like a queue
    fringe.push((problem.getStartState(), []))  # creating a tuple of list that contains state and action
    visited = []  # a list to keep track of visited nodes
    while not fringe.isEmpty():  # when the fringe is not empty,perform following search task
        state, action = fringe.pop()  # take out a state from the fringe, which is the processed state
        if (not state in visited):  # if the state is visited, put it in the visited states list
            visited.append(state)
            if problem.isGoalState(state):  # terminate the task and return the current path if we found the goal
                return action
            # for every child of the current node
            for successor, step, stepcost in problem.getSuccessors(state):
                fringe.push((successor, action + [step]))

    return []
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()  # for UCS, the fringe acts like a priority queue
    fringe.push((problem.getStartState(), [], 0), 0)  # creating a tuple of list that contains state, action and costs
    visited_states = []  # a list to keep track of visited nodes

    while not fringe.isEmpty():  # when the fringe is not empty,perform following search task
        state, action, costs = fringe.pop()  # take out a state from the fringe, which is the processed state

        if (not state in visited_states):  # if the state is visited
            visited_states.append(state)  # put it in the visited states list

            if problem.isGoalState(state):  # terminate the task and return the current path if we found the goal
                return action
            # for every child of the current node
            for successor, step, stepcost in problem.getSuccessors(state):
                # record the actions and total cost
                fringe.push((successor, action + [step], costs + stepcost), costs + stepcost)

    return []
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()  # for astar, the fringe acts like a priority queue as well
    # creating a tuple of list that contains state, action and costs for the state,
    # and h(x) value which is for the astar search
    fringe.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    visited = []  # a list to keep track of visited nodes
    while not fringe.isEmpty():  # when the fringe is not empty,perform following search task
        state, action, costs = fringe.pop()  # take out a state from the fringe, which is the processed state
        if not state in visited:  # if the state is visited
            visited.append(state)  # put it in the visited states list

            if problem.isGoalState(state):  # terminate the task and return the current path if we found the goal
                return action
            # for every child of the current node
            for successor, step, stepcost in problem.getSuccessors(state):
                gvalue = costs + stepcost  # the total path cost
                # add g(x) and h(x) together, combining the value which makes it an astar search
                fringe.push((successor, action + [step], costs + stepcost), gvalue + heuristic(successor, problem))
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
