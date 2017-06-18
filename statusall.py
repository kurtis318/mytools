#!/usr/bin/python
import os
from subprocess import Popen, PIPE

def statusrepo(path):
    """ Execut git status with a specific repo directory path """

    print("  >>>BEGIN<<< statusrepo:%s" % (path))
    os.chdir(path)
    cmd="git status"
    p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print "Return code: ", p.returncode
    print out.rstrip(), err.rstrip()
    print("  >>>END<<< statusrepo:%s" % (path))

# Main-line code starts here

basedir="/home/kurtis/dev/ibm-git"
repos=["collect_ambari_info","collect_linux_info","iperf1a","lbsbdtools","lbshpctools","mytools","XIKEY"]
for repo in repos:
    path=basedir+"/"+repo
    print("#" * 80)
    print(">>> %s\n" % (path))
    statusrepo(path)
