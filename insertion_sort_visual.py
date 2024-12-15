import matplotlib.pyplot as plt
import time
import random

# Visualization of Insertion Sort
def insertion_sort_visualization(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            plt.clf()
            colors = ['skyblue'] * len(arr)
            colors[j] = 'lightcoral'
            colors[j + 1] = 'lightcoral'
            plt.bar(range(len(arr)), arr, color=colors)
            plt.xticks(range(len(arr)), arr, rotation=0)
            plt.title(f"Insertion Sort Step: Moving element at index {j+1}")
            plt.pause(2.0)  # Slower visualization for better understanding
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.xticks(range(len(arr)), arr, rotation=90)
    plt.title("Insertion Sort Completed")
    plt.show()

# Example Insertion Sort visualization
arr = [random.randint(1, 100) for _ in range(11)]
insertion_sort_visualization(arr)
