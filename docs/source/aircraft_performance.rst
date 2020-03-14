Aircraft performance
====================

In this lines, we will try to introduce you in the aircraft design and performance
world, not only by explaining some realtionships but also showing how to solve
them by making use of **skaero**.

Equations for flight peformance
-------------------------------

We can identify at least three kind of forces which cause the different
accelerations on aircraft's flight: aerodynamic, propulsive and gravity ones.
Though different reference systems may apply when solving for the general
flgiht equations (which is not the objective of this package), it is interesting
to express these equations from the point of view of wind axis:

.. math::

    m\frac{\text{d}V}{\text{d}t} = \sum{F_{x}}=T\cos(\alpha + \epsilon_{T}) - D - W\sin{\gamma}

    mV\frac{\text{d}\gamma}{\text{d}t} = \sum{F_{y}}= T \sin(\alpha + \epsilon_{T}) + L - W \cos(\gamma)

Where in previous equations:

* m: the actual mass of the aircraft
* W: weight of the aircraft, the mass times local gravity value
* T: thrust
* L: aerodynamic lift
* D: aerodynamic drag
* V: aircraft speed
* :math:`\alpha`: angle of attack
* :math:`\gamma`: climb angle
* :math:`\epsilon_{T}`: incidence of thrust axis with respect to body axes

Previous equations might be simplified taking into account that the angle of
attack does no take great values during flight conditions and therefore together
with the incidence of thrust angle, therefore cosines and sines functions might
be linearized:

.. math::

    m\frac{\text{d}V}{\text{d}t} = \sum{F_{x}}=T - D - W\sin{\gamma}

    mV\frac{\text{d}\gamma}{\text{d}t} = \sum{F_{y}}= L - W \cos(\gamma)


We can solve for the aerodynamic forces in the previous equations if we know
some aircraft geometrical and aerodynamic parameters such us the wing surface or
lift-drag realtionship:

.. code-block:: python

   # Make use of the performance module for solvinf lift and drag
   from skaero.performance import lift, drag

   # Assume unitary values in units [Pa], [m2] and [none]
   Q, S, Cl = 1.00, 1.00, 1.00

   # They could by passing dynamic pressure, surface and respective coefficient
   L = lift(Q, S, Cl)
   D = drag(Q, S, Cd)

A relationship between both aerodynamic forces and therefore, between both
the lift and drag coefficient must be defined for solving at least one as
function of the other. This relationship is called the "polar drag", which might
be expressed as :math:`C_{d} = C_{d0} + K C_{l} ^ {2}` and can be found again
in the performance moduke:

.. code-block:: python

   # Import the polar drag from skaero
   from skaero.performance import drag_factor, polar_drag

   # Known aircraft parameters
   Cl, e0, AR, K = 0.5, 0.95, 6.00, drag_factor(AR, e0) 

   # Drag factor as function of lift coefficient
   Cd = polar_drag(Cd0, K, Cl)

The relationship between lift and drag is known as "aerodynamic efficiency"
and it achieves its maximum when the drag is minimized and the lift maximized,
which happens at the following condition:

.. math::

    C_{Lopt} = \sqrt{\frac{C_{D0}}{K}}
    C_{D} = 2 * C_{D0}

Making the previous 


