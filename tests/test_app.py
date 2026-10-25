import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from streamlit.testing.v1 import AppTest

APP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")


def new():
    return AppTest.from_file(APP, default_timeout=30).run()


def click(at, key):
    next(b for b in at.button if b.key == key).click()
    return at.run()


def test_welcome_opens_and_get_started_works():
    at = new()
    assert not at.exception
    at = click(at, "get_started")
    assert at.session_state["page"] == "dashboard" and not at.exception


def test_all_pages_open_via_sidebar():
    at = new()
    for key in ("dashboard", "analyzer", "matcher", "interview", "improve", "about", "welcome"):
        at.session_state["page"] = key
        at.run()
        assert not at.exception, key


def test_analyzer_empty_error_then_success():
    at = new(); at.session_state["page"] = "analyzer"; at.run()
    at = click(at, "run_job")
    assert any("paste" in e.value.lower() for e in at.error)
    at = click(at, "sample_job"); at = click(at, "run_job")
    assert not at.error and at.session_state["res_job"]["title"] == "Junior Data Analyst"


def test_matcher_flow_and_clear():
    at = new(); at.session_state["page"] = "matcher"; at.run()
    at = click(at, "run_match"); assert len(at.error) == 2
    at = click(at, "sample_match"); at = click(at, "run_match")
    assert at.session_state["res_match"]["score"] == 43.8
    at = click(at, "clear_match")
    assert "res_match" not in at.session_state and at.session_state["jd_text"] == ""


def test_interview_and_improve_flow():
    at = new(); at.session_state["page"] = "interview"; at.run()
    at = click(at, "run_q"); assert at.error
    at.text_input(key="role_title").set_value("Data Analyst"); at = click(at, "run_q")
    assert at.session_state["res_q"]["technical"] and not at.exception
    at.session_state["page"] = "improve"; at.run()
    at = click(at, "run_imp"); assert at.error
    at = click(at, "sample_imp"); at = click(at, "run_imp")
    assert "Managed" in at.session_state["res_imp"]["improved"] and not at.exception


def test_shared_job_description_persists_across_pages():
    at = new(); at.session_state["page"] = "analyzer"; at.run()
    at = click(at, "sample_job")
    at.session_state["page"] = "interview"; at.run()
    assert "Junior Data Analyst" in at.session_state["jd_text"]
