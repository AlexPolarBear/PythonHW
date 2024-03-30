import time
import codecs
import datetime
import multiprocessing


def process_a(queue_AB, pipe_AB):
    while True:
        message = queue_AB.get()
        lower_message = message.lower()
        with open('artifacts/4_3.txt', 'a') as f:
            timestamp = datetime.datetime.now().timestamp()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S,%f')
            f.write(f"{formatted_timestamp}: Sent message '{message}' to process A\n")
        pipe_AB.send(lower_message)
        time.sleep(5)

def process_b(pipe_BA, queue_BC):
    while True:
        message = pipe_BA.recv()
        if message:
            encoded_message = codecs.encode(message, 'rot_13')
            with open('artifacts/4_3.txt', 'a') as f:
                timestamp = datetime.datetime.now().timestamp()
                formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S,%f')
                f.write(f"{formatted_timestamp}: Received message '{message}' from process B\n")
            queue_BC.put(encoded_message)

def main_process(queue_BC):
    while True:
        message = queue_BC.get()
        with open('artifacts/4_3.txt', 'a') as f:
            timestamp = datetime.datetime.now().timestamp()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S,%f')
            f.write(f"{formatted_timestamp}: Encoded message from process B: {message}\n")


if __name__ == "__main__":
    queue_AB = multiprocessing.Queue()
    queue_BC = multiprocessing.Queue()
    parent_conn, child_conn = multiprocessing.Pipe()
    process_a = multiprocessing.Process(target=process_a, args=(queue_AB, child_conn))
    process_b = multiprocessing.Process(target=process_b, args=(parent_conn, queue_BC))
    main_process = multiprocessing.Process(target=main_process, args=(queue_BC,))
    process_a.start()
    process_b.start()
    main_process.start()

    while True:
        user_input = input("Enter a message: ")
        with open('artifacts/4_3.txt', 'a') as f:
            timestamp = datetime.datetime.now().timestamp()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S,%f')
            f.write(f"{formatted_timestamp}: User input: {user_input}\n")
        if user_input == "exit":
            process_a.terminate()
            process_b.terminate()
            main_process.terminate()
            break
        queue_AB.put(user_input)
        time.sleep(2)