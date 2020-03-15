"""
General performance utilities
"""

import numpy as np

def Cl_opt(Cd0, K):
    """ Solves for optimal lift coefficient

    .. math::

        C_{Lopt} = \sqrt{\frac{C_{D0}}{K}}

    Parameters
    ----------
    Cd0: float
        Induced drag coefficient
    e0: float
        Oswald efficiency

    Returns
    -------
    Cl_opt: float
        Optimum lift coefficient
    """

    Cl_opt = np.sqrt(Cd0 / K)
    return Cl_opt

def V_opt(mass, rho, S, Cl_opt):
    r""" Solves for the minimum thrust condition speed

    .. math::

        V_{opt} = \sqrt{\frac{2mg}{\rho SC_{Lopt}}}

    Parameters
    ----------
    mass: float
        Mass of the aicraft
    rho: float
        Density at given altitude
    S: float
        Surface of the wing
    Cl_opt: float
        Optimum lift coefficient

    Returns
    -------
    V_opt: float
        Optitmum flight speed
    """

    V_opt = np.sqrt( (2 * mass * c.g0) / (rho * S * Cl_opt) )
    return V_opt

def polar_drag(Cd0, K, Cl):
    """ Polar drag relationship

    .. math::

        C_{D} = C_{D0} + K C_{L} ^ {2}

    Parameters
    ----------
    Cd0: float
        Induced drag coefficient
    K: float
        Drag factor
    Cl: float
        Lift coefficient

    Returns
    -------
    Cd: float
        Polar drag coefficient
    """

    Cd = Cd0 + K * Cl ** 2
    return Cd

def aero_efficiency(Cl, Cd):
    r""" Solves for aerodynamic efficiency

    .. math::
        
        E = \frac{C_{L}}{C{D}}

    Parameters
    ----------
    Cl: float
        Lift coefficient
    Cd: float
        Drag coefficient

    Returns
    -------
    E: float
        Aerodynamic efficiency
    """

    E = Cl / Cd
    return E

