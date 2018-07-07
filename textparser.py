import re

def chars_from_text(text):
  chars_regex = re.compile(r'\D')
  return re.findall(chars_regex, text)

def integers_from_text(text):
  integers_regex = re.compile(r'\d')
  return re.findall(integers_regex, text)