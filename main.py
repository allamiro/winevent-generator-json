from logs.random_log_generator import generate_random_log
from logs.other_log_generator import generate_other_log
from utils.file_utils import write_to_file
from utils.other_utils import send_to_log_aggregator

def main():
    # Generate a random log and write it to a file
    log = generate_random_log()
    write_to_file(log, 'logs/random_log.json')

    # Generate another type of log and send it to a log aggregator
    log = generate_other_log()
    send_to_log_aggregator(log)

if __name__ == '__main__':
    main()
