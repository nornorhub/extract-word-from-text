#
# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt write a script
# which will use that text to build a message using the received word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\n)
#

import socket
import re

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 10000))
client.send(b"ma3loll")
wordCodes = client.recv(1024).decode().split('\n')[:-1]
x = []
with open("backdoor.txt", "r") as f:
	text = f.read()
	x = text.split('\n\n')
  
y = x
z = 0
for i in x:
  y[z] = i.splitlines()
  z += 1

z = y
j = 0
for i in y:
	k = 0
	for s in i:
		z[j][k] = s.split()
		k += 1
	j += 1

for i in range(len(wordCodes)):
	wordCodes[i] = wordCodes[i].split(', ')

words = []
  
for i in range(len(wordCodes)):
	words.append(z[int(wordCodes[i][0])-1][int(wordCodes[i][1])-1][int(wordCodes[i][2])-1])
res = re.sub(r'[^\w\s]', '', '\n'.join(words))
client.send(res.encode())
print(client.recv(1024))
