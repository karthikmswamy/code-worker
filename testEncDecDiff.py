#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Karthik Muthuswamy
# Test for encrpyt/decrypt

import encryptData, findDiff
from encryptData import encryptDESAndWriteData
from findDiff  import findDiffOfDirs

# Test inputs for GAppID and SPwd - success
print encryptDESAndWriteData('APIKey', 'UName', 'keys.txt', '')
appid,uname = encryptData.readDataAndDecryptDES('keys.txt', '')

print appid
print uname
# Test inputs for dir1 and dir2 - success
#print findDiff.findDiffOfDirs('code-worker','code-worker/code-worker','log')
