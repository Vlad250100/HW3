from sklearn import tree

import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from conf.tuning import settings
print (settings.LINK)
