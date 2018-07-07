import sys
import queue
import client

class Handler:
  integers_queue = queue.Queue()
  chars_queue = queue.Queue()
  client_instance = client.Client(integers_queue, chars_queue)

  def handle(self, request):
    request_data = request.get_data(as_text = True)
    urls = self.get_urls_from_request(request_data)
    self.client_instance.retrieve_and_queue_content_from_urls(urls)
    integer = self.integers_queue.get()
    return

  def get_urls_from_request(self, data):
    return data.split(',')