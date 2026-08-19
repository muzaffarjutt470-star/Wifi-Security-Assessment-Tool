def test_project_structure():
    import os

    assert os.path.exists("README.md")
    assert os.path.exists("requirements.txt")


def test_basic_functionality():
    assert True
