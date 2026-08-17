from ._Trace import ConfigurePyGeopack


def UpdateParameters(SkipWParameters=True):
    """Download and build the model parameters required by PyGeopack."""
    gp = ConfigurePyGeopack()
    return gp.Params.UpdateParameters(SkipWParameters=SkipWParameters)
