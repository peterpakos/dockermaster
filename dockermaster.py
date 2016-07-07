#!/usr/bin/env python
#
# Script for managing Docker containers
#
# Author: Peter Pakos <peter.pakos@wandisco.com>

from __future__ import print_function

from argparse import ArgumentParser
from os import path
from sys import stderr, argv

from docker import Client, errors
from prettytable import PrettyTable
from requests import exceptions


class Main(object):
    __version = '16.6.22'
    __name = path.basename(argv[0])
    __docker_host = 'unix://var/run/docker.sock'
    __cli = None

    def __init__(self):
        action = self.parse_args()

        try:
            self.__cli = Client(base_url=self.__docker_host)
        except errors.DockerException as err:
            self.die(err.message)

        if action == 'list':
            self.display_list()

    def __del__(self):
        if self.__cli:
            self.__cli.close()

    @staticmethod
    def die(message=None, code=1):
        if message is not None:
            print(message, file=stderr)
        exit(code)

    def parse_args(self):
        parser = ArgumentParser()
        parser.add_argument('-v', '--version',
                            help='show version', action="store_true")
        parser.add_argument('action', help='dupa', choices=['list'])
        parser.add_argument('-H', '--host', help='Socket or URL to bind to (default: unix:///var/run/docker.sock)')
        args = parser.parse_args()
        if args.version:
            self.display_version()
            exit()
        if args.host:
            self.__docker_host = args.host
        return args.action

    def display_version(self):
        print('%s version %s' % (self.__name, self.__version))

    def display_list(self):
        containers = None
        try:
            containers = self.__cli.containers(all=True)
        except exceptions.ConnectionError:
            self.die('Problem connecting to Docker Host')

        print('Containers found: %s' % len(containers))
        if containers:
            table = PrettyTable(['Name', 'IP Address', 'Image', 'Status'])
            for container in containers:
                table.add_row([container['Names'][0].replace('/', ''),
                               container['NetworkSettings']['Networks']['bridge']['IPAddress'],
                               container['Image'], container['Status']])
            print(table)


if __name__ == '__main__':
    app = Main()
