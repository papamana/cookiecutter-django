import warnings

from pathlib import Path

import pytest

template_root = Path(__file__).parents[1].as_posix()


@pytest.fixture(scope="module")
def bake_result(cookies_session):
    """Reusable project fixture."""
    # Set the module scope because creating a new project takes a while.
    session = cookies_session.bake(
        extra_context={"project_name": "Test Project"}, template=template_root
    )
    return session
 