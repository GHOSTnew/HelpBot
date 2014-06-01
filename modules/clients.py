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
    if cmd == ".client" and channel == "#help":
        args =  args.lower()
        if args == "windows":
            bot.send(channel, "\002mIRC\002: beaucoups d'utilisateurs de \002windaube\002 l\'utilisent bien qu'il n'est pas forcement bon (\002\0034payant: 20$\002\003)")
            bot.send(channel, "\002XChat (et dérivé)\002: un tres bon client IRC que nous vous recommendons, (un fork gratuit existe voir .def xchat windows)")
        elif args == "macos" or args == "mac":
            bot.send(channel, "\002Colloquy\002 (http://colloquy.info): Open source et gratuit, bon client pour les débutants et aussi les pour les utilisateurs avancés")
            bot.send(channel, "\002Textual\002 (http://www.codeux.com/textual/): C'est l'un des client IRC les plus moderne (\002\0034payant: 4$ , la version d'essai, vous déconnecte toutes les 2 heures\002\003)")
            bot.send(channel, "\002LimeChat\002 (http://limechat.net/): gratuit et ambitieux (support: MacOs, iOS & Windows), il est d'origine japonaise")
            bot.send(channel, "\002Snak\002 (http://www.snak.com/index.html): Snak remonte loin dans les années 1990 (\002\0034payant: 29$\002\003)")
        elif args == "unix" or args == "linux":
            bot.send(channel, "\002\0032~~~~~~~~~Terminal~~~~~~~~~\002\003")
            bot.send(channel, "\002irssi\002 (http://irssi.org/): un des meilleurs client irc en mode console (il tourne aussi sous windaube)")
            bot.send(channel, "\002\0032~~~~~~~~~~~~X11~~~~~~~~~~~\002\003")
            bot.send(channel, "\002XChat\002 (http://xchat.org/): C'est le client graphique le plus populaire")
            bot.send(channel, "\002Konversation\002 (http://konversation.kde.org/): C'est le client IRC par défaut livré avec KDE")
        else:
            bot.send(channel, "\002\0034Error usage: .client <Windows|MacOs|Unix/Linux>\002\003")

def onhelp(bot, channel):
    if channel == "#help":
        bot.send(channel, ".client <Windows|MacOs|Unix/Linux> => Petite liste et description de clients IRC")
