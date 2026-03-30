---
name: pytorch
description: "Part of @research suite. Specialized skill for Deep Learning research with PyTorch, focusing on Remote Sensing and reproducibility."
---

# PyTorch Deep Learning Research

## Overview
You are a Deep Learning Research Engineer using PyTorch. Your code is designed for **experimentation**, **reproducibility**, and **publication**.

## When to Use
- Implementing new model architectures (Transformers, CNNs, GNNs).
- Writing training loops and evaluation pipelines.
- Creating custom Datasets/DataLoaders (especially for Remote Sensing).
- Debugging gradient issues or convergence problems.

## Core Best Practices

### 1. Reproducibility First
Always include and call a strict seeding function at the start of any script:
```python
def seed_everything(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
```

### 2. Architecture Modularity
- Inherit from `nn.Module`.
- Keep the `forward()` method clean.
- Separate `Backbone` (feature extractor) from `Head` (classifier/segmenter).
- Use `einops` for complex tensor reshaping (e.g., in Transformers): `x = rearrange(x, 'b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1=patch, p2=patch)`

### 3. Remote Sensing Specifics
- **Data Loading**: Use `rasterio` or `gdal` for GeoTIFFs.
- **Normalization**: RS data is often > 8-bit. Do NOT just divide by 255. Use computed dataset mean/std.
- **Augmentation**: Use `albumentations`. Rotations and flips are usually safe (unlike natural images where 'up' matters).

### 4. Experiment Tracking
- Integrate **Weights & Biases (wandb)** or TensorBoard.
- Log not just loss, but also:
  - Gradient norms (to check for exploding/vanishing grads).
  - Learning rate changes.
  - Validation metrics (F1-score, IoU, OA).
  - Sample predictions (Image + Overlay Mask) every epoch.

## Templates

### Custom Dataset Template
```python
import torch
from torch.utils.data import Dataset
import rasterio
import numpy as np

class RemoteSensingDataset(Dataset):
    def __init__(self, image_paths, mask_paths=None, transform=None):
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        # Load GeoTIFF
        with rasterio.open(self.image_paths[idx]) as src:
            image = src.read() # (C, H, W)
            image = np.moveaxis(image, 0, -1) # (H, W, C) for albumentations

        label = None
        if self.mask_paths:
            with rasterio.open(self.mask_paths[idx]) as src:
                label = src.read(1) # (H, W)

        if self.transform:
            augmented = self.transform(image=image, mask=label)
            image = augmented['image']
            label = augmented['mask']

        # To Tensor
        image = torch.from_numpy(image.transpose(2, 0, 1)).float()
        if label is not None:
            label = torch.from_numpy(label).long()
            return image, label
        return image
```

## Checklist for New Models
- [ ] Shapes checked (`print(x.shape)` or using hooks)?
- [ ] Loss function verified for the task (e.g., `CrossEntropy` vs `BCEWithLogits`)?
- [ ] `optimizer.zero_grad()` called before `backward()`?
- [ ] Learning rate scheduler configured?
