from pathlib import Path
import pytest
import tempfile

import f3d


def test_compare_with_file():
    testing_dir = Path(__file__).parent.parent.parent / "testing"
    dataset = f"{testing_dir}/data/cow.vtp"
    reference = f"{testing_dir}/baselines/TestPythonCompareWithFile.png"
    output = tempfile.gettempdir() + "/TestPythonCompareWithFile.png"
    outputDiff = tempfile.gettempdir() + "/TestPythonCompareWithFile.diff.png"

    engine = f3d.Engine.create(True)
    engine.window.size = 300, 300

    # verify the size is properly set
    assert engine.window.width == 300
    assert engine.window.height == 300

    engine.scene.add(dataset)

    img = engine.window.render_to_image()
    img.save(output)

    error = 0.0

    assert img.compare(f3d.Image(reference), 0.05, error)
