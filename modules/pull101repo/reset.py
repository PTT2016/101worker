#! /usr/bin/env python

import os
import sys
import json
import shutil
import commands
sys.path.append('../../libraries/101meta')
import const101

def getRepoName(repoUrl):
	(head, tail) = os.path.split(repoUrl)
	return tail.replace('.git', '')

def removeContrib(dep):
	if os.path.exists(os.path.join(const101.sRoot, dep['targetdir' ], '.created_by_pull101repo')):
		print 'removing ' + dep['targetdir']
		shutil.rmtree(os.path.join(const101.sRoot, dep['targetdir' ]))

def removeSubdirs(dep):
	name = getRepoName(dep['sourcerepo'])
	depsPath = os.path.join(gitdepsFolder, name)
	dirList = os.listdir(depsPath)
	for fname in dirList:
		if not '.git' in fname or 'README' in fname:
			if os.path.exists(os.path.join(const101.sRoot, dep['targetdir' ], fname, '.created_by_pull101repo')):
				print 'removing ' + os.path.join(dep['targetdir'], fname)
				shutil.rmtree(os.path.join(const101.sRoot, dep['targetdir'], fname))		

#MAIN PROGRAM
basePath = os.path.dirname(const101.sRoot)
gitdepsFolder = os.path.join(basePath, "gitdebs")

if os.path.isfile('./gitdeps_local'):
	print 'loading gitdeps from last run'
	localGitDeps = json.loads(open('./gitdeps_local').read())
	for dep in localGitDeps:
		if not dep.get('mode') == 'subdirsonly':
			removeContrib(dep)
		else:
			removeSubdirs(dep)
else:
	print "Can't find local gitdeps - pull101repo wasn't completely executed yet"