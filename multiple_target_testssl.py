import os
import time

# path can be changed
checker = '/home/../ext-tools/testssl.sh/testssl.sh'
try:
        # path can be changed
        fp = open("ip_ssl_check_1.txt","r")
        for line in fp:
                check = os.system(checker + 'https://' + line)
                time.sleep(7)
finally:
        fp.close()
