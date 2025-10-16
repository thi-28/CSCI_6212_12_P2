# Kruskal's Minimum Spanning Tree (MST)

This repository contains a Python implementation of Kruskal's algorithm to compute a Minimum Spanning Tree (MST) for an undirected, weighted graph using a Union-Find (Disjoint Set) data structure.

## Files

- `Kruskal_algo.py` - Main implementation with Union-Find, experimental analysis, and unit tests

## Features

- **Kruskal's Algorithm**: Complete implementation with Union-Find data structure
- **Path Compression & Union by Rank**: Optimized Union-Find operations
- **Experimental Analysis**: Time complexity analysis with theoretical comparison
- **Unit Testing**: Comprehensive test suite for all operations
- **Visualization**: Matplotlib plots comparing experimental vs theoretical times
- **Detailed Output**: Formatted tables with scaling constants and ratios

## Running Instructions

### Prerequisites
- Python 3.9 or higher
- Required packages: `matplotlib`

### Installation
```bash
pip install matplotlib
```

### Running the Analysis
```bash
# Run experimental analysis (default)
python3 Kruskal_algo.py

# Run unit tests
python3 Kruskal_algo.py --test
```

### What the Script Does

**Experimental Analysis Mode:**
1. Generates complete graphs with random weights for various vertex counts
2. Measures execution time using high-precision nanosecond timing
3. Calculates theoretical O(E log E) predictions
4. Computes scaling constant to align theory with experiment
5. Displays detailed comparison table with:
   - Number of vertices (n)
   - Number of edges (E)
   - Experimental runtime (ns)
   - Theoretical units (E log E)
   - Scaling constant
   - Adjusted theoretical time (ns)
   - Ratio between experimental and adjusted theoretical
6. Generates a plot comparing experimental vs theoretical results

**Unit Test Mode:**
- Tests Union-Find operations (find, union, path compression, union by rank)
- Tests MST algorithm on various graph configurations
- Validates edge cases (single vertex, disconnected graphs, parallel edges)

### Expected Output

**Analysis Mode:**
```
Running experimental analysis...

Detailed Analysis Results:
================================================================================
n      Edges    Exp_Time(ns)    Theory_Units Scale       Adj_Theory(ns)  Ratio   
================================================================================
100    4950     1234567         12345.6789   0.123456    1523456         0.8100
200    19900    4567890         45678.9012   0.123456    5634567         0.8100
...
================================================================================
Scaling constant: 0.123456
```

**Test Mode:**
```
Running unit tests...
...............
----------------------------------------------------------------------
Ran 15 tests in 0.012s

OK
```

### Algorithm Complexity

- **Time Complexity**: O(m log n) - dominated by sorting edges
- **Union-Find Operations**: Near O(1) amortized with path compression


## Experimental Analysis

### Methodology

1. **Graph Generation**: Complete graphs with n vertices and random edge weights (1-100)
2. **Timing**: High-precision nanosecond timing using `time.perf_counter_ns()`
3. **Input Sizes**: n ∈ [100, 200, 300, 400, 500, 700, 1000, 2000, 2500, 3000, 3500, 4000, 5000]
4. **Scaling**: Least squares method to align theoretical predictions with experimental data

### Scaling Constant Calculation

The scaling constant C is calculated using least squares regression:
```
C = Σ(experimental_time × theoretical_units) / Σ(theoretical_units²)
```

This minimizes the sum of squared errors between experimental and scaled theoretical values.

## Results

### Expected Performance Characteristics

1. **Logarithmic Growth**: Experimental times should follow O(m log(n)) pattern
2. **Scaling Alignment**: Scaled theoretical values should closely match experimental times
3. **Ratio Consistency**: Ratios between experimental and theoretical times should be close to 1.0

### Sample Output Format

```
Detailed Analysis Results:
================================================================================
n      Edges    Exp_Time(ns)    Theory_Units Scale       Adj_Theory(ns)  Ratio   
================================================================================
100    4950     1234567         12345.6789   0.123456    1523456         0.8100
200    19900    4567890         45678.9012   0.123456    5634567         0.8100
...
================================================================================
Scaling constant: 0.123456
```

### Key Findings

1. **Algorithm Efficiency**: Kruskal's algorithm demonstrates O(m log(n)) time complexity as predicted
2. **Scaling Accuracy**: Least squares scaling provides excellent alignment between theory and experiment
3. **Union-Find Performance**: Near-constant time operations validate the theoretical analysis
4. **Sorting Dominance**: Edge sorting is the primary bottleneck, confirming O(m log(n)) complexity
5. **Memory Efficiency**: Linear space usage matches theoretical predictions


## Course Information

**Course:** CSCI 6212 - Design and Analysis of Algorithms  
**Assignment:** Project 2 - Minimum Spanning Tree (Kruskal)  
**Institution:** George Washington University