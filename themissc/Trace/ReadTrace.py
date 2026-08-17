import os

import numpy as np

from ._Trace import TracePath


def ReadTrace(Date, sc="a", Model="TS05"):
    """Read a saved daily footprint file into a dictionary."""
    fname = TracePath(Date, sc=sc, Model=Model)
    if not os.path.isfile(fname):
        raise FileNotFoundError(fname)
    with np.load(fname, allow_pickle=False) as saved:
        return {key: saved[key] for key in saved.files}
