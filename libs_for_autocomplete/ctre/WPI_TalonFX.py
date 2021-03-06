from .TalonFX import TalonFX

from .WPI_BaseMotorController import WPI_BaseMotorController


class WPI_TalonFX(TalonFX, WPI_BaseMotorController):
    """ CTRE Talon SRX Motor Controller when used on CAN Bus. """

    def configSelectedFeedbackSensor(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        configSelectedFeedbackSensor(*args, **kwargs)
        Overloaded function.
        
        1. configSelectedFeedbackSensor(self: ctre._ctre.WPI_TalonFX, feedbackDevice: ctre._ctre.FeedbackDevice, pidIdx: int = 0, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        2. configSelectedFeedbackSensor(self: ctre._ctre.WPI_TalonFX, feedbackDevice: ctre._ctre.RemoteFeedbackDevice, pidIdx: int = 0, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        """
        pass

    def set(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        set(*args, **kwargs)
        Overloaded function.
        
        1. set(self: ctre._ctre.WPI_TalonFX, value: float) -> None
        
        2. set(self: ctre._ctre.WPI_TalonFX, mode: ctre._ctre.ControlMode, value: float) -> None
        
        3. set(self: ctre._ctre.WPI_TalonFX, mode: ctre._ctre.ControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        
        4. set(self: ctre._ctre.WPI_TalonFX, mode: ctre._ctre.TalonFXControlMode, value: float) -> None
        
        5. set(self: ctre._ctre.WPI_TalonFX, mode: ctre._ctre.TalonFXControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        """
        pass

    def setInverted(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        setInverted(*args, **kwargs)
        Overloaded function.
        
        1. setInverted(self: ctre._ctre.WPI_TalonFX, invertType: ctre._ctre.TalonFXInvertType) -> None
        
        2. setInverted(self: ctre._ctre.WPI_TalonFX, invertType: ctre._ctre.InvertType) -> None
        
        3. setInverted(self: ctre._ctre.WPI_TalonFX, bInvert: bool) -> None
        """
        pass

    def setVoltage(self, output):  # real signature unknown; restored from __doc__
        """ setVoltage(self: ctre._ctre.WPI_TalonFX, output: volts) -> None """
        pass

    def __init__(self, deviceNumber):  # real signature unknown; restored from __doc__
        """
        __init__(self: ctre._ctre.WPI_TalonFX, deviceNumber: int) -> None
        
        Constructor for a WPI_TalonFX
        
        :param deviceNumber: Device ID of TalonFX
        """
        pass
