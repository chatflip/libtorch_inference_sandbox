import os

import torch
import torchvision.models as models


def main(root):
    model = models.segmentation.deeplabv3_mobilenet_v3_large(pretrained=True).eval()
    script_module = torch.jit.script(model)
    model_path = os.path.join(root, "deeplabv3_mobilenetv3_large.pt")
    script_module.save(model_path)


if __name__ == "__main__":
    dst_root = "./../models"
    os.makedirs(dst_root, exist_ok=True)
    main(dst_root)
