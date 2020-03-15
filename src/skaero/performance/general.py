"""
General performance utilities
"""

import numpy as np


def aspect_ratio(b, S):
    """ Solves for the aspect ratio of the wing

    .. math::
        
        AR = \frac{b ^ {2}}{S}

    Parameters
    ----------
    b: float
        Wing span
    S: float
        Wingn surface

    Returns
    -------
    AR: float
        Aspect ratio value
    """

    AR = b ** 2 / S
    return AR

def drag_factor(AR, e0):
    r""" Also known as 'K', relates the ideal elliptic wing drag with the actual
    one by introducing the Oswald efficiency.

    .. math::

    K = \frac{1}{\pi AR e_{0}}

    Parameters
    ----------
    AR: float
        Aspect ratio of the wing
    e0: float
        Oswald efficiency

    Parameters
    ----------
    K: float
        Drag factor
    """

    K = 1 / (np.pi * AR * e0)
    return K
