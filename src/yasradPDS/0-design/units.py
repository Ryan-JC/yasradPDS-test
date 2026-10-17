"""
units.py

The only place units are converted: user units (ft, mm, oz/yd^2) to SI and back.

Everything outside this file works in SI. No frontend (CLI or GUI) and no other module should do its own unit conversion.
"""