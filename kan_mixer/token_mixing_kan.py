import torch.nn as nn
from .kan_linear import KANLinear

class TokenMixingKAN(nn.Module):
    def __init__(self, n_tokens, n_channel, n_hidden):
        super().__init__()
        self.layer_norm = nn.LayerNorm([n_tokens, n_channel])
        self.kan1 = KANLinear(n_tokens, n_hidden)
        self.kan2 = KANLinear(n_hidden, n_tokens)
        self.activations = None

    def forward(self, X):
        z = self.layer_norm(X)
        z = z.permute(0, 2, 1)
        z = self.kan1(z)
        z = self.kan2(z)
        z = z.permute(0, 2, 1)
        U = X + z
        self.activations = U
        return U
