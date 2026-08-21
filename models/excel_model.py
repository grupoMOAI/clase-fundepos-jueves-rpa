import os
import pandas as pd
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"xlsx", "xls"}


class ExcelModel:
    def __init__(self, upload_folder: str):
        self.upload_folder = upload_folder
        os.makedirs(self.upload_folder, exist_ok=True)

    @staticmethod
    def is_allowed(filename: str) -> bool:
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    def save(self, file_storage) -> str:
        filename = secure_filename(file_storage.filename)
        path = os.path.join(self.upload_folder, filename)
        file_storage.save(path)
        return path

    def preview(self, path: str, rows: int = 5) -> tuple[list[str], list[list]]:
        df = pd.read_excel(path).head(rows)
        headers = df.columns.astype(str).tolist()
        data = df.astype(object).where(df.notna(), "").values.tolist()
        return headers, data
