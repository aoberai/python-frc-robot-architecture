# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class SensorTimeBase(__pybind11_builtins.pybind11_object):
    """
    Velocity Measurement Periods
    
    Members:
    
      Per100Ms_Legacy : Legacy Mode
    
      PerSecond : Per-Second Velocities
    
      PerMinute : Per-Minute Velocities
    """

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.SensorTimeBase, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.SensorTimeBase) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.SensorTimeBase, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Per100Ms_Legacy = SensorTimeBase.Per100Ms_Legacy
    PerMinute = SensorTimeBase.PerMinute
    PerSecond = SensorTimeBase.PerSecond
    __entries = {
        'Per100Ms_Legacy': (
            SensorTimeBase.Per100Ms_Legacy,
            'Legacy Mode',
        ),
        'PerMinute': (
            SensorTimeBase.PerMinute,
            'Per-Minute Velocities',
        ),
        'PerSecond': (
            SensorTimeBase.PerSecond,
            'Per-Second Velocities',
        ),
    }
    __members__ = {
        'Per100Ms_Legacy': SensorTimeBase.Per100Ms_Legacy,
        'PerMinute': SensorTimeBase.PerMinute,
        'PerSecond': SensorTimeBase.PerSecond,
    }
