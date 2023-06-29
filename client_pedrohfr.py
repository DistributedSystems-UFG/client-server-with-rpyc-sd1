import rpyc
from constRPYC import *

class Client:
  conn = rpyc.connect(SERVER, PORT)

  def append(self, data):
      return self.conn.root.exposed_append(data)

  def value(self):
      return self.conn.root.exposed_value()

  def search(self, data):
      return self.conn.root.exposed_search(data)

  def remove(self, data):
      return self.conn.root.exposed_remove(data)

  def insert(self, index, data):
      return self.conn.root.exposed_insert(index, data)

  def sort(self):
      return self.conn.root.exposed_sort()

client = Client()
client.append(5)
client.append(6)

print(client.value())
print(client.search(6))

client.remove(6)
print(client.value())

client.insert(0, 10)
print(client.value())

client.sort()
print(client.value())