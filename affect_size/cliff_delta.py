from typing import Iterable, Tuple, Union

from numpy import sqrt, isnan, nan
from scipy.stats import norm


def cliff_delta(
    s1: Iterable,
    s2: Iterable,
    alpha: int = 0.05,
    accurate_ci: bool = False,
    raise_nan: bool = True,
) -> Tuple[float, Tuple[float, float]]:
    """Calculate Cliff's Delta between two samples. 

    The current implementation is not very efficient. For a better version,
    see https://github.com/neilernst/cliffsDelta.

    Parameters
    ----------
    s1 : Iterable
        first sample
    s2 : Iterable
        second sample
    alpha : int, optional
        significance level, by default 0.05
    accurate_ci : bool, optional
        if True, the confidence interval is calculated using the more accurate formula
    raise_nan : bool, optional
        if True, an error is raised if NaN is found in the samples. If False, NaN is ignored.

    Returns
    -------
    Tuple[float, Tuple[float, float]]
        the method returns the delta value and its confidence interval.

    Notes
    -----

    Assuming the first sample:
    .. math:: s1 = {x_1, \cdots, x_n}
    and the second sample:
    .. math:: s2 = {y_1, \cdots, y_m}
    One can define:
    .. math:: \delta(x_i, y_j) = \cases{
        \text{if } x_i = y_j, 1,
        \text{if } x_i \neq y_j, 0,
        \text{if } x_i \notin \{y_1, \cdots, y_m\}, -1}
    """
    # TODO: implement w/ numpy
    m: int = len(s1)
    n: int = len(s2)
    delta_val: float = sum((delta(i, j) for i in s1 for j in s2)) / (m * n)

    if alpha > 1:
        raise ValueError("alpha must be between 0 and 1. Received: {}".format(alpha))

    delta_std: float = sqrt(
        (
            (
                m ** 2
                * sum(
                    (
                        (1 / n * sum((delta(i, j) for j in s2)) - delta_val) ** 2
                        for i in s1
                    )
                )
            )
            + (
                n ** 2
                * sum(
                    (
                        (1 / m * sum((delta(i, j) for i in s1)) - delta_val) ** 2
                        for j in s2
                    )
                )
            )
            - sum(((delta(i, j) - delta_val) ** 2 for i in s1 for j in s2))
        )
        / (n * m * (n - 1) * (m - 1))
    )
    z_crit: float = norm.ppf(1 - alpha / 2)
    if not accurate_ci:
        ci_size: float = delta_std * z_crit
        return delta_val, (delta_val - ci_size, delta_val + ci_size)
    else:
        ci_size: float = z_crit * delta_std * sqrt(
            1 - 2 * delta_val ** 2 + delta_val ** 4 + (z_crit * delta_std) ** 2
        )
        denom_corretion: float = 1 - delta_val ** 2 + (z_crit * delta_std) ** 2
        return (
            delta_val,
            (
                (delta_val - delta_val ** 3 - ci_size) / denom_corretion,
                (delta_val - delta_val ** 3 + ci_size) / denom_corretion,
            ),
        )


def delta(
    x: Union[float, int], y: Union[float, int], raise_nan: bool = True
) -> Union[int, float]:
    """Calculate delta between two values, i.e. return 1 if the 
    first is larger, -1 if the second is larger and 0 if the two are equal.

    Parameters
    ----------
    x : Union[float, int]
        first value
    y : Union[float, int]
        second value
    raise_nan : bool, optional
        if True, an error is raised if NaN is found in the samples. If False, NaN is ignored.

    Returns
    -------
    int or float
        delta between x and y

    Raises
    ------
    ValueError
        if x and y are neither larger, smaller or equal, something has gone
        amiss. If raise_nan is True, an error is raised even if the samples are NaN.
    """
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0
    else:
        if isnan(x) or isnan(y):
            if raise_nan:
                raise ValueError("NaN found in samples")
            else:
                return nan
        else:
            raise ValueError(
            "x and y are neither larger, nor smaller, nor equal, nor nan. Values received: x = {}, y = {}".format(
                x, y
            )
        )

