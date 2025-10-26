from b2sdk.v2 import InMemoryAccountInfo
from b2sdk.v2 import B2Api
import os
import pathlib

BRANCH_NAME = pathlib.Path(os.environ["BRANCH_NAME"]).name
PDF_NAME = f'{BRANCH_NAME}-manual_en.pdf'

print(PDF_NAME)

APP_KEY = os.environ["BACKBLAZE_APP_KEY"]
APP_KEY_ID = os.environ["BACKBLAZE_APP_KEY_ID"]

info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", APP_KEY_ID, APP_KEY)

buck = b2_api.get_bucket_by_name("cataloguing-manual")
buck.upload_local_file(pathlib.Path.cwd() / 'src' / 'render' / 'manual_en.pdf', PDF_NAME)
link = buck.get_download_url(PDF_NAME)

# insert link into README.

print(link)

with open(pathlib.Path.cwd() / 'src' / 'template.md') as readme:
  readme.write(pathlib.Path.cwd() / 'README.md')



