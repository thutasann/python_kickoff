import subprocess

script_path = './test.sh'

result = subprocess.run(['sh', script_path], capture_output=True, text=True)

print('Output:', result.stdout)
print('Error:', result.stderr)
print('Return code:', result.returncode)
