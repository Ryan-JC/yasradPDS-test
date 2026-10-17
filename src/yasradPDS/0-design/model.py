"""
model.py
The data classes that make up a design, grouped the way a user
thinks about it: canopy parameters, line lengths, mass, and deployment settings.

A Design holds a main canopy, and optionally, a drogue.

These classes only hold data. They do not calculate anything, read or write files (storage.py), or convert units (units.py).

ex:
class dataClassName:
    parameter1: type
    parameter2: type
    ...
"""