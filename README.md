# mathdistops

This package provides statistical functions for normal and exponential distributions, including pnorm, qnorm, pexp, and qexp. Each function not only performs the respective statistical calculation but also generates the corresponding plot of the distribution, offering both numerical results and visual outputs.

![](https://github.com/UBC-MDS/mathdistops/blob/main/img/mathdistops.jpg?raw=true)


[![ci-cd](https://github.com/UBC-MDS/mathdistops/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/mathdistops/actions/workflows/ci-cd.yml) 
[![codecov](https://codecov.io/gh/UBC-MDS/mathdistops/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/mathdistops)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Documentation Status](https://readthedocs.org/projects/mathdistops/badge/?version=latest)](https://mathdistops.readthedocs.io/en/latest/?badge=latest)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/MathDistOps)
[![version](https://img.shields.io/github/v/release/UBC-MDS/mathdistops)](https://github.com/UBC-MDS/mathdistops/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Contributors
Our team listed in alphabetical order:
- Katherine Chen
- Kun Ya
- Oak Chong
- Sandra Gross

## Functions
### Description
- pexp(q, rate=1, graph=True): Represents the Cumulative Distribution Function (CDF) of the exponential distribution characterized by a given parameter `rate`. The function calculates the cumulative probability for a given quantile `q` and plots the corresponding probability distribution (PDF) and the CDF. 

- qexp(p, rate=1, graph=True): Quantile Function of an exponential distribution, characterized by a given rate parameter `rate`. The function calculates the quantile corresponding to given cumulative probability `p` in an exponential distribution. Optionally, it can also generate and return a visualization of the PDF and the CDF.

- pnorm(q, mean = 0, std_dev =1, graph = True): Cumulative Distribution Function of the normal distribution with specified mean and standard deviation. It will return the cumulative probability up to the given value `q`. Optionally, it can generate and return a visualization of the distributions, the PDF and the CDF. 

- qnorm(p, mean=0, std_dev=1, graph=True): Calculates the quantile (Inverse Cumulative Distribution Function) corresponding to a specified cumulative probability `p` of the normal distribution with specified mean and standard deviation. The function can additionally create and provide a graphical representation of the PDF and the CDF.

A detailed documentation of the functions can be found here: https://mathdistops.readthedocs.io/en/latest/autoapi/index.html

### Documentation
A detailed guide and tutorial for using these functions can be found on ReadTheDocs. For specific vignettes on the norm functions, please visit: https://mathdistops.readthedocs.io/en/latest/example_norm.html. Additionally, for comprehensive examples on the usage of qexp and pexp, refer to: https://mathdistops.readthedocs.io/en/latest/example_exp.html.
  

## Installation

### For Users
In order to install the package you can run the command `pip install mathdistops`.

### For Developers
This package uses [Poetry](https://python-poetry.org/) for dependency management and packaging. To install and use this package, please follow these steps:

1. To **create a new virtual environment** in Conda with Python, use the following commands in the terminal: 

```bash
conda create --name mathdistops python=3.9.0 -y
```

2. **Activate the installed environment** via: 

```bash
conda activate mathdistops
```

3. Please **install** and set up **poetry**:

```bash
conda install poetry
```

4. **Install the Package with Poetry**: Use Poetry to install the package and its dependencies.

```bash
poetry install
```

5. Now you are ready to use the mathdistops package!

## Usage

### Using this package

To use this package, you can import and call its functions in your Python scripts. Here's an example:

```python
# Run this on jupyter notebook to import pnorm and qnorm function
from mathdistops import pnorm, qnorm

# Using pnorm to get the cumulative probability and plot for a normal distribution
df_pnorm, fig_pnorm = pnorm(1, mean=0, std_dev=1)
print(df_pnorm)
fig_pnorm
```

The following image displays a sample usage in a Jupyter Notebook:
<img src="https://github.com/UBC-MDS/mathdistops/blob/main/img/usage_sample_pnorm.png?raw=true" style="width: 750px;"/>

Similar to `pnorm` for the normal distribution, `pexp` offers functionality for the exponential distribution. Here's how you can use `pexp` in a Jupyter Notebook:

```python
# Run this on jupyter notebook to import pexp and qexp function
from mathdistops import pexp, qexp

# Using pexp to get the cumulative probability and plot for an exponential distribution
df_pexp, fig_pexp = pexp(1, rate=1)
print(df_pexp)
fig_pexp
```

Below is an illustration of its usage in a Jupyter Notebook:
<img src="https://github.com/UBC-MDS/mathdistops/blob/main/img/usage_sample_pexp.png?raw=true" style="width: 750px;"/>

Regarding `qnorm` and `qexp`, these functions operate similarly, generating a DataFrame that summarizes the data and also producing plots for the `PDF` and `CDF`, with the calculated results indicated on the graphs. However, unlike their counterparts, they accept quantiles as inputs instead of probabilities.


### Running unit tests

To run unit tests for this package, add `pytest` to the environment file, which was created during the installation process via:

```bash
conda install pytest
```

Execute the following in the project root directory: 

```bash
poetry run pytest
```

To get a the code coverage reporting, run this command:

```bash
poetry run pytest --cov=mathdistops
poetry run pytest --cov-branch --cov=mathdistops
```

## Python Ecosystem Integration
While python has relevant functions for normal and exponential distribution in the scipy.stats package, this package offer an in-built additional functionality of returning the plot to help with visualization and understanding the problem. 

### Related Packages:
- [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) is an official scipy package to represent a normal continuous random variable.
- [scipy.stats.expon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html) is an official scipy package to represent an exponential continuous random variable.

## Dependencies

This package necessitates a Python version of 3 or higher. Additional required packages can be found in the [environment file](https://github.com/UBC-MDS/mathdistops/blob/main/environment.yaml) of this repository.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms. Please check our [contributing file](https://github.com/UBC-MDS/mathdistops/blob/main/CONTRIBUTING.md)

## Code of Conduct

Welcome to our project! We appreciate your interest in contributing. Please follow our [code of conduct](https://github.com/UBC-MDS/mathdistops/blob/main/CONDUCT.md)

## License

`mathdistops` was created by Katherine Chen, Kun Ya, Oak Chong, Sandra Gross. It is licensed under the terms of the MIT license.

## Credits

`mathdistops` was created with a template tool [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
