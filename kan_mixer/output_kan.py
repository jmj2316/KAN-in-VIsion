import torch.nn as nn
from .kan_linear import KANLinear

class OutputKAN(nn.Module):
    def __init__(self, n_tokens, n_channel, n_output):
        super().__init__()
        self.layer_norm = nn.LayerNorm([n_tokens, n_channel])
        self.global_avg_pool = nn.AdaptiveAvgPool1d(1)
        self.out_kan = KANLinear(n_channel, n_output)
        self.activations = None

    def forward(self, x):
        x = self.layer_norm(x)
        x = x.permute(0, 2, 1)
        x = self.global_avg_pool(x)
        x = x.squeeze(-1)
        output = self.out_kan(x)
        self.activations = self.out_kan.acts
        return output
