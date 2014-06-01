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

import os
from lib.ircstyle import * 

def load(bot, cmd, nick, channel, args):
    if cmd == ".add":
        ajout(args)
        bot.send(channel, "Mot ajouté")
    elif cmd == ".def":
        bot.send(channel, definition(args))
    elif cmd == ".del":
        delete(args)
        bot.send(channel, "Mot suprimé")

def onhelp(bot, channel):
    bot.send(channel, ".add => ajoute une définition")
    bot.send(channel, ".def => affiche la définition d'un mot")
    bot.send(channel, ".del => supprime un mot du dictionnaire")

def definition(word):
  fichier = open("conf/dico.conf", "r")
  i = 0
  search_proba = None
  for ligne in fichier:
    ligne = ligne.split(">||<")
    if ligne[0].lower() == word.lower():
      return "\002" + ligne[0] + "\002: " + format_text(ligne[1])
    elif ligne[0].lower().__contains__(word.lower()) and i < 4:
      if i == 0:
         search_proba = ligne[0]
      else:
         search_proba += ", " + ligne[0]
      i += 1
  fichier.close()
  if search_proba:
    return "aucune définition pour \002" + word + "\002, peut etre recherchez vous : " + search_proba
  return "aucune définition pour \002" + word

def ajout(phrase):
  fichier = open("conf/dico.conf", "a")
  fichier.write(phrase + '\n')
  fichier.close()

def delete(word):
  contenu_fichier = ""
  fichier = open("conf/dico.conf", "r")
  for ligne in fichier:
      wordfichier = ligne.split(">||<")
      if wordfichier[0].lower() !=  word.lower():
          contenu_fichier += ligne + "\n"
  fichier.close
  os.system("rm conf/dico.conf && touch conf/dico.conf")
  fichier = open("conf/dico.conf", "a")
  fichier.write(contenu_fichier)
  fichier.close()
