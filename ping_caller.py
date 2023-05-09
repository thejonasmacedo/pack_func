import subprocess, datetime, os


def ping(site, num_pings='4', timeout=None):

    # ping website and store output in a variable
    if num_pings:
        if timeout:
            ping_output = subprocess.check_output(['/bin/ping', '-c', num_pings, '-W', timeout,  site])
            ping_output = ping_output.decode('utf-8')
            return ping_output
        ping_output = subprocess.check_output(['/bin/ping', '-c', num_pings,  site])
        ping_output = ping_output.decode('utf-8')
        return ping_output
    
    if timeout:
        ping_output = subprocess.check_output(['/bin/ping', '-W', timeout, site])
        ping_output = ping_output.decode('utf-8')
        return ping_output


    ping_output = subprocess.check_output(['/bin/ping', site])

    # Decode output as string and print
    ping_output = ping_output.decode('utf-8')
    return ping_output

log_file_path = datetime.datetime.now().strftime('%d-%m-%Y') + '_logfile.txt'

def ping_terminal(site, num_pings='4', timeout=None):
    path = os.path.dirname(__file__)
    terminal_ping_output = ping(site, num_pings, timeout)
    with open(f'{path}/{log_file_path}', 'a') as log_file:
        log_file.write(
            f'This is the terminal ping: {terminal_ping_output}',
            
        )
    return terminal_ping_output

print(ping_terminal('youtube.com'))