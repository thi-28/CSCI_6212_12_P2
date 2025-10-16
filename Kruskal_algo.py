"""
Kruskal's Minimum Spanning Tree implementation in Python.

Author: Prathi Patil S
Date: 2025-10-15

Notes:
- Uses built-in Python sorting; no custom sort implementation required.
- Employs a Union-Find (Disjoint Set) data structure for cycle detection.
"""

from typing import List, Tuple
import time
import math
import random
import gc
import matplotlib.pyplot as plt
import unittest


class UnionFind:
    #Union-Find (Disjoint Set)) with path compression and union by rank.
    def __init__(self, size: int) -> None:
        self.parent: List[int] = list(range(size))
        self.rank: List[int] = [0] * size

    def find(self, node: int) -> int: #Find node with path compression.
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a: int, b: int) -> bool: #Union the sets of a and b
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False # Already connected
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        return True


#Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph
def kruskal_mst(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:

    edges.sort(key=lambda x: x[0])  # Sort by weight O(m log n)
    
    # Initialize empty MST and weight accumulator
    T = []
    total_weight = 0
    
    uf = UnionFind(n)

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v): 
            T.append((weight, u, v)) #Edge added to the MST since no cycle is formed
            total_weight += weight
            uf.union(u, v) # Merge the components containing u and v to avoid cycle formation

            if len(T) == n - 1: # Early termination: MST is complete when it has n-1 edges
                return T, total_weight

    # Returns MST was built (may be partial if graph is disconnected)
    return T, total_weight


def generate_graph(n: int) -> List[Tuple[int, int, int]]:
    """Generate complete graph with n vertices and random weights."""
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((random.randint(1, 100), i, j))
    return edges


def theoretical_units_graph(n: int) -> float: # Theoretical units: m log n for a graph with n vertices
    m = n*(n-1)//2
    return float(m) * math.log2(n)


def experimental_time_graph(n: int) -> Tuple[int, int]: # Runtime in ns, returns (time, edge_count)
    edges = generate_graph(n)
    gc.collect()
    start = time.perf_counter_ns()
    _ = kruskal_mst(n, edges)
    elapsed = time.perf_counter_ns() - start
    return elapsed, len(edges)


def analyze_linear_graphs(n_values: List[int]) -> None:
    """Run experimental vs theoretical analysis over n_values and print detailed table."""
    print("\nDetailed Analysis Results:")
    print("=" * 80)
    print(f"{'n':<6} {'Edges':<8} {'Exp_Time(ns)':<15} {'Theory_Units':<12} {'Scale':<12} {'Adj_Theory(ns)':<15} {'Ratio':<8}")
    print("=" * 80)
    
    exp_times: List[int] = []
    theory_units: List[float] = []
    edges_counts: List[int] = []
    
    for n in n_values:
        exp_ns, m = experimental_time_graph(n)
        th_units = theoretical_units_graph(n)
        exp_times.append(exp_ns)
        theory_units.append(th_units)
        edges_counts.append(m)  # Use actual edge count from graph generation
    
    # Calculate scaling constant C using least squares method
    numerator = sum(e * t for e, t in zip(exp_times, theory_units))
    denominator = sum(t * t for t in theory_units)
    scale = (numerator / denominator) if denominator > 0 else 0.0
    
    for n, m, exp_ns, th_units in zip(n_values, edges_counts, exp_times, theory_units):
        adj_theory = int(scale * th_units)
        ratio = (exp_ns / adj_theory) if adj_theory > 0 else float('inf')
        print(f"{n:<6} {m:<8} {exp_ns:<15} {th_units:<12.4f} {scale:<12.6f} {adj_theory:<15} {ratio:<8.4f}")
    
    print("=" * 80)
    print(f"Scaling constant: {scale:.6f}")
    
    # Plot the results with least squares scaled theoretical values
    theo_scaled = [scale * th for th in theory_units]
    plot_results(n_values, exp_times, [int(t) for t in theo_scaled])


def plot_results(ns: List[int], exp_times_ns: List[int], adjusted_theory_ns: List[int]) -> None:
    """Plot nodes (n) vs time for experimental and adjusted theoretical curves."""
    plt.figure(figsize=(9, 6))
    plt.plot(ns, exp_times_ns, marker='o', label='Experimental (ns)')
    plt.plot(ns, adjusted_theory_ns, marker='s', label='Adjusted Theoretical (ns)')
    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Time (ns)')
    plt.title("Kruskal's MST: Experimental vs Adjusted Theoretical Time")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
class TestUnionFind(unittest.TestCase):
    def test_initialization(self):
        uf = UnionFind(5)
        self.assertEqual(uf.parent, [0, 1, 2, 3, 4])
        self.assertEqual(uf.rank, [0, 0, 0, 0, 0])

    def test_find_single_element(self):
        uf = UnionFind(3)
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(2), 2)

    def test_union_different_elements(self):
        uf = UnionFind(3)
        result = uf.union(0, 1)
        self.assertTrue(result)
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertNotEqual(uf.find(0), uf.find(2))

    def test_union_same_elements(self):
        uf = UnionFind(3)
        uf.union(0, 1)
        result = uf.union(0, 1)  # Already connected
        self.assertFalse(result)

    def test_path_compression(self):
        uf = UnionFind(5)
        # Create a chain: 0->1->2->3->4
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        uf.union(3, 4)
        
        # Find should compress the path
        root = uf.find(4)
        self.assertEqual(root, 0)  # All should point to root 0
        # After path compression, parent[4] should directly point to root
        self.assertEqual(uf.parent[4], 0)

    def test_union_by_rank(self):
        uf = UnionFind(4)
        # Union smaller tree to larger tree
        uf.union(0, 1)  # rank[0] = 1
        uf.union(2, 3)  # rank[2] = 1
        uf.union(0, 2)  # Should attach smaller tree to larger
        
        # All should be connected
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertEqual(uf.find(0), uf.find(3))

    def test_complex_union_sequence(self):
        uf = UnionFind(6)
        # Union sequence: (0,1), (2,3), (4,5), (1,3), (3,5)
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)
        uf.union(1, 3)
        uf.union(3, 5)
        
        # All elements should be in same component
        root = uf.find(0)
        for i in range(6):
            self.assertEqual(uf.find(i), root)


class TestKruskalMST(unittest.TestCase):
    def test_single_vertex(self):
        n = 1
        edges: List[Tuple[int, int, int]] = []
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(mst, [])
        self.assertEqual(total, 0)

    def test_two_vertices_single_edge(self):
        n = 2
        edges = [(10, 0, 1)]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 1)
        self.assertEqual(total, 10)
        self.assertEqual(mst[0], (10, 0, 1))

    def test_two_vertices_two_edges_parallel(self):
        n = 2
        edges = [(50, 0, 1), (5, 0, 1)]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 1)
        self.assertEqual(total, 5)
        self.assertEqual(mst[0], (5, 0, 1))

    def test_three_vertices_triangle(self):
        n = 3
        edges = [(3, 0, 2), (1, 0, 1), (2, 1, 2)]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 2)
        self.assertEqual(total, 3)
        self.assertIn((1, 0, 1), mst)
        self.assertIn((2, 1, 2), mst)

    def test_complete_graph_four_vertices(self):
        n = 4
        edges = [
            (3, 0, 1), (1, 0, 2), (4, 0, 3),
            (2, 1, 2), (6, 1, 3),
            (5, 2, 3),
        ]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 3)
        self.assertEqual(total, 1 + 2 + 4)

    def test_disconnected_vertices(self):
        n = 4
        edges = [(2, 0, 1), (3, 1, 2)]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 2)
        self.assertEqual(total, 5)

    def test_duplicate_weights(self):
        n = 5
        edges = [
            (10, 0, 1), (10, 1, 2), (10, 2, 3), (10, 3, 4),
            (10, 0, 2), (10, 1, 3), (10, 2, 4)
        ]
        mst, total = kruskal_mst(n, edges)
        self.assertEqual(len(mst), 4)
        self.assertEqual(total, 40)

    def test_experimental_analysis(self):
        n_values = [100, 200, 300, 400, 500]
        random.seed(123)
        analyze_linear_graphs(n_values)


if __name__ == "__main__":
    import sys
    
    # Check if user wants to run unit tests
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Running unit tests...")
        unittest.main(argv=[''], exit=False)
    else:
        # Run experimental analysis using the updated function
        print("Running experimental analysis...")
        n_values = [100, 200, 300, 400, 500, 700, 1000, 2000, 2500, 3000, 3500, 4000, 
                   5000]
        analyze_linear_graphs(n_values)


