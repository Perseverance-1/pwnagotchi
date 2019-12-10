#Not complete, yet..

import logging
import subprocess
import string
import re
import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts

'''
brute needed, to install:
apt-get install nmap
Output stored in nmap folder as nmap.xml
Use in conjunction with brutespray plugin to dig deeper.
Output in /usr/share/brutespray/brutesprat_output
'''

class nmap(plugins.Plugin):
    __author__ = 'Perseverance'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __name__ = 'nmap'
    __description__ = 'An nmap plugin for pwnagotchi that implements port scanning post login'

    def __init__(self):
        self.text_to_set = ""
        
    def on_loaded(self):
        logging.info("[Brutespray] Plugin Loaded")

    def on_ready(self, agent):
        logging.info("[Brutespray] Spraying Network")
        brute = subprocess.run(('/usr/share/brutespray/./brutespray.py `echo -f /nmap/nmap.xml -t3 -P /opt/wordlists/ -c` '),shell=True,stdout=subprocess.PIPE)
        logging.info("brutespray complete")

    # called when the AI finished loading
    def on_ai_ready(self, agent):
        pass

    # called when the AI finds a new set of parameters
    def on_ai_policy(self, agent, policy):
        pass

    # called when the AI starts training for a given number of epochs
    def on_ai_training_start(self, agent, epochs):
        pass

    # called after the AI completed a training epoch
    def on_ai_training_step(self, agent, _locals, _globals):
        pass

    # called when the AI has done training
    def on_ai_training_end(self, agent):
        pass

    # called when the AI got the best reward so far
    def on_ai_best_reward(self, agent, reward):
        pass

    # called when the AI got the worst reward so far
    def on_ai_worst_reward(self, agent, reward):
        pass

    # called when the status is set to bored
    def on_bored(self, agent):
        pass

    # called when the status is set to excited
    def on_excited(self, agent):
        pass

    # called when the agent is waiting for t seconds
    def on_wait(self, agent, t):
        pass

    # called when the agent is sleeping for t seconds
    def on_sleep(self, agent, t):
        pass

    # called when an epoch is over (where an epoch is a single loop of the main algorithm)
    def on_epoch(self, agent, epoch, epoch_data):
        pass
