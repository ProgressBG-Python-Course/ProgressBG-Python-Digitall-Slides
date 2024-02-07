error_lines = (line for line in open('./syslog') if 'error' in line)
for line in error_lines:
    print(line)
