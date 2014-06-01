#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################# Copyright ################################
#     Author: GHOSTnew            #              2014                  #
########################################################################
# This file is part of HelpBot.                                        #
# HelpBot is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# HelpBot is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.      #
########################################################################

import socket 
import socks
import time
import web
import re
import modules
import ssl

################################ Config #################################################
nick = "HelpBot"
real_name = "Help on our Network"
nickserv = "password nickserv" # for nickserv auth (set None for no ns auth)
channels = ["#opAmanda", "#help"] #channel
host = "server host"
port = 6697
Tor = False
password = None #server password (None by default)
SSL = True #SSL , false by default
import_modules =  ["noob", "opamanda", "ubuntu_fr", "wikipedia", "sms_killers", "clients"]
################################ End config ##############################################

class Bot(object):
    def __init__ (self, host, port, nick, real_name,Tor, nickserv=None, password=None, SSL=False):
        self.host = host
        self.port = port
        self.nick = nick
        self.real_name = real_name
        self.password = password
        self.nickserv = nickserv
        self.ssl = SSL
        if Tor == True:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
            socket.socket = socks.socksocket
        self.sock = socket.socket()

    def connect(self):
        self.sock.connect((self.host, self.port))
        if self.ssl == True:
            try:
                self.sock = ssl.wrap_socket(self.sock)
                self.sock.do_handshake()
            except:
                print "Failed to do ssl handshake" 
        time.sleep(5)
        self.raw_line('USER ' + self.nick + ' 0 ' + self.nick +' :' + self.real_name)
        if self.password:
            self.raw_line('PASS ' + self.password)
        self.raw_line('NICK ' + self.nick)
        self.raw_line('mode +B')
        time.sleep(2)
        if self.nickserv:
            self.send("NickServ", "IDENTIFY " + nickserv)
            time.sleep(2)
        for chan in channels:
            self.join(chan)
    
    def disconnect(self):
        self.sock.close()
        self.sock = socket.socket()

    def read(self):
        return self.sock.recv(1024)

    def send(self, channel, msg):
        self.sock.send('PRIVMSG ' + channel + ' :' + msg + '\r\n')

    def notice(self, channel, msg):
        self.sock.send('NOTICE ' + channel + ' :' + msg + '\r\n')

    def action(self, channel, msg):
        self.sock.send('PRIVMSG ' + channel + ' :' + '\001ACTION' + msg + '\001\r\n')

    def raw_line(self, line):
        self.sock.send(line + '\r\n')

    def join(self, channel):
        if channel.startswith('#'):
            self.sock.send('JOIN ' + channel + '\r\n')
        else:
            self.sock.send('JOIN #' + channel + '\r\n')

    def kick(self, channel, nick, reason = ""):
        self.sock.send('KICK ' + channel + ' ' + nick + ' :' + reason + '\r\n')
def main():
    HelpBot = Bot(host, port, nick, real_name, Tor, nickserv, password, SSL)
    HelpBot.connect()
    while True:
        data = HelpBot.read()
        if not data:
            print "connexion lost"
            HelpBot.disconnect()
            HelpBot.connect()
            #break
        #print data
        if data.find('PING') != -1:
            HelpBot.raw_line('PONG ' + data.split()[1] + '\r\n') 
        elif data.find('PRIVMSG') != -1: 
            cmd = (':'.join(data.split (':')[2:])).split( )[0]
            channel = ''.join (data.split(':')[:2]).split (' ')[-2]
            nick_source = (data.split (':')[1]).split('!')[0]
            arg = data.split(" ") 
            args = ''
            for index,item in enumerate(arg) :
                if index > 3 : 
                    if args == '': 
                        args = item 
                    else : 
                        args += ' ' + item
            args = args.split('\r')[0]
            if cmd == ".help":
                for module in import_modules:
                    mod = __import__ ("modules." + module, fromlist=import_modules)
                    mod.onhelp(HelpBot, channel)
            else:
                for module in import_modules:
                    mod = __import__ ("modules." + module, fromlist=import_modules)
                    mod.load(HelpBot, cmd, nick_source, channel, args)  
           
if __name__ == "__main__" :
    main()
