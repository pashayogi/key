import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  jangan memperjual belikan tools ini')
print(b+'\t    MR.K7C8NG')
print('\t GITHUB=https://github.com/pashayogi')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] tools sedang berjalan..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nhubungi MR.K7C8NG JIKA ADA MASALAH\nThanks TO :MR.K7C8NG\n\n')


# semoga bermanfaat
# BY=MR.K7C8NG
