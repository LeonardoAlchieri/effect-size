[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/LeonardoAlchieri/effect-size/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/LeonardoAlchieri/effect-size/blob/main/LICENSE)
[![PyPI pyversions](https://img.shields.io/badge/Python-3.10-informational)](https://github.com/LeonardoAlchieri/effect-size)

# Effect size package

Python package to calculate affect sizes (Cohen's δ, Hedge's g, Cliff's δ and Vargha-Delaney's A)

At the moment, only Cliff's δ is implemented. The other effect sizes will be added soon.

## Usage

```python
from effect_size_analysis import cliff_delta
from numpy.random import rand

x: ndarray = rand(100)
y: ndarray = rand(100)
cliff_delta(s1=x,s2=y,alpha=0.05,accurate_ci=True)
```
```
(0.0136, (-0.1455859031658134, 0.17209949612394954))
```
The first value is the delta value, while the second tuple represents the confidence interval.
