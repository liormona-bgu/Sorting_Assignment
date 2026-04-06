# Sorting_Assignment
Lior Monasevich - 212071401
Liron Fried - 212211825
Part B:
In this part of the assignment, we conducted a comparative experiment to evaluate the runtime performance of three sorting algorithms. We chose to use:
- Insertion Sort
- Merge Sort
- Bubble Sort

We tested the array sizes: 100, 500, 1000, 5000, 7500, 10000, and repeated the experiment for each size 5 times using different random arrays (the same size). 

For each array size, each sorting algorithm was executed on a copy of the same array, and the runTime of the execution was saved.

For each algorithm and input size, we calculated:
Average runtime (mean)
Standard deviation (STD)

The standard deviation represents the variability of the runtime across different runs, giving insight into the stability of each algorithm.

The results are presented in the result1.png file.
The plot is added to the repository (result1.png file) and includes:
- A line for the average runtime of each algorithm across various array sizes.
- A shaded region representing the standard deviation around the mean.

In the plot, the difference in growth rates between algorithms is displayed. 
Merge Sort performs significantly better for large inputs (O(n log n))
Insertion Sort and Bubble Sort show slower growth (O(n²))
Variance increases with input size, especially for the slower algorithms
