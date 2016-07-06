#!/usr/bin/env python
#
# Python template
#
# Author: Peter Pakos
# Copyright (C) 2015

import sys
import getopt
import os
from docker import Client


# Main class
class Main(object):
    app_version = "1.0"
    app_name = os.path.basename(sys.argv[0])

    def __init__(self):
        self.test = self.parse_options()

    # Parse arguments
    def parse_options(self):
        try:
            options, args = getopt.getopt(sys.argv[1:], "hv", [
                "help",
                "version"
            ])
        except getopt.GetoptError as err:
            self.error("Error: %s" % err)
            self.usage()
            self.die(1)

        for opt, arg in options:
            if opt in ("-h", "--help"):
                self.usage()
                self.die()
            if opt in ("-v", "--version"):
                self.version()
                self.die()

    # Display version
    def version(self):
        print "%s version %s" % (self.app_name, self.app_version)

    # Display help page
    def usage(self):
        self.version()
        print "Usage: %s [OPTIONS]" % self.app_name
        print "AVAILABLE OPTIONS:"
        print "-h\t\tPrint this help summary page"
        print "-v\t\tPrint version number"

    def error(self, message=None):
        if message is not None:
            print >> sys.stderr, message

    # App code to be run
    def run(self):
        c = Client(base_url='unix:///var/run/docker.sock')
        try:
            c.containers()
        except:
            e = sys.exc_info()[1]
            print >> sys.stderr, "Error: %s" % str(e)
            sys.exit(1)

    # Exit app with code and optional message
    def die(self, code=0, message=None):
        if message is not None:
            print message
        sys.exit(code)


# Instantiate main class and run it
if __name__ == '__main__':
    app = Main()
    app.run()
