import os
import time
import random

protocols = {
    "HTTP": {
        "port": 80,
        "full_name": "Hypertext Transfer Protocol",
        "common_usage": "Web browsing",
        "hint": "8_"
    },
    "FTP": {
        "port": [20, 21],
        "full_name": "File Transfer Protocol",
        "common_usage": "File transfers",
        "hint": "2_ & 2_ (Sequential)"
    },
    "SMB/CIFS": {
        "port": 445,
        "full_name": "Server Message Block/Common Internet File System",
        "common_usage": "File sharing, printer sharing, network browsing,\nand inter-process communication over a computer network",
        "hint": "44_"
    },
    "IMAPS": {
        "port": 993,
        "full_name": "Internet Message Access Protocol Secure",
        "common_usage": "Secure email retrieval",
        "hint": "99_"
    },
    "POP3": {
        "port": 110,
        "full_name": "Post Office Protocol version 3",
        "common_usage": "Email retrieval",
        "hint": "11_"
    },
    "POP3S": {
        "port": 995,
        "full_name": "Post Office Protocol version 3 Secure",
        "common_usage": "Secure email retrieval",
        "hint": "99_"
    },
    "HTTPS": {
        "port": 443,
        "full_name": "Hypertext Transfer Protocol Secure",
        "common_usage": "Secure web browsing",
        "hint": "44_"
    },
    "TELNET": {
        "port": 23,
        "full_name": "Telnet",
        "common_usage": "Remote terminal access",
        "hint": "2_"
    },
    "PPTP": {
        "port": 1723,
        "full_name": "Point-to-Point Tunneling Protocol",
        "common_usage": "Virtual private network (VPN) connections",
        "hint": "172_"
    },
    "SNMP": {
        "port": [161, 162],
        "full_name": "Simple Network Management Protocol",
        "common_usage": "Network device management",
        "hint": "16_ & 16_ Sequential"
    },
    "LDAPS": {
        "port": 636,
        "full_name": "Lightweight Directory Access Protocol Secure",
        "common_usage": "Secure LDAP communication",
        "hint": "63_"
    },
    "AFP/SLP": {
        "port": 427,
        "full_name": "Apple Filing Protocol/Service Location Protocol",
        "common_usage": "Apple file sharing and service discovery",
        "hint": "42_"
    },
    "AFP": {
        "port": 548,
        "full_name": "Apple Filing Protocol",
        "common_usage": "Apple file sharing",
        "hint": "54_"
    },
    "FTPS": {
        "port": [989, 990],
        "full_name": "File Transfer Protocol Secure",
        "common_usage": "Secure file transfers",
        "hint": "98_ & 99_ Sequential"
    },
    "LDAP": {
        "port": 389,
        "full_name": "Lightweight Directory Access Protocol",
        "common_usage": "Directory service communication",
        "hint": "38_"
    },
    "NETBIOS/NETBT": {
        "port": [137, 138, 139],
        "full_name": "NetBIOS/NetBT",
        "common_usage": "NetBIOS communication over TCP/IP",
        "hint": "13_ , 13_ & 13_"
    },
    "RADIUS": {
        "port": [1812, 1813],
        "full_name": "Remote Authentication Dial-In User Service",
        "common_usage": "User authentication and accounting for network access",
        "hint": "181_ & 1813"
    },
    "IMAP": {
        "port": 143,
        "full_name": "Internet Message Access Protocol",
        "common_usage": "Email retrieval",
        "hint": "14_"
    },
    "Diameter": {
        "port": 3868,
        "full_name": "Diameter",
        "common_usage": "Authentication, authorization, and accounting (AAA) protocol",
        "hint": "386_"
    },
    "L2TP": {
        "port": 1701,
        "full_name": "Layer 2 Tunneling Protocol",
        "common_usage": "VPN connections",
        "hint": "170_"
    },
    "SSH": {
        "port": 22,
        "full_name": "Secure Shell",
        "common_usage": "Secure remote administration",
        "hint": "2_"
    },
    "RDP": {
        "port": 3389,
        "full_name": "Remote Desktop Protocol",
        "common_usage": "Remote desktop access",
        "hint": "338_"
    },
    "SRTP": {
        "port": 5004,
        "full_name": "Secure Real-time Transport Protocol",
        "common_usage": "Secure audio and video streaming",
        "hint": "500_"
    },
    "SMTP": {
        "port": 25,
        "full_name": "Simple Mail Transfer Protocol",
        "common_usage": "Email transfer",
        "hint": "2_"
    },
    "DNS": {
        "port": 53,
        "full_name": "Domain Name System",
        "common_usage": "Domain name resolution",
        "hint": "5_"
    },
    "TACAS+": {
        "port": 49,
        "full_name": "Terminal Access Controller Access-Control System Plus",
        "common_usage": "Authentication, authorization, and accounting (AAA) protocol",
        "hint": "4_"
    },
    "DHCP": {
        "port": [68, 67],
        "full_name": "Dynamic Host Configuration Protocol",
        "common_usage": "Automatic IP address assignment",
        "hint": "6_ & 6_ Sequential"
    },
    "Kerbos": {
        "port": 88,
        "full_name": "Kerberos",
        "common_usage": "Network authentication protocol",
        "hint": "8_"
    }
}

def clear_screen():
    if os.name == "nt":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Linux and macOS

def format_exit_message(message):
    punctuation_marks = ['.', '!', '?']
    for mark in punctuation_marks:
        message = message.replace(mark, mark + '\n')
    return message

def check_ports(user_input, actual_ports):
    user_ports = user_input.replace(',', ' ').split()
    if isinstance(actual_ports, int):
        return len(user_ports) == 1 and str(actual_ports) == user_ports[0]
    elif isinstance(actual_ports, list):
        if set(user_ports) == set(map(str, actual_ports)):
            return True
        elif isinstance(actual_ports, str) and '-' in user_input:
            # Check if the user input matches the format Port1-Port3
            port_range = actual_ports.split('-')
            try:
                start_port, end_port = map(int, port_range)
                user_start, user_end = map(int, user_input.split('-'))
                if start_port <= user_start <= user_end <= end_port:
                    return True
            except ValueError:
                pass
        return False
    else:
        return False

def flashcard_game(protocols):
    questions = list(protocols.keys())
    random.shuffle(questions)
    correct_answers = 0
    total_questions = len(protocols)

    for protocol in questions:
        details = protocols[protocol]
        clear_screen()
        print("What is/are the port number(s) for", protocol + "?")

        previous_inputs = []  # Store previous inputs for the current question

        while True:
            user_input = input("\nEnter the port number(s): ")
            user_ports = user_input.split('/')

            # Check if the user's input matches the actual port number(s)
            if check_ports(user_input, details["port"]):
                print("Correct!")
                print("Full name:", details["full_name"])
                print("Common usage:", details["common_usage"])
                correct_answers += 1
                break  # Exit the loop and proceed to the next protocol
            else:
                clear_screen()
                print("Not quite, please try again.")
                print("\nWhat is/are the port number(s) for", protocol + "?")
                print("\nHint:", details["hint"])

                # Add the user's input to the list of previous inputs
                if user_input not in previous_inputs:
                    previous_inputs.append(user_input)

                # Display all previous inputs for the current question
                if previous_inputs:
                    print("\nPrevious inputs:")
                    for prev_input in previous_inputs:
                        print(prev_input)

        # Wait for the user to continue
        input("Press ENTER key to continue...")

    clear_screen()
    if correct_answers == total_questions:
        exit_message = "Congratulations! You answered all the questions correctly! The game is now over and the script will now exit. Thank you for playing!"
    else:
        exit_message = f"Game over. You answered {correct_answers} out of {total_questions} questions correctly. The script will now exit. Thank you for playing!"

    formatted_exit_message = format_exit_message(exit_message)
    print(formatted_exit_message)




# Call the flashcard_game function
flashcard_game(protocols)