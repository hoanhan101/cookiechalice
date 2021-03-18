from chalice import Chalice, Response

from chalicelib.utils import get_status

app = Chalice(app_name="{{cookiecutter.name}}")


@app.route("/")
def index():
    return {"status": get_status()}
