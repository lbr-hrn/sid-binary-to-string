import base64
import sys
import struct

def convert(binary):
    version = struct.unpack('B', binary[0:1])[0]
    # I do not know how to treat version != 1 (it does not exist yet)
    assert version == 1, version
    length = struct.unpack('B', binary[1:2])[0]
    authority = struct.unpack(b'>Q', b'\x00\x00' + binary[2:8])[0]
    string = 'S-%d-%d' % (version, authority)
    binary = binary[8:]
    assert len(binary) == 4 * length
    for i in range(length):
        value = struct.unpack('<L', binary[4*i:4*(i+1)])[0]
        string += '-%d' % value
    return string



def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # remove linhas de novo caracter.
            if line:
                try:
                    sid = base64.b64decode(line)
                    print(convert(sid))
                except Exception as e:
                    print(f"Falha em processar a linha: {line}")
                    print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Exemplo: python script.py <nomedoarquivo>")
        sys.exit(1)
    
    filename = sys.argv[1]
    process_file(filename)
