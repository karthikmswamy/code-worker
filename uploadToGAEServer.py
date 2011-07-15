#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Karthik Muthuswamy
# Uploads target folder to GAE server

import sys, pexpect, encryptData
from encryptData import encryptDESAndWriteData

if len(sys.argv) < 3:
	print 'Usage: python uploadToGAEServer.py <decryptionkey> <target>'
	sys.exit()
else:
	decKey = sys.argv[1]
	target = sys.argv[2]

email,pswd = encryptData.readDataAndDecryptDES('code-comparison.txt', decKey)
cmd = 'python /home/karthik/google_appengine/appcfg.py --email=' + email + ' update ' + target
print cmd
child = pexpect.spawn (cmd)

i = child.expect([pexpect.TIMEOUT, 'Password for codecomparison@gmail.com:', pexpect.EOF])

if i == 0:
	print 'No keys found, accepting ssh key permanently!'
	child.sendline ('yes')
	i = child.expect([pexpect.TIMEOUT, 'Password for codecomparison@gmail.com:', pexpect.EOF])
elif i == 1:
	print 'Password requested, sending password'
	child.sendline (pswd)
	print 'Password sent'
elif i ==2:
	print 'Keys available or it\'s a time out!'
	pass

print child.before
print 'Done'
