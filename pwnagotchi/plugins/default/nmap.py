//
Not complete, yet..
//

import logging
import subprocess
import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
#import nmap

class nmap(plugins.Plugin):
    __author__ = 'Perseverance'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __name__ = 'nmap'
    __description__ = 'An nmap plugin for pwnagotchi that implements port scanning post login'

    def __init__(self):
        logging.info("[Loaded] nmap plugin")
        
    def on_loaded(self):
        cracked = ['ls ~/handshakes/ | grep *.cracked']
        if 'cracked' not in self.options or ('cracked' in self.options and self.options['cracked'] is None):
            logging.info("[NMAP] No handshakes cracked")
        else:
            crack = subprocess.run(('aircrack-ng -w `echo '+OPTIONS['wordlist_folder']+'*.txt | sed \'s/\ /,/g\'` -l '+filename+'.cracked -q -b '+crack+' '+filename+' | grep KEY'),shell=True,stdout=subprocess.PIPE)
    crack = crack.stdout.decode('utf-8').strip()
    logging.info("[quickdic] "+result2)
    if result2 != "KEY NOT FOUND":
        key = re.search('\[(.*)\]', crack)
        pwd = str(key.group(1))
        set_text("Cracked password: "+pwd)
        display.update(force=True)

    # called when everything is ready and the main loop is about to start
    def on_ready(self, agent):
        logging.info("unit is ready")
        # you can run custom bettercap commands if you want
        #   agent.run('ble.recon on')
        # or set a custom state
        #   agent.set_bored()

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
