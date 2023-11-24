from ping3 import ping

subnet = input('Какую подсеть будем пинговать? Введи число <192.168.???.1 - 192.168.???.255>: ')
address = f'192.168.{subnet}.1-255'

counter = 1

job_list = []
not_job_list = []

for i in range(1, 255):
    ip_address = f'192.168.{subnet}.{counter}'
    answer = ping(ip_address)
    print(ip_address)
    counter += 1
    if answer is None:
        not_job_list.append(ip_address)
    else:
        job_list.append(ip_address)

string_job_ip = '\n'.join(job_list)
string_not_job_ip = '\n'.join(not_job_list)

file_job = open(f'Job_list_IP({address}).txt', 'w+')
file_job.write(string_job_ip)
file_job.close()

file_not_job = open(f'Not_job_list_IP({address}).txt', 'w+')
file_not_job.write(string_not_job_ip)
file_not_job.close()
