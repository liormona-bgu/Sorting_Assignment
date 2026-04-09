# Sorting_Assignment

Lior Monasevich - 212071401
Liron Fried - 212211825

Part B:
In this part of the assignment, we conducted a comparative experiment to evaluate the runtime performance of three sorting algorithms. We chose to use:
- Insertion Sort
- Merge Sort
- Bubble Sort

We tested the array sizes: 100, 500, 1000, 5000, 7500, 10000, and repeated the experiment for each size 5 times using different random arrays. 

For each array size, each sorting algorithm was executed on a copy of the same array, and the runTime of the execution was saved.

For each algorithm and input size, we calculated the average runtime (mean) and the standard deviation (STD).

The results are presented in the result1.png file added to the repository and include:

- A line for the average runtime of each algorithm across various array sizes.

- A shaded region representing the standard deviation around the mean.

In the plot, the difference in growth rates between algorithms is displayed. 
Merge Sort performs significantly better for large inputs (O(n log n))
Insertion Sort and Bubble Sort performed poorly due to their (O(n²)) complexity

Part C:
In this part, we evaluated performance on sorted arrays to which we added noise.

We reused sorted arrays from Part B and added noise by randomly swapping:

5% of the elements
20% of the elements

Each algorithm was tested under the same conditions as Part B, and the mean and STD were calculated.

Results are shown in the 2 result2.png files added to the repository.

Insertion Sort improves significantly on nearly sorted data, as fewer element shifts are required, and approaches its best-case complexity of O(n).
Merge Sort remains stable and unaffected by input order.
Bubble Sort shows minor improvement but remains inefficient.

Part D:

A Command Line Arguments was implemented using argparse to control:

Algorithms (-a)
Array sizes (-s)
Experiment type/noise level (-e)
Repetitions (-r)



