import sys

import line
import muroran_status

LINE_CHANNEL_ACCESS_TOKEN = sys.argv[1]

def main():
    status = muroran_status.status_getter()

    if status is not None:
        line.message_broadcast('TEST', LINE_CHANNEL_ACCESS_TOKEN)
    
    return


if __name__ == '__main__':
    main()