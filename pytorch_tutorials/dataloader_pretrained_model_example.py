import torch
import torchvision.models as models
from classification_dataset_sample import CustomDataset

if __name__ == "__main__":
    
    # Pretrained model 
    pretrained = True # or False
    model = models.resnet50(pretrained=True)
    
    # Dataloader initialization 
    dataset_class_instance = CustomDataset(...)
    train_dataloader = torch.utils.data.DataLoader(dataset_class_instance, batch_size=batch_size, shuffle=True, drop_last=True)
    
    # Loss function 
    criterion = torch.nn.CrossEntropyLoss()
    
    # Iteration over each example in the dataset
    for index, batch in enumerate(train_dataloader):
        image = batch['image']
        label = batch['label']
        prediction = model(image)
        output = criterion(prediction, label)
        output.backward()
