# socket 例子
import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 使用套接字接收发送数据
    udp_socket.sendto("hhhhhhaa", ("127.0.0.1", 8080))
    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
