# Kruskal's Minimum Spanning Tree (MST)

This repository contains a Python implementation of Kruskal's algorithm to compute a Minimum Spanning Tree (MST) for an undirected, weighted graph using a Union-Find (Disjoint Set) data structure.

## Files

- `Kruskal_algo.py` - Main script implementing Kruskal's algorithm with a runnable example

## Running Instructions

### Prerequisites
- Python 3.9 or higher
- No external packages required

### Installation
No installation needed.

### Running the Analysis
```bash
python3 Kruskal_algo.py
```

### What the Script Does
1. Defines an undirected graph with `n = 6` vertices and a list of weighted edges
2. Sorts edges in non-decreasing order of weight
3. Uses Union-Find to add the next lightest edge that does not create a cycle
4. Builds the MST with exactly `n-1` edges (if the graph is connected)
5. Prints the MST edges and the total weight

### Expected Output
- Console output listing MST edges as `(weight, u, v)`
- Console output showing the total MST weight

### Note
To explore time complexity empirically, increase `n` and add more edges in the `edges` list inside `__main__`, then re-run the script.

## Key Findings

Kruskal's algorithm constructs an MST by globally selecting the next lightest safe edge. The overall time complexity is dominated by sorting the edges, yielding O(E log E), with near-constant-time Union-Find operations for cycle detection.

## Course Information

**Course:** CSCI 6212 - Design and Analysis of Algorithms  
**Assignment:** Project 2 - Minimum Spanning Tree (Kruskal)
# Kruskal's Minimum Spanning Tree (MST)

This repository contains an implementation of Kruskal's algorithm to compute a Minimum Spanning Tree (MST) of an undirected, weighted graph using a Union-Find (Disjoint Set) data structure with path compression and union by rank.

## Algorithm Description

The `kruskal_mst` function sorts edges by non-decreasing weight and iteratively adds the next lightest edge that does not create a cycle. Cycle detection is done using Union-Find.

```python
def kruskal_mst(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    # edges: list of (weight, u, v)
    edges.sort()  # Sort edges by weight
    T = []        # Tree (MST) is empty
    j = 0         # Edge counter
    uf = UnionFind(n)
    while len(T) < n - 1 and j < len(edges):
        weight, u, v = edges[j]
        if uf.union(u, v):  # If adding edge does NOT create a cycle
            T.append((weight, u, v))
        j += 1
    return T
```

## Theoretical Analysis

Kruskal's algorithm is dominated by sorting the edges and performing near-constant-time Union-Find operations.

### Key Insights:
- **Sorting edges:** O(E log E)
- **Union-Find operations:** O(E α(V)) amortized (α is inverse Ackermann; ~constant)
- **Total complexity:** O(E log E)

## Experimental Analysis

The `__main__` block includes an example with `n = 6` and larger edge weights. You can scale `n` and the number of edges `E` to observe runtime behavior primarily influenced by the sort step.

### Results:
- Builds an MST with `n-1` edges if the graph is connected
- Prints both the MST edges and the total weight

## Files

- `Kruskal_algo.py` - Main implementation with an example in `__main__`

## Running Instructions

### Prerequisites
- Python 3.9 or higher

### Installation
No third-party packages required.

### Running the Program
```bash
python3 Kruskal_algo.py
```

### What the Script Does
1. Defines an undirected graph with `n = 6` vertices and a list of weighted edges
2. Runs Kruskal's algorithm to compute the MST
3. Prints the selected MST edges and their total weight

### Expected Output
- Console output listing MST edges `(weight, u, v)` and the total weight

### Note
To explore time complexity empirically, increase `n` and the number of edges in the `edges` list and re-run the script.

## Key Findings

Kruskal's algorithm efficiently constructs an MST by globally choosing the next lightest safe edge. Its performance is primarily governed by sorting the edges, yielding an overall time complexity of O(E log E).

## Course Information

**Course:** CSCI 6212 - Design and Analysis of Algorithms  
**Assignment:** Project 2 - Minimum Spanning Tree (Kruskal)  
**Institution:** George Washington University

