# tcp服务器
import socket
def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 连接
    tcp_server.bind(8999)

    tcp_server.listen(128)

    # 绑定
    tcp_server.accept()




if __name__ == '__main__':
    main()