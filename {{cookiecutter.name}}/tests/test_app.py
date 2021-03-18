from chalice.test import Client

from app import app


def test_index():
    with Client(app) as testclient:
        actual = testclient.http.get("/").json_body
        expected = {"status": "ok"}
        assert actual == expected
