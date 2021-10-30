# Cell Count

This package takes a binary array, and counts the number
of seperate objects in the array.


## Installation

Run the following to install:

```python
pip install cellcount
```

## Usage

```python
import cellcount as cc
import numpy as np

img = np.random.randint(2, size=(5,5))

# Count the number of seperate cells
num_of_cells = cc.cellCount(img)
```