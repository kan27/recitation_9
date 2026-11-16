# CMPS 2200 Recitation 09

## Answers

**Name:**_Srikanya Balaji Garuda________________________
**Name:**_________________________


Place all written answers from `recitation-09.md` here for easier grading.



- **2) (2 pts)** What is the worst-case work of your algorithm, assuming $G$ has $k$ connected components?

Worst-case work is still $O(E \log V)$. Though k connected components, each vertex and edge is still processed only once. (uses binary heap)

- **4) (2 pts)** What is the work of your full algorithm in the previous answer?

Work of constructing graph -> $O(V^2)$
Work of prims, acknowledging that E is $V^2$ because fully connected -> $O(V^2 \log V)$

Work of full algorithm = $O(V^2 + V^2\log V)$ or just $O(V^2 \log V)$
