# Rainflow Counting Module

A function for counting cycles according to the Rainflow Method.

The cycle counting method implemented here is based on Downing's 
Method 1 defined in the paper "Simple rainflow counting algorithms" 
by S.D.Downing & D.F.Socie, International Journal of Fatigue, January 1982.

This method is for limited histories where the data has been obtained 
and stored. Method 2 from the same paper (not implemented here) is 
designed for open-ended histories, typically used in a monitoring situation.

**numba** is used to speed up the actual rainflow counting algorithm.

**numpy** is used for the data manipulation required for the method. 

The result is quite a fast implementation.

## Example Useages

### Floating Point Data

```python
import numpy as np

import rainflow

# .... retrieve stored time series data as a 1D numpy float array.

ranges, means = rainflow.ranges_means(data)
```

### Using Integer Data

Sometimes it makes sense to convert real data into integral data
in order to eliminate very small ranges and avoid creating many
cycles of small ranges that have no effect.

Unless the data units are already such that 1 unit is a sensible
rounding limit, the data will have to be scaled so that significant data
is not lost.

```python
import numpy as np

import rainflow

# .... retrieve stored time series data as a 1D numpy float array.

scale = 10.0

ranges, means = rainflow.get_int_ranges_means(data, scale)

ranges /= scale
means /= scale
```
