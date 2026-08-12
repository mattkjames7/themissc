"""Network smoke tests for each implemented THEMIS data group."""

import os
import shutil
import subprocess
import sys
import textwrap

import pytest


DATE = 20210101

# One known-available Level 1 or Level 2 product per data group.
CASES = [
    pytest.param("EFI", "EFI", "2", id="EFI"),
    pytest.param("ESA", "ESA", "2", id="ESA"),
    pytest.param("FFT", "FFT", "2", id="FFT"),
    pytest.param("FGM", "FGM", "2", id="FGM"),
    pytest.param("Fields", "FIT", "2", id="Fields"),
    pytest.param("GMOM", "GMOM", "2", id="GMOM"),
    pytest.param("MOM", "MOM", "2", id="MOM"),
    pytest.param("Oth", "SCMODE", "1", id="Oth"),
    pytest.param("Pos", "V03", "1", id="Pos"),
    pytest.param("SCM", "SCM", "2", id="SCM"),
    pytest.param("SST", "SST", "2", id="SST"),
]


@pytest.mark.network
@pytest.mark.parametrize("group,product,level", CASES)
def test_download_and_read_one_day(tmp_path, group, product, level):
    """Download one known day into isolation and read its CDF variables."""
    script = textwrap.dedent(
        f"""
        import themissc

        interface = getattr(themissc, {group!r})
        kwargs = {{"sc": "a", "Prod": {product!r}, "L": {level!r}}}
        interface.DownloadData(
            Date={DATE}, Overwrite=False, Verbose=True, **kwargs
        )
        data, attributes = interface.ReadCDF({DATE}, **kwargs)

        assert isinstance(data, dict)
        assert data
        assert isinstance(attributes, dict)
        assert data.keys() == attributes.keys()
        """
    )
    env = os.environ.copy()
    env["THEMIS_PATH"] = str(tmp_path)
    env.setdefault("MPLCONFIGDIR", str(tmp_path / "matplotlib"))

    # Each CDF is read in a fresh interpreter. This keeps memory-heavy products
    # from accumulating native NumPy allocations over the parametrized suite.
    try:
        subprocess.run(
            [sys.executable, "-c", script],
            check=True,
            env=env,
            timeout=180,
        )
    finally:
        # pytest retains tmp_path directories until session teardown. Remove
        # each downloaded CDF now so later cases do not retain its file cache.
        shutil.rmtree(tmp_path, ignore_errors=True)
