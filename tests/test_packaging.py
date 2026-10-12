from importlib.metadata import distribution
from pathlib import Path

import pyoes


def test_package_has_no_scaffold_resources():
    package = Path(pyoes.__file__).parent
    assert not (package / "scaffolds").exists()


def test_package_registers_only_the_demo_app_factory():
    entry_points = distribution("pyoes").entry_points
    assert {(entry.group, entry.name, entry.value) for entry in entry_points} == {
        ("paste.app_factory", "main", "pyoes:main"),
    }
