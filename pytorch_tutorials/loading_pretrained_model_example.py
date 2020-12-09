import torch
import torchvision.models as models

if if __name__ == "__main__":
    pretrained = True # or False
    model = models.resnet50(pretrained=True)
    train_dataloader = # ....
    criterion = torch.nn.CrossEntropyLoss()
    
    for index, batch in enumerate(train_dataloader):
        image = batch['image']
        label = batch['label']
        prediction = model(image)
        output = criterion(prediction, label)
        output.backward()
        
        