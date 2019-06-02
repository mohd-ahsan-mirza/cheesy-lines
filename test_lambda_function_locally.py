import os
os.environ['source_email'] = ""
os.environ['destination_email'] = ""
# DON'T COMMIT EMAIL ADDRESSES
from lambda_function import *
send_email()