"""Regression tests for cross-platform product path templates."""

import ntpath

import pytest

import themissc


GROUPS = ["EFI", "ESA", "FFT", "FGM", "Fields", "GMOM", "MOM", "Oth", "Pos", "SCM", "SST"]


@pytest.mark.parametrize("group", GROUPS)
def test_product_path_templates_are_windows_safe(group):
    config = getattr(getattr(themissc, group), f"_{group}")

    # On Windows, ntpath interprets the colon in a typed format field such as
    # ``{:s}`` as a drive separator and corrupts the template during join().
    assert "{:" not in config.idxfname
    assert "{:" not in config.datapath
    assert config.idxfname.format("PROD", "2", "a").endswith("PROD.2.a.dat")

    windows_template = ntpath.join("C:\\data", group, "{}", "{}", "{}")
    assert windows_template.format("PROD", "2", "a") == ntpath.join(
        "C:\\data", group, "PROD", "2", "a"
    )
