import os

import pytest
import torch
from torch.utils.data import Dataset

from mlops_cookie_project1.data import corrupt_mnist
from tests import _PATH_DATA

data_file_path = os.path.join(_PATH_DATA, "raw")


@pytest.mark.skipif(not os.path.exists(data_file_path), reason="Data files not found")
def test_my_dataset():
    train, test = corrupt_mnist()
    assert len(train) == 30000, f"Expected train dataset length 30000, but got {len(train)}"
    assert len(test) == 5000, f"Expected test dataset length 5000, but got {len(test)}"
    for dataset in [train, test]:
        for x, y in dataset:
            assert x.shape == (1, 28, 28), f"Expected input shape (1, 28, 28), but got {x.shape}"
            assert y in range(10), f"Expected target in range 0-9, but got {y}"
    train_targets = torch.unique(train.tensors[1])
    assert (train_targets == torch.arange(0, 10)).all(), "Train targets do not match expected range 0-9"
    test_targets = torch.unique(test.tensors[1])
    assert (test_targets == torch.arange(0, 10)).all(), "Test targets do not match expected range 0-9"
