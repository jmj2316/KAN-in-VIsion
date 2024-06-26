import torch.nn as nn

class ImageToPatches(nn.Module):
    def __init__(self, patch_size):
        super().__init__()
        self.P = patch_size

    def forward(self, x):
        P = self.P
        B, C, H, W = x.shape
        x = x.reshape(B, C, H // P, P, W // P, P)
        x = x.permute(0, 2, 4, 1, 3, 5)
        x = x.reshape(B, H // P * W // P, C * P * P)
        return x
