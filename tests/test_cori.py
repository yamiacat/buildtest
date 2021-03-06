import os
import pytest
from buildtest.menu.build import BuildTest


def test_cori():

    if os.getenv("NERSC_HOST") != "cori":
        pytest.skip("Test runs only on Cori")

    here = os.path.dirname(os.path.abspath(__file__))
    cori_configuration = os.path.join(here, "settings", "cori.config.yml")

    buildspec_files = os.path.join(here, "examples", "cori_buildspecs", "hostname.yml")
    cmd = BuildTest(config_file=cori_configuration, buildspecs=[buildspec_files])
    cmd.build()
