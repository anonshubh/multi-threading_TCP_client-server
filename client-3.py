"""
M2M Lab Exercise 4
- Client that sends the TCP requests 
(Random Values, P and Q in the range 100 to 499) to the Server
Built by - Shubh Pathak (MSM19B018)
"""
import socket,time,random,base64

PORT = 10001

SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

# Sends the request to Server
def send(data):
    print(f"Sending {data} to Server")
    message = base64.b64encode(data.encode("utf-8"))
    client.send(message)


if __name__ == '__main__':
    try:
        while True:
            P = random.randint(100,500)
            Q = random.randint(100,500)
            data = f"C3:(P,Q)=({P},{Q})"
            send(data)
            time.sleep(3)
    except:
        print("\nStopped Sending requests to Server...")
    finally:
        client.close()