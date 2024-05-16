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
            # Update metrics
            try:
                status_code = int(line_parse[-2])
                file_size = int(line_parse[-1])
            except (ValueError, IndexError):
                continue  # Skip if there's an issue with parsing these values

            # Check if status code exists in the given dict
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Update total file size
            total_file_size += file_size

            # Update line count
            count += 1

            # Print metrics after every 10 lines
            if count % 10 == 0:
                print(f"File size: {total_file_size}")
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print(f"{k}: {v}")
                sys.stdout.flush()

except KeyboardInterrupt:
    pass
finally:
    # Print final metrics when the script is interrupted
    print(f"File size: {total_file_size}")
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print(f"{k}: {v}")
    sys.stdout.flush()
