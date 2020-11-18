import os
import sys
import torch
import numpy as np
from PIL import Image
from glob import glob

DATA_TYPES = ['*.png']

def dictionary_contents(path,types,recursive=False):
    files = []
    if recursive:
        path = path+"/**/*"
    for type in types:
        if recursive:
            for x in glob(path+type,recursive=True):
                files.append(os.path.join(path,x))
        else:
            for x in glob(path+type):
                files.append(os.path.join(path,x))
    return files 

class CustomDataset(Dataset):
    """Example of custom dataset for classification."""

    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = dictionary_contents(path=root_dir, types=DATA_TYPES, recursive=False)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        """ example of __getitem__ where the name of the file is: '{class name}_{example number}.png' """
        image_path = self.image_paths[index]
        image = Image.open(image_path).convert("RGB")
        
        image_name = image_path.split('/')[-1]
        label = image_name.split('_')[0]
        
        if self.transform:
            image = self.transform(image)
        
        output = {}
        output['image'] = image
        output['label'] = label

        return output