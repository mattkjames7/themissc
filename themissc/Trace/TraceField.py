import os

import numpy as np

from ..Pos.ReadCDF import ReadCDF
from ._Trace import ConfigurePyGeopack, EARTH_RADIUS_KM, FOOTPRINT_FIELDS, TracePath


def TraceField(
    Date,
    sc="a",
    Model="TS05",
    Overwrite=False,
    Verbose=True,
    alt=100.0,
    MaxLen=1000,
    DSMax=1.0,
    **kwargs,
):
    """Trace every GSM spacecraft position and save its daily footprints.

    Position CDF coordinates are converted from km to Earth radii before
    tracing. The returned dictionary is also saved as one compressed NPZ file
    per date, spacecraft and model.
    """
    Date = int(Date)
    sc = sc.lower()
    Model = Model.upper()
    fname = TracePath(Date, sc=sc, Model=Model)

    if os.path.isfile(fname) and not Overwrite:
        from .ReadTrace import ReadTrace

        return ReadTrace(Date, sc=sc, Model=Model)

    data, _ = ReadCDF(Date, sc=sc)
    if data is None:
        raise FileNotFoundError(f"No position data available for THEMIS {sc} on {Date}")

    prefix = f"th{sc}"
    position_key = f"{prefix}_pos_gsm"
    time_key = f"{prefix}_state_time"
    if position_key not in data or time_key not in data:
        raise KeyError(f"Position CDF does not contain {position_key} and {time_key}")

    position_km = np.asarray(data[position_key], dtype="float64")
    unix_time = np.asarray(data[time_key], dtype="float64")
    if position_km.ndim != 2 or position_km.shape[1] != 3:
        raise ValueError(f"{position_key} must have shape (n, 3)")
    if unix_time.shape != (position_km.shape[0],):
        raise ValueError("Position and time arrays have different lengths")
    if not np.all(np.isfinite(position_km)) or not np.all(np.isfinite(unix_time)):
        raise ValueError("Every trace requires a finite GSM position and time")

    position_re = position_km / EARTH_RADIUS_KM
    ut = np.mod(unix_time, 86400.0) / 3600.0
    dates = np.full(unix_time.size, Date, dtype="int32")

    gp = ConfigurePyGeopack()
    if not os.path.isfile(gp.Globals.DataFile):
        raise FileNotFoundError(
            "PyGeopack model parameters are missing; run "
            "themissc.Trace.UpdateParameters() first"
        )

    trace = gp.TraceField(
        position_re[:, 0],
        position_re[:, 1],
        position_re[:, 2],
        dates,
        ut,
        Model=Model,
        CoordIn="GSM",
        alt=alt,
        MaxLen=MaxLen,
        DSMax=DSMax,
        Verbose=Verbose,
        TraceDir="both",
        **kwargs,
    )

    output = {
        "Date": dates,
        "ut": ut,
        "unix_time": unix_time,
        "position_gsm_km": position_km,
        "position_gsm_re": position_re,
        "nstep": np.asarray(trace.nstep),
        "spacecraft": np.array(sc),
        "model": np.array(Model),
        "earth_radius_km": np.array(EARTH_RADIUS_KM),
        "alt_km": np.array(alt),
        "max_length": np.array(MaxLen),
        "max_step_re": np.array(DSMax),
    }
    for field in FOOTPRINT_FIELDS:
        output[field] = np.asarray(getattr(trace, field))

    os.makedirs(os.path.dirname(fname), exist_ok=True)
    tmpfname = fname + ".tmp"
    try:
        with open(tmpfname, "wb") as f:
            np.savez_compressed(f, **output)
        os.replace(tmpfname, fname)
    finally:
        if os.path.isfile(tmpfname):
            os.remove(tmpfname)

    if Verbose:
        print(f"Saved {unix_time.size} {Model} footprints to {fname}")
    return output
