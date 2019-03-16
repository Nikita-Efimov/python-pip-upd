import os

pip_name = str(input('input your pip name: '))

print(pip_name)

stream = os.popen(' '.join([pip_name, 'list', '--format', 'freeze']))

pckg_list = stream.read()

for line in pckg_list.split('\n'):
    pckg = line.split('==')[0]
    os.system(' '.join([pip_name, 'install', '-U', pckg]))
