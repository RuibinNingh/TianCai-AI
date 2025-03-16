import os
import subprocess

current_dir = os.getcwd()
node_path = os.path.join(current_dir, '.\\node-v22.14.0-win-x64')
os.environ['PATH'] = node_path + ';' + os.environ['PATH']
print("Updated PATH:", os.environ['PATH'])
command = 'cd .\\web && pnpm dev'
subprocess.run(command, shell=True)
