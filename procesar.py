import sys, subprocess
url = sys.argv[1]
print('Enlace:', url)
subprocess.run(['ollama', 'run', 'llama3.2:1b', 'Genera una pagina HTML de afiliados'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'ok'])
subprocess.run(['git', 'push', 'origin', 'maestro'])