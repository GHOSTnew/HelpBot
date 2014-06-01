# -*- coding: utf-8 -*-
import re, urllib, gzip, StringIO
import web

#Author: Sean B. Palmer & GHOSTnew
#Modified by GHOSTnew

ubuntu_uri = 'http://doc.ubuntu-fr.org/%s'

r_tr = re.compile(r'(?ims)<tr[^>]*>.*?</tr>')
r_paragraph = re.compile(r'(?ims)<p[^>]*>.*?</p>|<li(?!n)[^>]*>.*?</li>')
r_tag = re.compile(r'<(?!!)[^>]+>')
r_whitespace = re.compile(r'[\t\r\n ]+')
r_redirect = re.compile(
   r'(?ims)class=.redirectText.>\s*<a\s*href=./([^"/]+)'
)

abbrs = ['etc', 'ca', 'cf', 'Co', 'Ltd', 'Inc', 'Mt', 'Mr', 'Mrs',
         'Dr', 'Ms', 'Rev', 'Fr', 'St', 'Sgt', 'pron', 'approx', 'lit',
         'syn', 'transl', 'sess', 'fl', 'Op', 'Dec', 'Brig', 'Gen'] \
   + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') \
   + list('abcdefghijklmnopqrstuvwxyz')
t_sentence = r'^.{5,}?(?<!\b%s)(?:\.(?=[\[ ][A-Z0-9]|\Z)|\Z)'
r_sentence = re.compile(t_sentence % r')(?<!\b'.join(abbrs))

def load(bot, cmd, nick, channel, args):
    if cmd == ".ubuntu-fr":
      bot.send(channel, doc_fr(args))
def onhelp(bot, channel):
    bot.send(channel, ".ubuntu-fr => recherche dans la doc d'ubuntu")

def unescape(s):
   s = s.replace('&gt;', '>')
   s = s.replace('&lt;', '<')
   s = s.replace('&amp;', '&')
   s = s.replace('&#160;', ' ')
   s = s.replace('&#039;', '\'')
   return s

def text(html):
   html = r_tag.sub('', html)
   html = r_whitespace.sub(' ', html)
   return unescape(html).strip()

def search(term):
   try: import search
   except ImportError, e:
      print e
      return term

   if isinstance(term, unicode):
      term = term.encode('utf-8')
   else: term = term.decode('utf-8')

   term = term.replace('_', ' ')
   try: uri = search.google_search('site:doc.ubuntu-fr.org %s' % term)
   except IndexError: return term
   if uri:
      return uri[len('http://doc.ubuntu-fr.org/'):]
   else: return term

def ubuntu_fr(term, last=False):
   global ubuntu_uri
   if not '%' in term:
      if isinstance(term, unicode):
         t = term.encode('utf-8')
      else: t = term
      q = urllib.quote(t)
      u = ubuntu_uri % (q)
      bytes = web.get(u)
   else: bytes = web.get(ubuntu_uri % (term))

   if bytes.startswith('\x1f\x8b\x08\x00\x00\x00\x00\x00'):
      f = StringIO.StringIO(bytes)
      f.seek(0)
      gzip_file = gzip.GzipFile(fileobj=f)
      bytes = gzip_file.read()
      gzip_file.close()
      f.close()

   bytes = r_tr.sub('', bytes)

   if not last:
      r = r_redirect.search(bytes[:4096])
      if r:
         term = urllib.unquote(r.group(1))
         return ubuntu_fr(term,  last=True)

   paragraphs = r_paragraph.findall(bytes)

   if not paragraphs:
      if not last:
         term = search(term)
         return ubuntu_fr(term, last=True)
      return None

   # Pre-process
   paragraphs = [para for para in paragraphs
                 if (para and 'technical limitations' not in para
                          and 'window.showTocToggle' not in para
                          and 'Deletion_policy' not in para
                          and 'Template:AfD_footer' not in para
                          and not (para.startswith('<p><i>') and
                                   para.endswith('</i></p>'))
                          and not 'disambiguation)"' in para)
                          and not '(images and media)' in para
                          and not 'This article contains a' in para
                          and not 'id="coordinates"' in para
                          and not 'class="thumb' in para]
                          # and not 'style="display:none"' in para]

   for i, para in enumerate(paragraphs):
      para = para.replace('<sup>', '|')
      para = para.replace('</sup>', '|')
      paragraphs[i] = text(para).strip()

   # Post-process
   paragraphs = [para for para in paragraphs if
                 (para and not (para.endswith(':') and len(para) < 150))]

   para = text(paragraphs[0])
   m = r_sentence.match(para)

   if not m:
      if not last:
         term = search(term)
         return ubuntu_fr(term, last=True)
      return None
   sentence = m.group(0)

   maxlength = 275
   if len(sentence) > maxlength:
      sentence = sentence[:maxlength]
      words = sentence[:-5].split(' ')
      words.pop()
      sentence = ' '.join(words) + ' [...]'

   if (('Vous avez suivi un lien vers une page qui n\'existe pas encore.' in sentence)
    or ('Créer cette page' in sentence)):
      if not last:
         term = search(term)
         return ubuntu_fr(term, last=True)
      return None

   sentence = '"' + sentence.replace('"', "'") + '"'
   sentence = sentence.decode('utf-8').encode('utf-8')
   ubuntu_uri = ubuntu_uri.decode('utf-8').encode('utf-8')
   term = term.decode('utf-8').encode('utf-8')
   return sentence + ' - ' + (ubuntu_uri % (term))

def doc_fr(origterm):
  #origterm = origterm.encode('utf-8')
  term = urllib.unquote(origterm)
  if term.startswith(':') and (' ' in term):
    a, b = term.split(' ', 1)
    a = a.lstrip(':')
    if a.isalpha():
        language, term = a, b
  term = term[0].upper() + term[1:]
  term = term.replace(' ', '_')
  print term
  try: result = ubuntu_fr(term)
  except IOError:
    return 'Can\'t connect to doc.ubuntu-fr.org (' + term +')'

  if result is not None:
    print result
    return result
  else: return'Can\'t find anything in doc.ubuntu-fr for ' + origterm +'.'
