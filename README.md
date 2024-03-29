[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/LeonardoAlchieri/effect-size/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/LeonardoAlchieri/effect-size/blob/main/LICENSE)
[![PyPI pyversions](https://img.shields.io/badge/Python-3.10-informational)](https://github.com/LeonardoAlchieri/effect-size)

# Effect size package

Python package to calculate affect sizes (Cohen's δ, Hedge's g, Cliff's δ and Vargha-Delaney's A)

At the moment, only Cliff's δ is implemented. The other effect sizes will be added soon.

## Usage

```python
from effect_size_analysis.cliff_delta import cliff_delta
from numpy.random import rand

x: ndarray = rand(100)
y: ndarray = rand(100)
cliff_delta(s1=x,s2=y,alpha=0.05,accurate_ci=True)
```
```
(0.0136, (-0.1455859031658134, 0.17209949612394954))
```
The first value is the delta value, while the second tuple represents the confidence interval.

## Citation

If you use this work, please consider citing the following paper:
* Alchieri, Leonardo, et al. "Lateralization Effects in Electrodermal Activity Data Collected Using Wearable Devices." Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 8.1 (2024): 1-30.
```bibtex
@article{alchieri2024lateralization,
  title={Lateralization Effects in Electrodermal Activity Data Collected Using Wearable Devices},
  author={Alchieri, Leonardo and Abdalazim, Nouran and Alecci, Lidia and Gashi, Shkurta and Gjoreski, Martin and Santini, Silvia},
  journal={Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  volume={8},
  number={1},
  pages={1--30},
  year={2024},
  publisher={ACM New York, NY, USA}
}
```

## Contacts
For any information, contact me, Leonardo Alchieri, at leonardo@alchieri.eu. This package was developed as part of my PhD at USI (Università della Svizzera italiana), Switzerland.

