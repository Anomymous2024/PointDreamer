import torch
from lightconvpoint.nn import Module
from lightconvpoint.utils.functional import batch_gather

def max_pool(input: torch.Tensor, indices: list) -> torch.Tensor:
    features = batch_gather(input, dim=2, index=indices[0]).contiguous()
    features = features.max(dim=3)[0]
    return features

class MaxPooling(Module):

    def __init__(self, sampling, neighborhood_search, ratio=1, neighborhood_size=16):
        super().__init__()

        self.sampling = sampling
        self.neighborhood_size = neighborhood_size
        self.neighborhood_search = neighborhood_search
        self.ratio = 1

    def forward_without_features(self, pos):
        if self.ratio == 1:
            ids = self.neighborhood_search(pos, pos, self.neighborhood_size)
            return None, [pos], [ids]
        else:
            _, support = self.sampling(pos, ratio=self.ratio, return_support_points=True)
            ids = self.neighborhood_search(pos, support)
            return None, [support], [ids]

    def forward_with_features(self, x: torch.Tensor, pos: torch.Tensor, support_points: list, indices: list) -> torch.Tensor:
        return max_pool(x, indices)