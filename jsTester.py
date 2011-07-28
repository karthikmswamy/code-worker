#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Karthik Muthuswamy

import os, sys, encryptData, subprocess, webbrowser
import threading, time
from github2.client import Github
from encryptData import encryptDESAndWriteData

repoFolder = ''

class threadingJInst(threading.Thread):
	def run(self):
		global repoFolder
		print 'Starting Java Instance'
		# Run the jar file on port 9876 and open the web browser
		os.system('java -jar ../' + repoFolder + '/gui/test/lib/jstestdriver/JsTestDriver.jar --port 9876')

def mainThread():
	global repoFolder
	if len(sys.argv) < 2:
		print 'Usage: python jsTester.py <decryptionkey> <repoURL>'
		sys.exit()
	if len(sys.argv) == 2:
		decKey = sys.argv[1]
		repoURL = 'git@github.com:SMU-SIS/TournamentServer-GUI.git'
	elif len(sys.argv) == 3:
		decKey = sys.argv[1]
		repoURL = sys.argv[2]

	appid,uname = encryptData.readDataAndDecryptDES('keys.txt', decKey)

	# GitHub configurations
	GITHUB_USER = uname
	GITHUB_TOKEN = appid

	# API Object
	github = Github(username=GITHUB_USER, api_token=GITHUB_TOKEN)
	# Get the folder name by splitting the GIT url
	sp = repoURL.partition('/')
	repoFolder = sp[2].replace('.git','')
	# Clone or update the GIT url
	#gitCloneUpdateRepo(repoURL, repoFolder)

	# Initiate a thread for executing the JsTestDriver while
	# the browser is initiated on the main thread	
	thread = threadingJInst()
	thread.start()
	print 'Waiting for the Java instance to warm-up'
	time.sleep(1)
	brwsr = subprocess.Popen('chromium-browser http://localhost:9876/capture',shell=True)
	print os.path.abspath('.')
	execCmd = 'sh ../' + repoFolder + '/gui/scripts/test.sh'
	# Capture log in a text file
	os.system(execCmd + '>log.txt')

	# Capturing output of the device on log.txt
	#fnull = open('log.txt', 'w')
	#result = subprocess.call(execCmd, shell = True, stdout = fnull, stderr = fnull)
	#fnull.close()
	time.sleep(4)
	os.system('killall -KILL chromium-browser')
	os.system('killall -KILL java')

def gitCloneUpdateRepo(repoFolder, folderName):
	# If the directory exists, update the folder with
	# the latest code from git
	# Else clone the repository
	if os.path.exists('../' + folderName):
		os.chdir('../' + folderName)
		print('Updating git repository to latest version: %s' % (folderName))
		os.system('git pull')
		os.chdir('..')
		print os.path.abspath('.')
	else:
		print('Cloning git repository: %s' % (folderName))
		os.system('git clone ' + repoFolder + ' ../' + folderName)

	os.chdir('..')

mainThread()
