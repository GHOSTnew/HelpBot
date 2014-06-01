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

import ConfigParser

def load(bot, cmd, nick, channel, args):
    phrase = (cmd + " " + args).lower().split(" ")
    cfg = ConfigParser.ConfigParser()
    cfg.read('conf/smskillers.conf')
    chans = cfg.get('smskillers', 'channels')
    if channel.split("#")[1]  in chans.split(" "):
       fichier = open("conf/sms_word.conf", "r")
       i = 0
       for ligne in fichier:
           ligne = ligne.replace('\n', '')
           v = 0
           while v<len(phrase):
              if ligne.lower() in phrase[v]:
                 i +=1
              v += 1
       if i > 0 and i <= 3:
          bot.send(channel, "\002\0034Le Language SMS n'est pas authorisé, sur ce réseau: va donc apprendre le français : https://duckduckgo.com/?q=cour+de+français ")
       elif i > 3:
          bot.kick(channel, nick, "\002\0034Le Language SMS n'est pas authorisé, sur ce réseau: va donc apprendre le français : https://duckduckgo.com/?q=cour+de+français")
       if i >= 10:
          bot.raw_line("MODE " + channel + " +b " + nick + '!*@*')
def onhelp(bot, channel):
    pass
