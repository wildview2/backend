import pathlib
from typing import List
from fastapi import UploadFile


class DownloadFiles():
    async def __call__(self, upload_file: UploadFile) -> dict:

        async def download_file(upload_file: UploadFile) -> dict:
            folder_path = pathlib.Path(__file__).parent.resolve()
            upload_path = folder_path.joinpath(pathlib.Path("assets"))
            i = 1
            # поправить дикт на строку
            urls = []
            photo_path = upload_path.joinpath(pathlib.Path(f"{upload_file.filename}"))
            with open(photo_path, "wb+") as file_object:
                file_object.write(upload_file.file.read())
            urls[f"photo{i}"] = upload_file.filename
            i += 1
            return urls
        return await download_file(upload_file)


downloadfilesproduct = DownloadFiles()