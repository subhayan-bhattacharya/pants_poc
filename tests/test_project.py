"""Test file to check that project metadata is available."""

import pants_poc


def test_author_not_empty() -> None:
    """Check that the author variable is accessible."""
    project_author = pants_poc.__author__
    assert project_author is not None and project_author != ""


def test_email_not_empty() -> None:
    """Check that the email variable is accessible."""
    project_email = pants_poc.__email__
    assert project_email is not None and project_email != ""
