import torch.nn as nn
from .kan_linear import KANLinear

class ChannelMixingKAN(nn.Module):
    def __init__(self, n_tokens, n_channel, n_hidden):
        super().__init__()
        self.layer_norm = nn.LayerNorm([n_tokens, n_channel])
        self.kan3 = KANLinear(n_channel, n_hidden)
        self.kan4 = KANLinear(n_hidden, n_channel)
        self.activations = None

    def forward(self, U):
        z = self.layer_norm(U)
        z = self.kan3(z)
        z = self.kan4(z)
        Y = U + z
        self.activations = Y
        return Y
