import os

from pyoes.cachebust import file_hash


def test_file_hash(tmp_path):
    f = tmp_path / "app.css"
    f.write_text("a")
    first = file_hash(str(f))
    assert len(first) == 10
    assert file_hash(str(f)) == first

    f.write_text("bb")
    assert file_hash(str(f)) != first


def test_file_hash_same_size_new_mtime(tmp_path):
    f = tmp_path / "app.css"
    f.write_text("a")
    os.utime(f, ns=(1, 1))
    first = file_hash(str(f))
    f.write_text("b")
    os.utime(f, ns=(2, 2))
    assert file_hash(str(f)) != first


def test_file_hash_missing(tmp_path):
    assert file_hash(str(tmp_path / "missing.css")) is None
    assert file_hash(str(tmp_path)) is None
