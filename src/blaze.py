from b2sdk.v2 import InMemoryAccountInfo
from b2sdk.v2 import B2Api
import os
import pathlib

BRANCH_NAME = pathlib.Path(os.environ["BRANCH_NAME"]).name
PDF_NAME = f'{BRANCH_NAME}-manual.pdf'

print('PDF_NAME', PDF_NAME)

APP_KEY = os.environ["BACKBLAZE_APP_KEY"]
APP_KEY_ID = os.environ["BACKBLAZE_APP_KEY_ID"]

info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", APP_KEY_ID, APP_KEY)

buck = b2_api.get_bucket_by_name("cataloguing-manual")
manual_path = pathlib.Path.cwd() / 'src' / 'manual.pdf'
if not manual_path.exists():
    raise Exception('Manual render not found.')

buck.upload_local_file(manual_path, PDF_NAME)
link = buck.get_download_url(PDF_NAME)
print('LINK', link)
