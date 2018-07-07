import textparser
import requests
import concurrent.futures
import queue

class Client:
  def __init__(self, integers_queue, chars_queue):
    self.integers_queue = integers_queue
    self.chars_queue = chars_queue

  def retrieve_and_queue_content_from_urls(self, urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 16) as executor:
      # Very naive - first pass, taken from https://docs.python.org/3/library/concurrent.futures.html
      future_to_url = {executor.submit(self.retrieve_and_queue_content, url): url for url in urls}
      for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        data = future.result()

  def retrieve_and_queue_content(self, url):
    content = self.retrieve_content_from_url(url)
    chars = textparser.chars_from_text(content)
    integers = textparser.integers_from_text(content)
    self.queue_chars(chars)
    self.queue_integers(integers)

  def retrieve_content_from_url(self, url):
    response = requests.get(url, allow_redirects = False)
    return response.text

  def queue_chars(self, content):
    for char in content:
      self.chars_queue.put(char)
  
  def queue_integers(self, content):
    for integer in content:
      self.integers_queue.put(integer)
