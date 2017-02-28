
HOST = 'imap.gmail.com'
user = 'igordsm@gmail.com'

import imapclient 
from backports import ssl
import getpass

if __name__ == '__main__':
    print('CmdMAIL')
    print('-------------------------')

    print('Connecting')
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    context.check_hostname = False
    server = imapclient.IMAPClient(HOST, use_uid=True, ssl=True, ssl_context=context)

    print('Signing in')
    server.login(user, getpass.getpass())
    print('Done!')

    print('Selecting folder')
    inbox = server.select_folder('INBOX')
    messages = server.search(['NOT', 'DELETED'])
    print('%d messages in INBOX'%len(messages))

