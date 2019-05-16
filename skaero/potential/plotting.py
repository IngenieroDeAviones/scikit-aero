"""
This script enables to plot different singularities passing a list that
contains them.
"""

from matplotlib import pyplot
import numpy
import singularities


def plot(sing_list, label=None):
    """Plots a singularity.
    """

    singPlot = SingularityPlot()  # Create a SingularityPlot object
    return singPlot.plot(sing_list, label=label)  # Return the graph


class SingularityPlot(object):
    """Creates a SingularityPlot object
    """

    def __init__(self, ax=None, N=200):
        """Constructor.

        Parameters
        ----------

        ax :
            Axes in which to plot
        N :
            Number of points to compute potential
        """

        self.ax = ax
        if not self.ax:
            self.fig, self.ax = pyplot.subplots(figsize=(6, 6))

        self.N = N

    def sing_list(self):
        return self._singularities

    def getVelocity(self, sing_list, X, Y):

        u, v = 0, 0  # Initial velocities

        for singularity in sing_list:
            u_sing, v_sing = singularity.velocity(X, Y)
            u += u_sing
            v += v_sing

        return u, v

    def get_limits(self, sing_list):

        x_min, x_max, y_min, y_max = 0, 0, 0, 0

        for singularity in sing_list:
            if not isinstance(singularity, singularities.UniformStream):
                x = singularity.x
                y = singularity.y

                if x <= x_min:
                    x_min = x

                if y <= y_min:
                    y_min = y

                if x >= x_max:
                    x_max = x

                if y_max <= y_max:
                    y_max = y

        x_min -= 5.0
        x_max += 5.0
        y_min -= 5.0
        y_max += 5.0

        return x_min, x_max, y_min, y_max

    def plot(self, sing_list, label=None):
        """
        Plots a singularity
        """

        N = self.N  # Number of points in each direction
        x_start, x_end, y_start, y_end = self.get_limits(
            sing_list
        )  # x-direction boundaries

        x = numpy.linspace(x_start, x_end, N)  # 1D-array for x
        y = numpy.linspace(y_start, y_end, N)  # 1D-array for y
        X, Y = numpy.meshgrid(x, y)  # generates a mesh grid

        u, v = self.getVelocity(sing_list, X, Y)

        self.ax.set_title("Velocity StreamPlot")
        self.ax.set_xlabel("x", fontsize=16)
        self.ax.set_ylabel("y", fontsize=16)
        self.ax.set_xlim(x_start, x_end)
        self.ax.set_ylim(y_start, y_end)
        self.ax.streamplot(
            X, Y, u, v, density=2, linewidth=1, arrowsize=1, color="k", arrowstyle="->"
        )

        for singularity in sing_list:
            if not isinstance(singularity, singularities.UniformStream):
                self.ax.scatter(
                    singularity.x, singularity.y, color="#CD2305", s=80, marker="o"
                )
