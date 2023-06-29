import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
      self.value.append(data)
      return self.value

  def exposed_value(self):
      return self.value

  def exposed_search(self, data):
      return [i for i, x in enumerate(self.value) if x == data]

  def exposed_remove(self, data):
      self.value = [x for x in self.value if x != data]
      return self.value

  def exposed_insert(self, index, data):
      self.value.insert(index, data)
      return self.value

  def exposed_sort(self):
      self.value.sort()
      return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()