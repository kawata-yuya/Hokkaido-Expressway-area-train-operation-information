import sys

import line
import muroran_status
import check_info_change

LINE_CHANNEL_ACCESS_TOKEN = sys.argv[1]
LAST_STATUS_CHECK_SECRET_URL = sys.argv[2]

def main():
    status = muroran_status.status_getter()

    info_changed = check_info_change.check(status, LAST_STATUS_CHECK_SECRET_URL)
    
    if info_changed:
        line.message_broadcast(status, LINE_CHANNEL_ACCESS_TOKEN)
    
    return


if __name__ == '__main__':
    main()