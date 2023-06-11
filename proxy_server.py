import os
import socket

FORMATS = [
    "naive",
    "avro",
    "json",
    "pbuffer",
    "mpack",
    "yaml",
    "xml"
]

def handle_request(request):
    print(request)
    parts = request.decode().split()
    if len(parts) != 2 or parts[0] != 'get_result':
        return 'Error: Invalid request'
    formats = [parts[1]]
    print(parts)
    if 'all' in parts[1]:
        formats = FORMATS
    ans = b''
    for format_name in formats:
        format_name = format_name.upper()
        server_port = int(os.environ.get(f'{format_name}_PORT'))
        server_name = os.environ.get(f'{format_name}_NAME')
        print(f"Sending request for {format_name} serializer to {server_name}:{server_port}")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.sendto(b"calculate", (server_name, server_port))
        response, _ = server_socket.recvfrom(1024)
        ans += response
    return ans


def serve():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 2000))

    while True:
        request, address = server_socket.recvfrom(1024)
        response = handle_request(request)
        server_socket.sendto(response, address)


if __name__ == '__main__':
    serve()