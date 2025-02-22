---

# AI Lab 3111 - README

Welcome to the repository for **AI Lab 3111**! This lab covers fundamental and advanced topics in Artificial Intelligence, including **Markov Decision Processes (MDP)**, **Game Theory (Minimax + Alpha-Beta Pruning)**, **Search Algorithms (DFS, BFS, UCS, A*)**, **Sorting Algorithms (Heap Sort, Binary Search, Selection Sort)**, and **Data Structures (Stack, Queue)**. The implementations are provided using both **custom libraries** and **built-in Python libraries**.

Below is an organized breakdown of the topics covered, along with sections for code implementation. **ASCII diagrams** are included to help visualize key concepts.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Data Structures](#data-structures)
   - [Stack](#stack)
     - [Custom Implementation](#custom-implementation)
     - [Built-in Implementation](#built-in-implementation)
   - [Queue](#queue)
     - [Custom Implementation](#custom-implementation-1)
     - [Built-in Implementation](#built-in-implementation-1)
3. [Search Algorithms](#search-algorithms)
   - [Depth First Search (DFS)](#depth-first-search-dfs)
     - [Custom Stack Implementation](#custom-stack-implementation)
     - [Built-in Stack Implementation](#built-in-stack-implementation)
   - [Breadth First Search (BFS)](#breadth-first-search-bfs)
     - [Custom Queue Implementation](#custom-queue-implementation)
     - [Built-in Queue Implementation](#built-in-queue-implementation)
   - [Uniform Cost Search (UCS)](#uniform-cost-search-ucs)
   - [A* Search](#a-search)
4. [Sorting Algorithms](#sorting-algorithms)
   - [Heap Sort](#heap-sort)
     - [Reheap Down](#reheap-down)
     - [Reheap Up](#reheap-up)
   - [Binary Search](#binary-search)
   - [Selection Sort](#selection-sort)
5. [Game Theory](#game-theory)
   - [Tic Tac Toe](#tic-tac-toe)
   - [Minimax Algorithm](#minimax-algorithm)
   - [Alpha-Beta Pruning](#alpha-beta-pruning)
6. [Markov Decision Process (MDP)](#markov-decision-process-mdp)
   - [Policy Evaluation](#policy-evaluation)
   - [Value Iteration](#value-iteration)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

This repository contains implementations of various algorithms and concepts covered in AI Lab 3111. The goal is to provide a clear understanding of how these algorithms work and their practical applications. Each section includes a brief explanation of the concept, corresponding Python code, and **ASCII diagrams** where applicable.

---

## Data Structures

### Stack

A **Stack** is a linear data structure that follows the Last In, First Out (LIFO) principle.

#### Custom Implementation

```python
# stack.py
class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1

    def push(self, n):
        if self.top < len(self.stack) - 1:  # Checking if the stack is not full
            self.top += 1
            self.stack[self.top] = n
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:  # Checking if the stack is not empty
            popped_value = self.stack[self.top]
            self.top -= 1
            return popped_value
        else:
            print("Stack Underflow")
            return None

    def is_empty(self):
        return self.top == -1
```

#### Built-in Implementation

Python's built-in list can be used as a stack.

```python
# Using Python's built-in list as a stack
stack = []

# Push operation
stack.append(10)
stack.append(20)

# Pop operation
popped_value = stack.pop()  # Removes and returns the last element
print(popped_value)  # Output: 20

# Check if stack is empty
is_empty = len(stack) == 0
```

#### ASCII Diagram of a Stack

```
Push Operations:
Initial Stack: []
After Push(10): [10]
After Push(20): [10, 20]

Pop Operation:
After Pop(): [10]
```

---

### Queue

A **Queue** is a linear data structure that follows the First In, First Out (FIFO) principle.

#### Custom Implementation

```python
# queue.py
class Queue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail == self.k - 1):  # Queue is full
            print("The queue is full")
        else:
            if self.head == -1:  # Set head to 0 when enqueuing the first element
                self.head = 0
            self.tail += 1
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1 or self.head > self.tail:  # Queue is empty
            print("The queue is empty")
            return None
        else:
            temp = self.queue[self.head]
            self.head += 1
            if self.head > self.tail:  # Reset the queue if empty
                self.head = self.tail = -1
            return temp  # Return the dequeued value

    def printQueue(self):
        if self.head == -1:
            print("The queue is empty")
        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
```

#### Built-in Implementation

Python's `collections.deque` can be used as a queue.

```python
from collections import deque

# Initialize a deque as a queue
queue = deque()

# Enqueue operation
queue.append(10)
queue.append(20)

# Dequeue operation
dequeued_value = queue.popleft()  # Removes and returns the first element
print(dequeued_value)  # Output: 10

# Check if queue is empty
is_empty = len(queue) == 0
```

#### ASCII Diagram of a Queue

```
Enqueue Operations:
Initial Queue: []
After Enqueue(10): [10]
After Enqueue(20): [10, 20]

Dequeue Operation:
After Dequeue(): [20]
```

---

## Search Algorithms

### Depth First Search (DFS)

DFS explores as far as possible along each branch before backtracking.

#### Custom Stack Implementation

Using the custom stack implementation (`stack.py`).

```python
# dfs.py
from stack import Stack  # Importing custom Stack class

def dfs(graph, start_node):
    visited = set()
    stack = Stack(100)  # Initializing a stack with size 100 or adjust as needed
    stack.push(start_node)
    while not stack.is_empty():  # While the stack is not empty
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
        # Adding neighbors to the stack
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                stack.push(neighbor)
```

#### Built-in Stack Implementation

Using Python's built-in list as a stack.

```python
# dfs_builtin.py
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]  # Using list as a stack

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
        # Adding neighbors to the stack
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                stack.append(neighbor)
```

#### ASCII Diagram of DFS Tree

```
Graph:
       A
      / \
     B   C
    / \   \
   D   E   F

DFS Traversal (Starting from A): A -> C -> F -> B -> E -> D
```

---

### Breadth First Search (BFS)

BFS explores all neighbors at the present depth level before moving on to nodes at the next depth level.

#### Custom Queue Implementation

Using the custom queue implementation (`queue.py`).

```python
# bfs.py
from queue import Queue

def bfs(graph, start_node):
    visited = set()
    q = Queue(len(graph))  # Initializing custom queue with size
    q.enqueue(start_node)
    visited.add(start_node)
    while q.head != -1:  # While the queue is not empty
        current_node = q.dequeue()
        if current_node is None:
            continue  # Skipping if no more nodes
        print(current_node, end=" ")
        for neighbor in graph.get(current_node, []):  # Ensuring graph has the node
            if neighbor not in visited:
                q.enqueue(neighbor)
                visited.add(neighbor)
```

#### Built-in Queue Implementation

Using Python's `collections.deque` as a queue.

```python
# bfs_builtin.py
from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])  # Using deque as a queue
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
```

#### ASCII Diagram of BFS Tree

```
Graph:
       A
      / \
     B   C
    / \   \
   D   E   F

BFS Traversal (Starting from A): A -> B -> C -> D -> E -> F
```

---

---

### Uniform Cost Search (UCS)

UCS expands the least-cost node first.

```python
import heapq

def ucs(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [start])]  # (cost, node, path)

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return cost, path
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return None
```

#### ASCII Diagram of UCS Priority Queue

```
Priority Queue:
[(0, 'A', ['A'])]
Expanding A -> [(1, 'B', ['A', 'B']), (4, 'C', ['A', 'C'])]
Expanding B -> [(2, 'D', ['A', 'B', 'D']), (5, 'E', ['A', 'B', 'E'])]
```

---

### A* Search

A* uses both the cost to reach the node and a heuristic estimate to find the optimal path.

```python
import heapq

def astar(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic(start, goal), 0, start, [start])]  # (f, g, node, path)

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return g, path
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (g + cost + heuristic(neighbor, goal), g + cost, neighbor, path + [neighbor]))
    return None
```

#### ASCII Diagram of A* Search Tree

```
Graph:
       A (h=6)
      / \
     B(h=4) C(h=5)
    / \   \
   D(h=2) E(h=3) F(h=0)

A* Traversal (Starting from A): A -> B -> D -> F
```

---

## Sorting Algorithms

### Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

#### ASCII Diagram of a Max Heap

```
Max Heap:
        9
       / \
      7   6
     / \   \
    5   4   3
```

---

### Reheap Down

Reheap Down ensures the heap property is maintained when moving down the heap.

```python
def reheap_down(heap, index, size):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    smallest = index

    if left_child < size and heap[left_child] < heap[smallest]:
        smallest = left_child

    if right_child < size and heap[right_child] < heap[smallest]:
        smallest = right_child

    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        reheap_down(heap, smallest, size)
```

#### ASCII Diagram of Reheap Down

```
Before Reheap Down:
        3
       / \
      7   6
     / \   \
    5   4   9

After Reheap Down:
        9
       / \
      7   6
     / \   \
    5   4   3
```

---

### Reheap Up

Reheap Up ensures the heap property is maintained when moving up the heap.

```python
def reheap_up(heap, index):
    parent = (index - 1) // 2

    if index > 0 and heap[index] < heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        reheap_up(heap, parent)
```

#### ASCII Diagram of Reheap Up

```
Before Reheap Up:
        9
       / \
      7   6
     / \   \
    5   4   3

After Reheap Up:
        3
       / \
      7   6
     / \   \
    5   4   9
```

---

### Binary Search

Binary Search is an efficient algorithm for finding an item from a sorted list of items.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

#### ASCII Diagram of Binary Search

```
Array: [1, 3, 5, 7, 9, 11]
Target: 7

Step 1: Low = 0, High = 5, Mid = 2 (Value = 5)
Step 2: Low = 3, High = 5, Mid = 4 (Value = 9)
Step 3: Low = 3, High = 3, Mid = 3 (Value = 7) -> Found!
```

---

### Selection Sort

Selection Sort divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

#### ASCII Diagram of Selection Sort

```
Initial Array: [9, 2, 6, 5, 3]

Step 1: Swap 9 and 2 -> [2, 9, 6, 5, 3]
Step 2: Swap 9 and 3 -> [2, 3, 6, 5, 9]
Step 3: Swap 6 and 5 -> [2, 3, 5, 6, 9]
```

---

## Game Theory

### Tic Tac Toe

Implementation of the classic Tic Tac Toe game.

```python
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
```

#### ASCII Diagram of Tic Tac Toe Board

```
Initial Board:
   |   |  
-----------
   |   |  
-----------
   |   |  

After Moves:
 X | O |  
-----------
   | X |  
-----------
   |   | O
```

---

### Minimax Algorithm

The Minimax algorithm is used in decision-making and game theory to find the optimal move for a player.

```python
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
```

#### ASCII Diagram of Minimax Tree

```
Game Tree:
         Root
        / | \
       X1 X2 X3
      /  |  |  \
     O1  O2 O3  O4
    /    |  |    \
   X5    X6 X7    X8
```

---

### Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm.

```python
def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score
```

#### ASCII Diagram of Alpha-Beta Pruning

```
Game Tree:
         Root
        / | \
       X1 X2 X3
      /  |  |  \
     O1  O2 O3  O4
    /    |  |    \
   X5    X6 X7    X8

Pruned Branches:
         Root
        / | \
       X1 X2 X3
      /  |  |  
     O1  O2 O3  
    /    |  
   X5    X6  
```

---

## Markov Decision Process (MDP)

### Policy Evaluation

Policy evaluation computes the value function for a given policy.

```python
def policy_evaluation(policy, env, gamma=0.9, theta=1e-6):
    V = {state: 0 for state in env.get_all_states()}
    while True:
        delta = 0
        for state in env.get_all_states():
            v = V[state]
            action = policy[state]
            V[state] = sum(prob * (reward + gamma * V[next_state]) for prob, next_state, reward in env.get_transitions(state, action))
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break
    return V
```

---

### Value Iteration

Value iteration finds the optimal value function by iteratively updating the value of each state.

```python
def value_iteration(env, gamma=0.9, theta=1e-6):
    V = {state: 0 for state in env.get_all_states()}
    while True:
        delta = 0
        for state in env.get_all_states():
            v = V[state]
            V[state] = max(sum(prob * (reward + gamma * V[next_state]) for prob, next_state, reward in env.get_transitions(state, action)) for action in env.get_possible_actions(state))
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break
    return V
```

---

## Contributing

Feel free to contribute to this repository by opening issues or submitting pull requests. Any improvements or additional implementations are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
