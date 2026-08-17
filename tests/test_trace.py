"""Tests for daily magnetic field footprint generation."""

import importlib
from types import SimpleNamespace

import numpy as np

from themissc import Globals
from themissc.Trace._Trace import EARTH_RADIUS_KM, FOOTPRINT_FIELDS


def test_trace_all_gsm_positions_and_save_footprints(tmp_path, monkeypatch):
    module = importlib.import_module("themissc.Trace.TraceField")
    monkeypatch.setattr(Globals, "DataPath", str(tmp_path))

    position = np.array(
        [[EARTH_RADIUS_KM, 0.0, 0.0], [0.0, 2.0 * EARTH_RADIUS_KM, 0.0]]
    )
    times = np.array([1490659200.0, 1490662800.0])
    monkeypatch.setattr(
        module,
        "ReadCDF",
        lambda Date, sc: (
            {"tha_pos_gsm": position, "tha_state_time": times},
            {},
        ),
    )

    parameter_file = tmp_path / "parameters.bin"
    parameter_file.touch()
    calls = {}

    class FakeTrace:
        def __init__(self, x, y, z, Date, ut, **kwargs):
            calls.update(x=x, y=y, z=z, Date=Date, ut=ut, kwargs=kwargs)
            self.nstep = np.array([10, 20])
            for i, field in enumerate(FOOTPRINT_FIELDS):
                setattr(self, field, np.array([i, i + 0.5]))

    fake_gp = SimpleNamespace(
        Globals=SimpleNamespace(DataFile=str(parameter_file)),
        TraceField=FakeTrace,
    )
    monkeypatch.setattr(module, "ConfigurePyGeopack", lambda: fake_gp)

    result = module.TraceField(20170328, sc="a", Verbose=False)

    np.testing.assert_allclose(calls["x"], [1.0, 0.0])
    np.testing.assert_allclose(calls["y"], [0.0, 2.0])
    np.testing.assert_allclose(calls["z"], [0.0, 0.0])
    np.testing.assert_array_equal(calls["Date"], [20170328, 20170328])
    np.testing.assert_allclose(calls["ut"], [0.0, 1.0])
    assert calls["kwargs"]["Model"] == "TS05"
    assert calls["kwargs"]["CoordIn"] == "GSM"
    assert result["position_gsm_re"].shape == (2, 3)
    assert result["GlatN"].shape == (2,)

    saved = importlib.import_module("themissc.Trace.ReadTrace").ReadTrace(20170328)
    np.testing.assert_allclose(saved["position_gsm_re"], result["position_gsm_re"])
    np.testing.assert_allclose(saved["GlatN"], result["GlatN"])
