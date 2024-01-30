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

## Installation
This package uses [Poetry](https://python-poetry.org/) for dependency management and packaging. It is not yet available for installation via `pip`. To install and use this package, please follow these steps:

1. **Install Poetry and Conda**: If you don't have Poetry or Conda installed, install them by following the official installation guide for [Poetry](https://python-poetry.org/docs/#installation) and [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. **Clone the Repository**: Clone this repository to your local machine.

    ```bash
    git clone https://github.com/UBC-MDS/mathdistops.git
    cd mathdistops
    ```
3. **Install the virtual environment**:

   ```bash
    conda env create -f environment.yaml
    ```
4. **Activate the installed environment**:

   ```bash
    conda activate mathdistops
   ```

5. **Install the Package with Poetry**: Use Poetry to install the package and its dependencies.

    ```bash
    poetry install
    ```

## Usage

### Using this package

To use this package, you can import and call its functions in your Python scripts. Here's an example:

```python
# Run this on jupyter notebook to show the altair object
from mathdistops import pnorm

df, fig = pnorm(1, mean=0, std_dev=1)
print(df)
fig
```
Below is a sample usage on Jupyter Notebook. 

<img src="https://github.com/UBC-MDS/mathdistops/blob/main/img/usage_sample.jpg?raw=true" style="width: 750px;"/>

### Running unit tests

To run unit tests for this package, execute the following in the project root directory: 

```bash
    $ poetry run pytest
```

To get a the code coverage reporting, run this command:

```bash
    $ poetry run pytest --cov=mathdistops
    $ poetry run pytest --cov-branch --cov=mathdistops
```

## Functions
### Description
- pexp(q, rate=1, graph=True): Represents the Cumulative Distribution Function (CDF) of the exponential distribution characterized by a given parameter `rate`. The function calculates the cumulative probability for a given quantile `q` and plots the corresponding probability distribution (PDF) and the CDF. 

- qexp(p, rate=1, graph=True): Quantile Function of an exponential distribution, characterized by a given rate parameter `rate`. The function calculates the quantile corresponding to given cumulative probability `p` in an exponential distribution. Optionally, it can also generate and return a visualization of the PDF and the CDF.

- pnorm(q, mean = 0, std_dev =1, graph = True): Cumulative Distribution Function of the normal distribution with specified mean and standard deviation. It will return the cumulative probability up to the given value `q`. Optionally, it can generate and return a visualization of the distributions, the PDF and the CDF. 

- qnorm(p, mean=0, std_dev=1, graph=True): Calculates the quantile (Inverse Cumulative Distribution Function) corresponding to a specified cumulative probability `p` of the normal distribution with specified mean and standard deviation. The function can additionally create and provide a graphical representation of the PDF and the CDF.

### Documentation
A comprehensive guide and tutorial on utilizing these functions are available on ReadTheDocs. To access it, click the "docs" button located at the top of the README.

## Python Ecosystem Integration
While python has relevant functions for normal and exponential distribution in the scipy.stats package, this package offer an in-built additional functionality of returning the plot to help with visualization and understanding the problem. 

### Related Packages:
- [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) is an official scipy package to represent a normal continuous random variable.
- [scipy.stats.expon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html) is an official scipy package to represent an exponential continuous random variable.

## Dependencies

This package necessitates a Python version of 3 or higher. Additional required packages can be found in the [environment file](https://github.com/UBC-MDS/mathdistops/blob/main/environment.yaml) of this repository.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`mathdistops` was created by Katherine Chen, Kun Ya, Oak Chong, Sandra Gross. It is licensed under the terms of the MIT license.

## Credits

`mathdistops` was created with a template tool [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
