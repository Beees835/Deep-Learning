import numpy as np
import torch

# vector
vector = torch.tensor([1, 2, 3, 4])
print(vector.ndim)

# matrix
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(matrix.ndim)

print(f"dim={matrix.ndim}, shape={matrix.shape}")

npArray = np.arange(1, 21, dtype=np.float32)
print(npArray)

npArray = npArray.reshape((5, -1))
print(npArray)

# torch Array
torchArray = torch.from_numpy(npArray)
print(torchArray)
