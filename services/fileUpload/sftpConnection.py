import os

import pysftp
from autodotenv import load_dotenv


load_dotenv()

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def sendFileThroughSFTP(dataDirectory):
    with pysftp.Connection(os.getenv("sftpServer"), username=os.getenv("sftpUsername"), password=os.getenv("sftpPassword"),
                           cnopts= cnopts) as sftp:
        print(sftp.put(dataDirectory))
        sftp.close()
        return "OK"


def closeSftpConnection(sftp):
    sftp.close()