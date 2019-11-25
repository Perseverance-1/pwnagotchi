import pwnagotchi.mesh.wifi as wifi

range = (-.7, 1.02)
fuck_zero = 1e-20


class RewardFunction(object):
    def __call__(self, epoch_n, state):
        tot_epochs = epoch_n + fuck_zero
        tot_interactions = max(state['num_deauths'] + state['num_associations'], state['num_handshakes']) + fuck_zero #state['num_crack']
        tot_channels = wifi.NumChannels

        h = state['num_handshakes'] / tot_interactions
        a = .2 * (state['active_for_epochs'] / tot_epochs)
        c = .1 * (state['num_hops'] / tot_channels)
        #k = .3 * (state['num_crack'] / tot_interactions)

        b = -.3 * (state['blind_for_epochs'] / tot_epochs)
        m = -.3 * (state['missed_interactions'] / tot_interactions)
        i = -.2 * (state['inactive_for_epochs'] / tot_epochs)

        return h + a + c + b + i + m #+k
