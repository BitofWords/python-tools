import subprocess
import os
import sys
import glob

sys.path.insert(0, os.path.dirname(__file__))
import filelib


def restart_and_run_all(path='.'):
    files = filelib.get_file_list(path, '.ipynb', True)
    for f in files:
        print(f)
        subprocess.run(
            'jupyter nbconvert --to notebook --execute {} --output {}'.format(
                f, os.path.basename(f)
            ),
            shell=True
        )


def make_simple_python(path='.'):
    files = filelib.get_file_list(path, '.ipynb', True)
    template_path = os.path.join(os.path.dirname(__file__), 'simple_python.tpl')
    for f in files:
        print(f)
        subprocess.run(
            'jupyter nbconvert --to python {} --template {}'.format(
                f, template_path
            ),
            shell=True
        )
        pytyon_file_path = os.path.splitext(f)[0] + '.py'
        with open(pytyon_file_path, 'r+') as py:
            lines = py.readlines()
            new_lines = []
            for l in lines:
                if not l.strip() == '#':
                    new_lines.append(l)
            py.seek(0)
            py.writelines(new_lines[1:])
            py.truncate()
