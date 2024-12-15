Insertion Sort is a simple comparison-based sorting algorithm that works by building a sorted section of the list, one element at a time. It is particularly efficient for small datasets and lists that are already partially sorted.

Insertion Sort has a time complexity of O(n²) in the worst case, which makes it inefficient for larger datasets. However, it is easy to implement and efficient for small or partially sorted arrays.

## How it Works:

1)Start from the Second Element: The algorithm starts with the second element (considering the first element as already sorted).

2)Compare and Move: For each element in the unsorted section, it is compared with elements in the sorted section:

If the current element is smaller than the previous element, it continues comparing    with the previous elements until it finds its correct position.

During this process, the elements are shifted one position to the right to make space for the current element.

3)Insert at the Right Position: Once the correct position is found, the current element is placed there.

4)Repeat for All Elements: This process continues for all elements until the entire list is sorted.

## Example:

Consider the list [8, 4, 3, 7, 6]:

First Pass: Start with 4. Compare it with 8, and since 4 is smaller, move 8 to the right and place 4 before it. List becomes: [4, 8, 3, 7, 6].

Second Pass: Take 3. Compare it with 8 and 4. Since 3 is smaller, move both 8 and 4 to the right and place 3 before them. List becomes: [3, 4, 8, 7, 6].

Subsequent Passes: Continue this process until the entire list is sorted.


## Insertion Sort Visualization

This project provides a simple visualization of the Insertion Sort algorithm using Python and Matplotlib. The visualization demonstrates how the algorithm works by showing the step-by-step process of comparing, moving, and inserting elements in an array.

## Prerequisites 
To run this code, you will need:

Python 3.x

Matplotlib library

You can install Matplotlib using pip:
 ```bash
   pip install matplotlib
   ```
## Running the Visualization
The code generates a list of random integers and visualizes the sorting process. To run the visualization:

Save the script as insertion_sort_visual.py.

Run the script using Python:
 ```bash
   python insertion_sort_visual.py
   ```
## How the Visualization Works
The algorithm iteratively takes one element at a time and places it in the correct position relative to the already sorted part of the list.

If an element is smaller than its predecessor, it is compared with previous elements until it finds the right position.

The visualization uses bars to represent the elements, and the bars being compared or moved are highlighted in red.

The process continues until the entire list is sorted, which is then displayed in a final sorted visualization.

## Features

Step-by-step visualization of the Insertion Sort algorithm.

Comparisons and movements are highlighted in red for better understanding.

The sorting process is intentionally slowed down for easier comprehension.

## Example
An array of 11 random elements is generated, and the sorting process is displayed in real time.

## Customization
You can change the number of elements in the list by modifying the line:
 ```bash
   arr = [random.randint(1, 100) for _ in range(11)]
   ```
You can also adjust the speed of the visualization by modifying the plt.pause() value.


## License

This project is open source and available under [MIT](https://choosealicense.com/licenses/mit/)
