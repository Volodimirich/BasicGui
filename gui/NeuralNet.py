from typing import Any
from torchvision.models import resnet18, ResNet18_Weights
from torchvision import transforms
from PIL import Image
import numpy as np
import torch
import requests

response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

class NeuralNet():
    def __init__(self):
        self.net = resnet18(pretrained=True)
        self.net.eval()
        self.transforms = transforms.Compose([
            # v2.ToImage(),  # Convert to tensor, only needed if you had a PIL image
            transforms.ToTensor(),
            transforms.Resize((256, 256))
        ])
        
        response = requests.get("https://git.io/JJkYN")
        self.labels = response.text.split("\n")
        
        
    def predict(self, path):
        print(path)
        img = np.array(Image.open(path))
        tens = self.transforms(img)
        with torch.no_grad():
            pred = self.net(tens.unsqueeze(0))
        print(self.labels[pred.argmax().item()], pred.argmax().item(), )
        return self.labels[pred.argmax().item()]
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.predict(args, kwds)
        
        