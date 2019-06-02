import os
os.environ['charset'] = "UTF-8"
# DON'T COMMIT EMAIL ADDRESSES
os.environ['source_email'] = ""
os.environ['destination_email'] = ""
os.environ['max_sent'] = "0" #Don't change this setting if you want to send a line only once
os.environ['db_table'] = 'cheesy_lines'
os.environ['filter_key'] = "sent"
from lambda_function import *
#print(get_lines())
process("","")
