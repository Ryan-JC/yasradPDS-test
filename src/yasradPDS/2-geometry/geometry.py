"""
geometry.py
The shared building blocks for canopy shapes: small neutral primitives (Point, Arc, Polyline) and the BaseCanopy interface that every specific canopy shape implements (gore count, drag coefficient, etc).

Defines the interface only. Each canopy shape's own math lives in its own file (for example semi_ellipsoid.py).

eg.
class Point:
    x: float
    y: float

class BaseCanopy:
    gore_num: int
    c_d: int
    ...
"""