import sys, base64

#/ Create enconding
def encode(text):
    encoded = base64.b64encode(text)
    return encoded

#/ Verify arguments
if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    print('Usage: %s <FileName> ' %sys.argv[0].split('\\')[len(sys.argv[0].split('\\'))-1])
    sys.exit(0)

#/ Try to open & encode the file
try:
    toencode = open(filename)
    content = toencode.read()
    encodedContent = encode(content)
    encoded = open(filename,'w')
    encoded.write('value="'+encodedContent+'"\nexec(value.decode("base64"))') #/ Write encoded value as a variable to file
    encoded.close()
    print('File sucessfully encoded!')
except IOError: #/ except for "open"
    print('The file "%s" dont exist!' %filename)