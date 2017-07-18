import sys
import json
import threading
import simple_socket
import time









def encrypt(user_input, shifting_number):
    shifting_number = int(shifting_number)
    user_input = list(user_input)
    alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    word_length = len(user_input)
    i = 0
    u = 0
    o = 0
    for i in range(word_length):
        for u in range(26):
            if user_input[i] == alphabet[u]:
                user_input[i] = (u + shifting_number) % 26
    for o in range(word_length):
        for a in range(26):
            if user_input[o] == alphabet.index(alphabet[a]):
                user_input[o] = alphabet[a]

    user_input = "".join(user_input)
    return user_input










def json_creator(encrypted_user_input, zeit, shifting_number, sender, text_length):
    nachricht = {"nachrichten_id": 1,
                 "text": encrypted_user_input,
                 "text_länge": text_length,
                 "verschlüsselung":
                 {"algorithmus": "caesar",
                  "parameter": [shifting_number],
                  "verschlüsselte_parameter": []},
                 "sender_name": sender,
                 "zeitstempel": zeit}
    json_text = json.dumps(nachricht)
    return json_text












def sending():
    while True:
        for line in sys.stdin:
            user_input = line
            shifting_number = 0
            global zeit
            zeit = time.time()
            encrypted_user_input = encrypt(user_input, shifting_number)
            print("".join(encrypted_user_input))
            text_length = len(encrypted_user_input) - 1
            json_text = json_creator(encrypted_user_input, zeit, shifting_number, sender, text_length)
            print(json_text)
            my_socket.send(json_text)











def receiving():
    while True:
        nachricht = my_socket.receive()
        nachricht = str(nachricht)
        print(nachricht)
        exported_json = json.loads(nachricht)
        text = exported_json["text"]
        print(text)



my_socket = simple_socket.connect_as_client(server_address = "10.1.0.239", server_port = 8888)

sender = input(str("Guten Tag, wer sind Sie? "))

        
thread = threading.Thread(target = sending, args = ())
thread.start()
        
thread = threading.Thread(target = receiving, args = ())
thread.start()
        
