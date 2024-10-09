# Pascal's Triangle in Python

## Description
This project implements a Python function, `pascal_triangle(n)`, that returns a list of lists representing Pascal's triangle up to the `n`th row. Pascal's triangle is a triangular array of the binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

For example, Pascal's triangle for `n = 5` is:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Function
### `def pascal_triangle(n):`
This function generates Pascal's triangle up to `n` rows.
- **Parameter**: `n` (int) - The number of rows of Pascal's triangle to generate.
- **Returns**: A list of lists representing Pascal's triangle.
  - If `n <= 0`, the function returns an empty list.

## Usage

You can import the function into your Python script and use it to generate and print Pascal's triangle.

### Example

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

This script will output the following:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Edge Cases
- If `n <= 0`, the function returns an empty list.
- The function assumes `n` is always an integer.

## Installation

To use this function in your project:

1. Clone or download the project.
2. Import the `pascal_triangle` function from the `0-pascal_triangle.py` file into your Python script.

## Example Output

Here is an example output for `pascal_triangle(5)`:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## License

This project is open-source and free to use. You can modify and distribute it under the terms of the MIT License.

---

Enjoy working with Pascal's Triangle in Python!
