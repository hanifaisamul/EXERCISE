# 8-11. Archived Messages
def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop(0)
        sent_messages.append(current)

msg_list = ["Pesan A", "Pesan B"]
sent_list = []
send_messages(msg_list[:], sent_list)
print("Original msg list (tetap utuh):", msg_list)
