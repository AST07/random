import subprocess
packages=subprocess.check_output('pip freeze').decode('utf-8').split('\r\n')[:-1]
for package in packages:
	response=subprocess.call(f'pip uninstall -y {package}')