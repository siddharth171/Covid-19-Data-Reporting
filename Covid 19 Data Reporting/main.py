# TRIGGERING THE SERVICE IN SEQUENCE

# main.py is only worried about trigerring not sequencing

from reports.reports import aggregate

def trigger_mail_service():
    '''
    Triggering the servises here
    '''
    # AGGREGATE
    aggregate()
    
trigger_mail_service()