import os

import torch
import torchvision.models as models


def main(root):
    model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()
    script_module = torch.jit.script(model)
    model_path = os.path.join(root, "keypointrcnn_resnet50_fpn.pt")
    script_module.save(model_path)


if __name__ == "__main__":
    dst_root = "./../models"
    os.makedirs(dst_root, exist_ok=True)
    main(dst_root)
