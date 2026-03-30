import datetime

def log_message(message):

    timestamp  = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"

    with open(filename,"a") as l:
        l.write(log_entry)
filename="logs.txt"
# Example usage
while True:
    input_message = input("Enter a log message or exit:")
    if input_message.lower()=="exit":
        break
    log_message(input_message)
