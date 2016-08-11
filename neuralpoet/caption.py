import subprocess
import json
import os
from os.path import join as joinpath
from os.path import abspath, dirname
import sys


class CaptionRunner:
    """
    Caption Runner
    """
    runpath = abspath(joinpath(dirname(__file__), 'neuraltalk2'))

    def __init__(self, *args, **options):
        self.args = args
        self.options = {}
        for k, v in options.items():
            if os.path.exists(str(v)):
                self.options[k] = os.path.relpath(v, self.runpath)
            else:
                self.options[k] = v

    def __call__(self):
        os.chdir(self.runpath)
        output = subprocess.check_output(runner.command.split())
        return json.load(open('vis/vis.json'))

    @property
    def command(self):
        options = tuple(['-{k} {v}'.format(k=k, v=v) for k,v in self.options.items()])
        return ' '.join(self.args + options)

    def __repr__(self):
        return self.command

if __name__ == '__main__':
    runner = CaptionRunner('th', 'eval.lua',
                           num_images='-1',
                           gpuid='-1',
                           model=sys.argv[1],
                           image_folder=sys.argv[2])
    print(runner())
