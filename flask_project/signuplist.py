__author__ = 'masawant'
__author__ = 'masawant'

import boto.dynamodb

def add_user(username='',first_name='',last_name=''):
    #Open a connection to the Sign Up Table
    conn = boto.dynamodb.connect_to_region(
        'us-west-1',
        aws_access_key_id='',
        aws_secret_access_key='')
    signupListTable = conn.get_table('SignUpList')
    #Check if user already exists
    item = None
    try:
        item = signupListTable.get_item(
            hash_key = username
        )
    except:
        pass
    if item is None:
        item = signupListTable.new_item(
            hash_key = username
        )
        item['FirstName']=first_name
        item['LastName']=last_name
        item.put()
        return "UserAdded"
    else:
        return "AlreadyExists"