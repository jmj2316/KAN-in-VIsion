import torch.nn as nn
from .image_to_patches import ImageToPatches
from .per_patch_kan import PerPatchKAN
from .token_mixing_kan import TokenMixingKAN
from .channel_mixing_kan import ChannelMixingKAN
from .output_kan import OutputKAN

class KAN_Mixer(nn.Module):
    def __init__(self, n_layers, n_channel, n_hidden, n_output, image_size, patch_size, n_image_channel):
        super().__init__()
        n_tokens = (image_size // patch_size) ** 2
        n_pixels = n_image_channel * patch_size ** 2

        self.ImageToPatch = ImageToPatches(patch_size=patch_size)
        self.PerPatchKAN = PerPatchKAN(n_pixels, n_channel)
        self.MixerStack = nn.Sequential(*[
            nn.Sequential(
                TokenMixingKAN(n_tokens, n_channel, n_hidden),
                ChannelMixingKAN(n_tokens, n_channel, n_hidden)
            ) for _ in range(n_layers)
        ])
        self.OutputKAN = OutputKAN(n_tokens, n_channel, n_output)

    def forward(self, x):
        x = self.ImageToPatch(x)
        x = self.PerPatchKAN(x)
        x = self.MixerStack(x)
        return self.OutputKAN(x)
