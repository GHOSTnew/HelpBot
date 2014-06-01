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

def load(bot, cmd, nick, channel, args):
    if channel.lower() == "#opamanda":
        if cmd == ".tuto":
            arg = args.split(" ")
            if len(arg) == 1:
                tuto(bot, arg[0].lower())
            elif len(arg) >= 2:
                tuto(bot, arg[0].lower(), arg[1].lower())
            else:
                error(bot, cmd)
        elif cmd == ".lien":
             bot.send(channel, "\0036Blog officiel:\003 http://projetamanda.wordpress.com")
             bot.send(channel, "\0036English website:\003 http://helpother.net84.net")
             bot.send(channel, "\0036vimeo:\003 https://vimeo.com/projetamanda")
             bot.send(channel, "\0036Dailymotion:\003 http://www.dailymotion.com/opamanda")
             bot.send(channel, "\0036Twitter:\003 https://twitter.com/Projet_Amanda")
             bot.send(channel, "\0036Facebook:\003 https://www.facebook.com/pages/Projet-Amanda/437463849641730?ref=stream")
             bot.send(channel, "\0036pad:\003 https://etherpad.mozilla.org/2FZndMp71t")

def onhelp(bot, channel):
    if channel.lower() == "#opamanda":
        bot.send(channel, ".tuto => liste des tutoriels")
        bot.send(channel, ".lien => affiche tout les lien lié au projet")

def tuto(bot, os, lang="fr"):
    if os == "windows":
        if lang == "fr":
            bot.send("#opAmanda", "[HexChat] Se connecter à IRC http://projetamanda.wordpress.com/2013/10/19/windows-se-connecter-a-irc/")
            bot.send("#opAmanda", "[MetroIRC] Se connecter à IRC http://www.youtube.com/watch?v=qBUW8OlLNbk")
        elif lang == "en":
            bot.send("#opAmanda", "[mIRC] Connect to IRC http://helpother.net84.net/mIRC.html")
            bot.send("#opAmanda", "[MetroIRC] Connect to IRC (\0034 only subtiles are in english\003) http://www.youtube.com/watch?v=qBUW8OlLNbk")
        else:
            bot.send("#opAmanda", "\0034ERROR: 404 language not found\003")
    elif os == "linux":
        if lang == "fr":
            bot.send("#opAmanda", "[xChat] Se connecter à IRC http://projetamanda.wordpress.com/2013/10/22/gnulinux-se-connecter-a-irc/")
        elif lang == "en":
            bot.send("#opAmanda", "[WeeChat] Connect to IRC http://helpother.net84.net/Weechat.html")
        else:
            bot.send("#opAmanda", "\0034ERROR: 404 language not found\003")
    elif os == "android":
        if lang == "fr":
            bot.send("#opAmanda", "[yaaic] Se connecter à IRC http://projetamanda.wordpress.com/2013/10/19/android-se-connecter-a-irc/")
        else:
            bot.send("#opAmanda", "\0034ERROR: 404 language not found\003")
    elif os == "bsd":
        if lang == "en":
            bot.send("#opAmanda", "[Irssi] Connect to IRC http://helpother.net84.net/Irssi.html")
        else:
            bot.send("#opAmanda", "\0034ERROR: 404 language not found\003")
    elif os == "ios":
        if lang == "fr":
            bot.send("#opAmanda", "[Mango] Se connecter à IRC http://projetamanda.wordpress.com/2013/12/04/ios-se-connecter-a-irc/")
        else:
            bot.send("#opAmanda", "\0034ERROR: 404 language not found\003")
    else:
        error(bot, ".tuto")

def error(bot, cmd):
    if cmd == ".tuto":
        bot.send("#opAmanda", "\0034\002Error usage:\002 .tuto <windows|linux|BSD|android|ios> (lang)\003")
