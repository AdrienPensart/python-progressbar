from datetime import date

from .__about__ import __author__, __version__
from .bar import DataTransferBar, NullBar, ProgressBar
from .base import UnknownLength
from .multi import MultiBar, SortKey
from .shortcuts import progressbar
from .terminal.stream import LineOffsetStreamWrapper
from .utils import len_color, streams
from .widgets import (
    ETA,
    AbsoluteETA,
    AdaptiveETA,
    AdaptiveTransferSpeed,
    AnimatedMarker,
    Bar,
    BouncingBar,
    Counter,
    CurrentTime,
    DataSize,
    DynamicMessage,
    FileTransferSpeed,
    FormatCustomText,
    FormatLabel,
    FormatLabelBar,
    GranularBar,
    MultiProgressBar,
    MultiRangeBar,
    Percentage,
    PercentageLabelBar,
    ReverseBar,
    RotatingMarker,
    SimpleProgress,
    Timer,
    Variable,
    VariableMixin,
)

__date__ = str(date.today())
__all__ = [
    'progressbar',
    'len_color',
    'streams',
    'Timer',
    'ETA',
    'AdaptiveETA',
    'AbsoluteETA',
    'DataSize',
    'FileTransferSpeed',
    'AdaptiveTransferSpeed',
    'AnimatedMarker',
    'Counter',
    'Percentage',
    'FormatLabel',
    'SimpleProgress',
    'Bar',
    'ReverseBar',
    'BouncingBar',
    'UnknownLength',
    'ProgressBar',
    'DataTransferBar',
    'RotatingMarker',
    'VariableMixin',
    'MultiRangeBar',
    'MultiProgressBar',
    'GranularBar',
    'FormatLabelBar',
    'PercentageLabelBar',
    'Variable',
    'DynamicMessage',
    'FormatCustomText',
    'CurrentTime',
    'NullBar',
    '__author__',
    '__version__',
    'LineOffsetStreamWrapper',
    'MultiBar',
    'SortKey',
]
