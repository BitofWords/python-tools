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


def make_simple(path='.', output_format='python', ext='.py'):
    files = filelib.get_file_list(path, '.ipynb', True)
    template_path = os.path.join(os.path.dirname(__file__), 'simple_python.tpl')
    for f in files:
        print(f)
        subprocess.run(
            'jupyter nbconvert --to {} {} --template {}'.format(
                output_format, f, template_path
            ),
            shell=True
        )
        pytyon_file_path = os.path.splitext(f)[0] + ext
        with open(pytyon_file_path, 'r+') as py:
            lines = py.readlines()
            new_lines = []
            for i in range(len(lines) - 1):
                if lines[i].strip() == '#':
                    if lines[i + 1].strip() == '':
                        pass
                    else:
                        new_lines.append(lines[i])
                else:
                    new_lines.append(lines[i])
            py.seek(0)
            py.writelines(new_lines[1:])
            py.truncate()


def make_simple_python(path='.'):
    make_simple(path)


def make_simple_shell(path='.'):
    make_simple(path, 'script', '.sh')
