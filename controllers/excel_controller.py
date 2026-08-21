from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from models.excel_model import ExcelModel

excel_bp = Blueprint("excel", __name__)


@excel_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@excel_bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No se envió ningún archivo.")
        return redirect(url_for("excel.index"))

    file = request.files["file"]
    if file.filename == "":
        flash("Debe seleccionar un archivo.")
        return redirect(url_for("excel.index"))

    if not ExcelModel.is_allowed(file.filename):
        flash("Formato inválido. Solo se aceptan .xlsx o .xls.")
        return redirect(url_for("excel.index"))

    model = ExcelModel(current_app.config["UPLOAD_FOLDER"])
    path = model.save(file)
    headers, rows = model.preview(path, rows=5)

    return render_template(
        "preview.html",
        filename=file.filename,
        headers=headers,
        rows=rows,
    )
