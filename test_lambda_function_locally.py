import os
os.environ['charset'] = "UTF-8"
# DON'T COMMIT EMAIL ADDRESSES
os.environ['source_email'] = ""
os.environ['destination_email'] = ""
os.environ['max_sent'] = "0"
os.environ['db_table'] = 'cheesy_lines'
os.environ['filter_key'] = "sent"
from lambda_function import *
#get_lines()
process()
