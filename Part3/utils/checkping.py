import os

def check_ping(hostname):
    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
        return True
    else:
        pingstatus = "Network Error"
        return False
    return pingstatus