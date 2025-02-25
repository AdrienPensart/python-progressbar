import contextlib
import os
import time

import original_examples  # type: ignore
import progressbar
import pytest

# Import hack to allow for parallel Tox
try:
    import examples
except ImportError:
    import sys

    _project_dir = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(_project_dir)
    import examples

    sys.path.remove(_project_dir)


def test_examples(monkeypatch):
    for example in examples.examples:
        with contextlib.suppress(ValueError):
            example()


@pytest.mark.filterwarnings('ignore:.*maxval.*:DeprecationWarning')
@pytest.mark.parametrize('example', original_examples.examples)
def test_original_examples(example, monkeypatch):
    monkeypatch.setattr(progressbar.ProgressBar, '_MINIMUM_UPDATE_INTERVAL', 1)
    monkeypatch.setattr(time, 'sleep', lambda t: None)
    example()


@pytest.mark.parametrize('example', examples.examples)
def test_examples_nullbar(monkeypatch, example):
    # Patch progressbar to use null bar instead of regular progress bar
    monkeypatch.setattr(progressbar, 'ProgressBar', progressbar.NullBar)
    assert progressbar.ProgressBar._MINIMUM_UPDATE_INTERVAL < 0.0001
    example()


def test_reuse():
    bar = progressbar.ProgressBar()
    bar.start()
    for i in range(10):
        bar.update(i)
    bar.finish()

    bar.start(init=True)
    for i in range(10):
        bar.update(i)
    bar.finish()

    bar.start(init=False)
    for i in range(10):
        bar.update(i)
    bar.finish()


def test_dirty():
    bar = progressbar.ProgressBar()
    bar.start()
    assert bar.started()
    for i in range(10):
        bar.update(i)
    bar.finish(dirty=True)
    assert bar.finished()
    assert bar.started()
