# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module setuptools script."""

import distutils.command.build
from setuptools import setup

description = """PySC2LiU

PySC2LiU is a fork of DeepMind's PySC2 component with a modified GUI for
training students in building PyCommandCenter agents.

PySC2 is DeepMind's Python component of the StarCraft II Learning Environment
(SC2LE). It exposes Blizzard Entertainment's StarCraft II Machine Learning API
as a Python RL Environment. This is a collaboration between DeepMind and
Blizzard to develop StarCraft II into a rich environment for RL research. PySC2
provides an interface for RL agents to interact with StarCraft 2, getting
observations and sending actions.

We have published an accompanying blogpost and paper
https://deepmind.com/blog/deepmind-and-blizzard-open-starcraft-ii-ai-research-environment/
which outlines our motivation for using StarCraft II for DeepRL research, and
some initial research results using the environment.

Read the README at https://github.com/deepmind/pysc2 for more information.
"""


class BuildCommand(distutils.command.build.build):

  def initialize_options(self):
    distutils.command.build.build.initialize_options(self)
    # To avoid conflicting with the Bazel BUILD file.
    self.build_base = '_build'


setup(
    name='PySC2LiU',
    version='0.0.1',
    description='Starcraft II environment and library for training students.',
    long_description=description,
    author='Daniel de Leng',
    author_email='daniel.de.leng@liu.se',
    cmdclass={'build': BuildCommand},
    license='Apache License, Version 2.0',
    keywords='StarCraft AI',
    #url='https://github.com/deepmind/pysc2',
    packages=[
        'pysc2',
        'pysc2.agents',
        'pysc2.bin',
        'pysc2.env',
        'pysc2.lib',
        'pysc2.maps',
        'pysc2.run_configs',
        'pysc2.tests',
    ],
    install_requires=[
        'absl-py==2.1.0',
        'deepdiff==7.0.1',
        'dm-env==1.6',
        'enum34==1.1.10',
        'mock==5.1.0',
        'mpyq==0.2.5',
        'numpy==2.0.0',
        'portpicker==1.6.0',
        'protobuf==3.20.3',
        'pygame==2.6.0',
        'requests==2.32.3',
        's2clientprotocol==5.0.12.91115.0',
        's2protocol==5.0.12.91115.0',
        'sk-video==1.1.10',
        'websocket-client==1.8.0,',
    ],
    entry_points={
        'console_scripts': [
            'pysc2_agent = pysc2.bin.agent:entry_point',
            'pysc2_play = pysc2.bin.play:entry_point',
            'pysc2_replay_info = pysc2.bin.replay_info:entry_point',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
