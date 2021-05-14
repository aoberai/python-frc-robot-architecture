class DemandType():
    """
    How to interpret a demand value.
    
    Members:
    
      Neutral : Ignore the demand value and apply neutral/no-change.
    
      AuxPID : When closed-looping, set the target of the aux PID loop to the demand value.
    
    When following, follow the processed output of the combined
    primary/aux PID output of the master.  The demand value is ignored.
    Although it is much cleaner to use the 2-param Follow() in such cases.
    
      ArbitraryFeedForward : When closed-looping, add demand arbitrarily to the closed-loop output.
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
        """ __init__(self: ctre._ctre.DemandType, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.DemandType) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.DemandType, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    ArbitraryFeedForward = DemandType.ArbitraryFeedForward
    AuxPID = DemandType.AuxPID
    Neutral = DemandType.Neutral
    __entries = {
        'ArbitraryFeedForward': (
            DemandType.ArbitraryFeedForward,
            'When closed-looping, add demand arbitrarily to the closed-loop output.',
        ),
        'AuxPID': (
            DemandType.AuxPID,
            'When closed-looping, set the target of the aux PID loop to the demand value.\n\nWhen following, follow the processed output of the combined\nprimary/aux PID output of the master.  The demand value is ignored.\nAlthough it is much cleaner to use the 2-param Follow() in such cases.',
        ),
        'Neutral': (
            DemandType.Neutral,
            'Ignore the demand value and apply neutral/no-change.',
        ),
    }
    __members__ = {
        'ArbitraryFeedForward': DemandType.ArbitraryFeedForward,
        'AuxPID': DemandType.AuxPID,
        'Neutral': DemandType.Neutral,
    }
