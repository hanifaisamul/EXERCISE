# 8-10. Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop(0)
        print(f"Mengirim: {current}")
        sent_messages.append(current)

msg_list = ["Pesan 1", "Pesan 2"]
sent_list = []
send_messages(msg_list, sent_list)
print("Msg list:", msg_list)
print("Sent list:", sent_list)
