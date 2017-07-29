import subprocess
import os
import glob


def restart_and_run_all(dir_path='.'):
    files = glob.glob('{}/*.ipynb'.format(dir_path))
    for f in files:
        print(f)
        subprocess.run(
            'jupyter nbconvert --to notebook --execute {} --output {}'.format(
                f, os.path.basename(f)
            ),
            shell=True
        )


def make_simple_python(dir_path='.'):
    files = glob.glob('{}/*.ipynb'.format(dir_path))
    template_path = os.path.join(os.path.dirname(__file__), 'simple_python.tpl')
    for f in files:
        print(f)
        subprocess.run(
            'jupyter nbconvert --to python {} --template {}'.format(
                f, template_path
            ),
            shell=True
        )
