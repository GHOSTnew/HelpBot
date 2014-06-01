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

def format_text(text):
    text = text.replace('[~BOLD~]', '\002')
    text = text.replace('[~RED~]', '\0034')
    text = text.replace('[~WHITE~]', '\0030')
    text = text.replace('[~BLACK~]', '\0031')
    text = text.replace('[~BLUE~]', '\0032')
    text = text.replace('[~GREEN~]', '\0033')
    text = text.replace('[~DARKRED~]', '\0035')
    text = text.replace('[~PURPLE~]', '\0036')
    text = text.replace('[~BROWN~]', '\0037')
    text = text.replace('[~YELLOW~]', '\0038')

    text = text.replace('[~PINK~]', '\00313')
    if text.__contains__('[~CLEAR~]'):
       if text.split('[~CLEAR~]')[0].__contains__('\002'):
          text = text.replace('[~CLEAR~]', '\003\002')
       else:
          text = text.replace('[~CLEAR~]', '\003')
    return text
