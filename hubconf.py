import torch
def hello_world():
  print("hello world")
  return 14


import torchvision.models as models

model = models.vgg16(weights='IMAGENET1K_V1')
torch.save(model.state_dict(), 'model_weights.pth')


def get_model():
  print("hi")
  return model
