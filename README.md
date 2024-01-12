# mathdistops

This package provides statistical functions for normal and exponential distributions, including pnorm, qnorm, pexp, and qexp. Each function not only performs the respective statistical calculation but also  generate a corresponding plot, offering both numerical results and visual outputs.

![Python](https://img.shields.io/badge/lanaguge-Python-red.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/MathDistOps)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/MathDistOps?include_prereleases)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/MathDistOps)
[![MIT License](https://img.shields.io/badge/License-MIT-informational?style=flat-square)](LICENSE-MIT)

## Installation

```bash
$ pip install mathdistops
```

## Functions
- pexp(x, rate, plot_graph=False): Calculate the exponential distribution cumulative probability for a given value and plots the corresponding distribution. This function computes the cumulative probability at a specified quantile `x` for an exponential distribution with a given rate parameter `lambda`. Optionally, it can generate and return a visualization of the distribution.

- pnorm(x, mean=0, std_dev=1, plot_graph=True): Cumulative Distribution Function (CDF) of the normal distribution with specified mean and standard deviation. It will return the cumulative probability up to the given value `x`. Optionally, it can generate and return a visualization of the distribution.

- qexp(p, rate, plot_graph=False): Calculates the quantile corresponding to given cumulative probability in an exponential distribution and plots the corresponding distribution. This function computes the quantile corresponding to a specified cumulative probability `p`. for an exponential distribution characterized by a given rate parameter `lambda`. Optionally, it can also generate and return a visualization of the distribution.

- qnorm(p, mean=0, std_dev=1, plot_graph=True): Calculates the quantile (Inverse Cumulative Distribution Function) of the normal distribution.This function computes the quantile corresponding to a specified cumulative probability `p`. for an exponential distribution characterized by a given rate parameter `lambda`. Optionally, it can also generate and return a visualization of the distribution.

## Python Ecosystem Integration
While python has relevant functions for normal and exponential distribution in the scipy.stats package, this package offer an in-built additional functionality of returning the plot to help with visualization and understanding the problem. 

### Related Packages:
- [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) is an official scipy package to represent a normal continuous random variable.
- [scipy.stats.expon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html) is an official scipy package to represent an exponential continuous random variable.

## Usage
- Usage instructions to be updated in the near future. 

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`mathdistops` was created by Ziwei Chen, Kun Ya, Sivakorn Oak Chong, Sandra Gross. It is licensed under the terms of the MIT license.

## Credits

`mathdistops` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
