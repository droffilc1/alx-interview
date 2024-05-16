#!/usr/bin/python3
""" 0-stats """

import sys


total_file_size = 0
count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        # Parse the line
        line_parse = line.split(" ")

        if len(line_parse) > 4:
            # UPdate metrics
            status_code = int(line_parse[-2])
            file_size = int(line_parse[-1])

            # Check if status code exists in a given dict
            if status_code in status_codes.keys():
                status_codes[status_code] += 1

            # Update total file size
            total_file_size += file_size

            # Update line count
            count += 1

        # Print metrics after every 10 lines
        if count % 10 == 0:
            # Reset count
            count = 0

            # Print the update file size
            print(f"File size: {total_file_size}")

            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print(f"{k}: {v}")

except KeyboardInterrupt:
    pass
