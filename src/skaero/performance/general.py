"""
General performance utilities
"""

def lift(Q, S, Cl):
    """ Lift force

    .. math::
        L = Q \cdot S \cot Cl

    Parameters
    ----------
    Q: float
        Dynamic pressure
    S: float
        Wing surface
    Cl: float
        Lift coefficient

    Returns
    -------
    L: float
        Lift force
    """
    L = Q * S * Cl
    return L

def drag(Q, S, Cd):
    """ Drag force

    .. math::
        D = Q \cdot S \cot Cd

    Parameters
    ----------
    Q: float
        Dynamic pressure
    S: float
        Wing surface
    Cd: float
        Drag coefficient

    Returns
    -------
    D: float
        Drag force
    """
    D = Q * S * Cd
    return D

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

def polar_drag(Cd0, K, Cl):
    """ Polar drag relationship

    .. math::

        C_{d} = C_{d0} + K C_{l} ^ {2}

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

    Cd = Cd0 * K * Cl ** 2
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

