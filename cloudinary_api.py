import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os
load_dotenv()


class Image:
    def __init__(self):
        self.cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME')
        self.api_key=os.getenv('CLOUDINARY_API_KEY')
        self.api_secret=os.getenv('CLOUDINARY_API_SECRET')

        cloudinary.config(
            cloud_name=self.cloud_name,
            api_key=self.api_key,
            api_secret=self.api_secret,
            secure=True,
        )


    def upload(self, file, name):
        """
        Upload an image to cloudinary
        :param file: Upload file location
        :param name: string name
        """

        upload_result = cloudinary.uploader.upload(file=file, public_id=name, overwrite=True)
        optimize_url, _ = cloudinary_url(source=name, fetch_format="auto", quality="auto")
        auto_crop_url, _ = cloudinary_url(source=name, width=500, height=500, crop="auto", gravity="auto")

        return auto_crop_url



