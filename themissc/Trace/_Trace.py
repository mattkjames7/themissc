import os

from .. import Globals


EARTH_RADIUS_KM = 6371.2
FOOTPRINT_FIELDS = (
    "GlatN",
    "GlatS",
    "MlatN",
    "MlatS",
    "GlonN",
    "GlonS",
    "MlonN",
    "MlonS",
    "GltN",
    "GltS",
    "MltN",
    "MltS",
    "Lshell",
    "MltE",
    "FlLen",
)


def TracePath(Date, sc="a", Model="TS05"):
    """Return the output filename for one daily spacecraft trace."""
    return os.path.join(
        Globals.DataPath,
        "Trace",
        Model.upper(),
        sc.lower(),
        f"{int(Date):08d}.npz",
    )


def ConfigurePyGeopack():
    """Set portable default locations before importing PyGeopack."""
    parameter_root = os.path.join(Globals.DataPath, "Trace", "Parameters")
    os.environ.setdefault("GEOPACK_PATH", os.path.join(parameter_root, "geopack"))
    os.environ.setdefault("OMNIDATA_PATH", os.path.join(parameter_root, "omni"))
    os.environ.setdefault("KPDATA_PATH", os.path.join(parameter_root, "kp"))

    import PyGeopack

    return PyGeopack
