#! /usr/bin/python
import sys, localconfig, platform, time
#OS Runtime comments
if platform.system() == "Windows":
        sys.path.append(localconfig.winpath)
        print "You are running the AnkitBot UAA Module for Windows. Sponsored by DQ. :)"
else:
        sys.path.append(localconfig.linuxpath)
        print "You are running the AnkitBot UAA Module for Linux. Sponsored by DQ. :)"
import wikipedia
import globalfunc as globe
override = False
if not globe.startAllowed(override):
        print "Fatal - System Access Denied."
        sys.exit(1)
        print "System Alert - Program is still running."
globe.main()
globe.checkWait()
globe.pageCleanup()
wikipedia.stopme()
