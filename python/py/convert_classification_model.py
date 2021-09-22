import os

import torch
import torchvision.models as models


def main(root):
    model = models.mobilenet_v2(pretrained=True).eval()
    example = torch.rand(1, 3, 224, 224)
    traced_script_module = torch.jit.trace(model, example)
    model_path = os.path.join(root, "mobilenetv2.pt")
    traced_script_module.save(model_path)

    qmodel = models.quantization.mobilenet_v2(pretrained=True, quantize=True).eval()
    example = torch.rand(1, 3, 224, 224)
    traced_script_qmodule = torch.jit.trace(qmodel, example)
    qmodel_path = os.path.join(root, "quantize_mobilenetv2.pt")
    traced_script_qmodule.save(qmodel_path)


if __name__ == "__main__":
    dst_root = "./../models"
    os.makedirs(dst_root, exist_ok=True)
    main(dst_root)
