#!/usr/bin/python3
""" 0-stats """

import sys

total_file_size = 0
count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        # Strip and split the line to parse the components
        line_parse = line.strip().split(" ")

        # Ensure line has enough components to avoid index errors
        if len(line_parse) > 4:
            try:
                # Assume the status code is the second to last element
                status_code = int(line_parse[-2])
                # Assume the file size is the last element
                file_size = int(line_parse[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code if status code is in the dictionary
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Update line count
                count += 1

                # Print metrics after every 10 lines
                if count % 10 == 0:
                    print(f"File size: {total_file_size}")
                    for k, v in sorted(status_codes.items()):
                        if v != 0:
                            print(f"{k}: {v}")
                    sys.stdout.flush()
            except (ValueError, IndexError):
                continue  # Skip if there's an issue with parsing these values

except KeyboardInterrupt:
    pass
finally:
    # Print final metrics when the script is interrupted
    print(f"File size: {total_file_size}")
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print(f"{k}: {v}")
    sys.stdout.flush()
