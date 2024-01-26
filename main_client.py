from src.App.app_client import ClientApp
from src.Conn.client_conn import ClientConn

if __name__ == '__main__':
    ClientApp('127.0.0.1',1961).main()