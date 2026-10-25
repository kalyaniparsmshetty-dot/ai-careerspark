import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from careerspark import analyzer as an, samples


def test_empty_and_short_input_rejected():
    assert an.validate_text("", "job description", 25)[0] is False
    ok, msg, _ = an.validate_text("too short", "job description", 25)
    assert not ok and "too short" in msg
    assert an.validate_text("1234 5678 !!!! " * 10, "job description", 25)[0] is False


def test_long_input_is_trimmed_with_notice():
    ok, msg, text = an.validate_text("python sql " * 5000, "job description", 25)
    assert ok and len(text) == an.MAX_CHARS and "first" in msg


def test_skill_detection_edge_cases():
    assert an.find_skills("We use Java and JavaScript") == ["Java", "JavaScript"]
    assert "SQL" in an.find_skills("Knowledge of SQL.") and "MySQL" not in an.find_skills("sql only")
    assert "C++" in an.find_skills("experience with C++, and C#")
    assert "Excel" not in an.find_skills("an excellent communicator")
    assert an.find_skills("hello world") == []


def test_job_analysis_depends_on_input():
    a = an.analyze_job(samples.SAMPLE_JD)
    b = an.analyze_job(samples.SAMPLE_HEALTH_JD)
    assert "SQL" in a["skills"] and "HIPAA" not in a["skills"]
    assert "HIPAA" in b["skills"] and "SQL" not in b["skills"]
    assert a["title"] == "Junior Data Analyst" and a["level"] == "entry-level"
    assert a["responsibilities"] and a["experience"]


def test_match_score_follows_formula():
    m = an.match_resume("I know Python and Excel well. " * 4, "Need Python, SQL, Excel and Tableau skills. " * 2)
    assert m["matched"] == ["Python", "Excel"] or set(m["matched"]) == {"Python", "Excel"}
    assert set(m["missing"]) == {"SQL", "Tableau"}
    assert m["score"] == round(100 * len(m["matched"]) / len(m["jd_skills"]), 1) == 50.0


def test_match_changes_with_resume():
    low = an.match_resume("I enjoy painting and cooking at weekends with friends and family.", samples.SAMPLE_JD)
    high = an.match_resume(samples.SAMPLE_RESUME, samples.SAMPLE_JD)
    assert low["score"] < high["score"]
    assert an.match_resume("x " * 30, "Python SQL")["score"] == 0.0


def test_no_jd_skills_gives_zero_and_empty():
    m = an.match_resume(samples.SAMPLE_RESUME, "We want a friendly person for our shop.")
    assert m["jd_skills"] == [] and m["score"] == 0.0


def test_questions_vary_by_input_and_title_only():
    t = an.generate_questions("Nurse", "")
    d = an.generate_questions("", samples.SAMPLE_JD)
    assert t["source"] == "job title" and any(q["skill"] == "Patient Care" for q in t["technical"])
    assert d["source"] == "job description" and any(q["skill"] == "SQL" for q in d["technical"])
    assert len(d["hr"]) == 8 and d["scenario"]
    assert an.generate_questions("zzz", "")["source"] == "none"
    assert all(q["difficulty"] in ("Beginner", "Intermediate", "Advanced") for q in d["technical"] + d["scenario"])


def test_improve_does_not_invent_facts():
    r = an.improve_text(samples.SAMPLE_IMPROVE, samples.SAMPLE_JD)
    assert "Managed the college library database project" in r["improved"]
    assert not any(ch.isdigit() for ch in r["improved"])
    assert "Python" not in r["improved"]            # keywords are suggested, never inserted
    assert "SQL" in r["keywords_to_consider"]
    assert r["suggestions"]


def test_reports_are_text():
    assert "Score:" in an.report_match(an.match_resume(samples.SAMPLE_RESUME, samples.SAMPLE_JD))
    assert "TECHNICAL" in an.report_questions(an.generate_questions("", samples.SAMPLE_JD))
    assert "Role:" in an.report_job(an.analyze_job(samples.SAMPLE_JD))
