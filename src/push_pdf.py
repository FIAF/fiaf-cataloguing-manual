from b2sdk.v2 import InMemoryAccountInfo
from b2sdk.v2 import B2Api
import os
import pathlib

APP_KEY = os.environ["BACKBLAZE_APP_KEY"]
APP_KEY_ID = os.environ["BACKBLAZE_APP_KEY_ID"]

info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", APP_KEY_ID, APP_KEY)

buck = b2_api.get_bucket_by_name("cataloguing-manual")
r = buck.upload_local_file(pathlib.Path.cwd() / 'src' / 'render' / 'manual_en.pdf', 'test.pdf')

print(r)
