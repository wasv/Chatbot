import wikipedia
import string
import re
from sys import argv

def lookup(request):
  try:
    response = wikipedia.summary(request, sentences=2)
    response = filter(lambda x: x in string.printable, response)
    #response = re.sub(r'\(.*?\)\s', '', response)
  except wikipedia.exceptions.DisambiguationError as e:
    response = lookup(e.options[0])
  return response

if argv[1] == "--shell":
  while True:
    request = raw_input("\nArticle: ")
    if request == "!end":
      break
    elif request == "":
      continue
    print lookup(request)
else:
  print lookup(' '.join(argv[1:]))