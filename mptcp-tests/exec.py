#!/usr/bin/python

import sys
import os

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    if (argc != 2):
        print 'Usage: $ python %s filename TEST [PATH_MANGER]' % argvs[0]
        quit()

    testlist = ["route","tcpdump","iperf","qperf"]

    if (argvs[1] == "all"):
        print "Start: %s test\n" % argvs[1]
        for i in range(len(testlist)):
            os.system("python ./tests/"+testlist[i]+".py")
    elif argvs[1] in testlist:
        print "Start: %s test\n" % argvs[1]
        os.system("python ./tests/"+argvs[1]+".py")
    else:
        print "\nERROR: %s No such test. Check your test" % argvs[1]
    print "\nEnd: %s test" % argvs[1]
