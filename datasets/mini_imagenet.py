import os.path as osp
from PIL import Image, ImageFilter
from torch.utils.data import Dataset
from torchvision import transforms
import numpy as np


class MiniImageNet(Dataset):

    def __init__(self, data_path, setname, backbone, augment):
        csv_path = osp.join(data_path, setname + '.csv')
        lines = [x.strip() for x in open(csv_path, 'r').readlines()][1:]

        data = []
        label = []
        lb = -1

        self.wnids = []

        for l in lines:
            name, wnid = l.split(',')
            if wnid not in self.wnids:
                self.wnids.append(wnid)
                lb += 1

            if setname == 'd':
                path = osp.join(data_path, 'test', str(lb), name)
            else:
                path = osp.join(data_path, 'images', name)

            data.append(path)
            label.append(lb)

        self.data = data
        self.label = label

        image_size = 84
        if augment and setname == 'train':
            transforms_list = [
                transforms.RandomResizedCrop(image_size),
                transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
            ]
        else:
            transforms_list = [
                transforms.Resize(92),
                transforms.CenterCrop(image_size),
                transforms.ToTensor(),
            ]

        # Transformation
        if backbone == 'ConvNet':
            self.transform = transforms.Compose(
                transforms_list + [
                    transforms.Normalize(np.array([0.485, 0.456, 0.406]),
                                         np.array([0.229, 0.224, 0.225]))
                ])
        elif backbone == 'Res12':
            self.transform = transforms.Compose(
                transforms_list + [
                    transforms.Normalize(np.array([x / 255.0 for x in [120.39586422, 115.59361427, 104.54012653]]),
                                         np.array([x / 255.0 for x in [70.68188272, 68.27635443, 72.54505529]]))
                ])
        elif backbone == 'Res18':
            self.transform = transforms.Compose(
                transforms_list + [
                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])
                ])
        elif backbone == 'WRN' or backbone == 'WRN_28':
            self.transform = transforms.Compose(
                transforms_list + [
                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])
                ])
        else:
            raise ValueError('Non-supported Network Types. Please Revise Data Pre-Processing Scripts.')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        path, label = self.data[i], self.label[i]
        image = Image.open(path).convert('RGB')
        orig = self.transform(image)
        return orig, label