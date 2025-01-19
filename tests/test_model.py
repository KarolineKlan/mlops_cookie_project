import pytest
import torch

from mlops_cookie_project1.model import MyAwesomeModel


@pytest.mark.parametrize("batch_size", [32, 64])
def test_model(batch_size: int) -> None:
    model = MyAwesomeModel()
    x = torch.randn(batch_size, 1, 28, 28)
    y = model(x)
    assert y.shape == (batch_size, 10), f"Expected output shape ({batch_size}, 10), but got {y.shape}"



