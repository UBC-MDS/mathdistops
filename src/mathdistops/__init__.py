# read version from installed package
from importlib.metadata import version
__version__ = version("mathdistops")

from mathdistops.pnorm import pnorm
from mathdistops.qnorm import qnorm
from mathdistops.qexp import qexp
from mathdistops.pexp import pexp
