# stdlib
from typing import Dict
from typing import Union

allowlist: Dict[str, Union[str, Dict[str, str]]] = {}  # (path: str, return_type:type)

# MNIST
allowlist["torchvision.transforms.Compose"] = "torchvision.transforms.Compose"
# allowlist["torchvision.transforms.Compose.__iter__"] = "torchvision.transforms.ToTensor"
# TODO: Compose.transforms property only exists on the object not on the class?
# allowlist["torchvision.transforms.Compose.transforms"] = "syft.lib.python.List"
allowlist["torchvision.transforms.ToTensor"] = "torchvision.transforms.ToTensor"
allowlist["torchvision.transforms.Normalize"] = "torchvision.transforms.Normalize"
# TODO: Normalize properties only exists on the object not on the class?
# allowlist["torchvision.transforms.Normalize.inplace"] = "syft.lib.python.Bool"
# TODO: mean and std are actually tuples
# allowlist["torchvision.transforms.Normalize.mean"] = "syft.lib.python.List"
# allowlist["torchvision.transforms.Normalize.std"] = "syft.lib.python.List"
allowlist["torchvision.datasets.MNIST"] = "torchvision.datasets.MNIST"
allowlist["torchvision.datasets.MNIST.__len__"] = "syft.lib.python.Int"
allowlist["torchvision.datasets.VisionDataset"] = "torchvision.datasets.VisionDataset"
allowlist["torchvision.datasets.VisionDataset.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.CelebA"] = "torchvision.datasets.CelebA"
allowlist["torchvision.datasets.CelebA.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.CIFAR10"] = "torchvision.datasets.CIFAR10"
allowlist["torchvision.datasets.CIFAR10.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Cityscapes"] = "torchvision.datasets.Cityscapes"
allowlist["torchvision.datasets.Cityscapes.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.CocoCaptions"] = "torchvision.datasets.CocoCaptions"
allowlist["torchvision.datasets.CocoCaptions.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.CocoDetection"] = "torchvision.datasets.CocoDetection"
allowlist["torchvision.datasets.CocoDetection.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.EMNIST"] = "torchvision.datasets.EMNIST"
allowlist["torchvision.datasets.EMNIST.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.FakeData"] = "torchvision.datasets.FakeData"
allowlist["torchvision.datasets.FakeData.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.FashionMNIST"] = "torchvision.datasets.FashionMNIST"
allowlist["torchvision.datasets.FashionMNIST.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Flickr8k"] = "torchvision.datasets.Flickr8k"
allowlist["torchvision.datasets.Flickr8k.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Flickr30k"] = "torchvision.datasets.Flickr30k"
allowlist["torchvision.datasets.Flickr30k.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.HMDB51"] = "torchvision.datasets.HMDB51"
allowlist["torchvision.datasets.HMDB51.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.ImageNet"] = "torchvision.datasets.ImageNet"
allowlist["torchvision.datasets.ImageNet.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Kinetics400"] = "torchvision.datasets.Kinetics400"
allowlist["torchvision.datasets.Kinetics400.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.KMNIST"] = "torchvision.datasets.KMNIST"
allowlist["torchvision.datasets.KMNIST.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.LSUN"] = "torchvision.datasets.LSUN"
allowlist["torchvision.datasets.LSUN.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Omniglot"] = {
    "return_type": "torchvision.datasets.Omniglot",
    "min_version": "0.7.0",
}
allowlist["torchvision.datasets.Omniglot.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.PhotoTour"] = "torchvision.datasets.PhotoTour"
allowlist["torchvision.datasets.PhotoTour.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.Places365"] = {
    "return_type": "torchvision.datasets.Places365",
    "min_version": "0.7.0",
}
allowlist["torchvision.datasets.Places365.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.QMNIST"] = "torchvision.datasets.QMNIST"
allowlist["torchvision.datasets.QMNIST.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.SBDataset"] = "torchvision.datasets.SBDataset"
allowlist["torchvision.datasets.SBDataset.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.SBU"] = "torchvision.datasets.SBU"
allowlist["torchvision.datasets.SBU.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.STL10"] = "torchvision.datasets.STL10"
allowlist["torchvision.datasets.STL10.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.SVHN"] = "torchvision.datasets.SVHN"
allowlist["torchvision.datasets.SVHN.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.UCF101"] = "torchvision.datasets.UCF101"
allowlist["torchvision.datasets.UCF101.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.USPS"] = "torchvision.datasets.USPS"
allowlist["torchvision.datasets.USPS.__len__"] = "syft.lib.python.Int"

allowlist[
    "torchvision.datasets.VOCSegmentation"
] = "torchvision.datasets.VOCSegmentation"
allowlist["torchvision.datasets.VOCSegmentation.__len__"] = "syft.lib.python.Int"

allowlist["torchvision.datasets.VOCDetection"] = "torchvision.datasets.VOCDetection"
allowlist[
    "torchvision.datasets.VOCDetection.__len__"
] = "torchvision.datasets.VOCDetection"

allowlist["torchvision.transforms.CenterCrop"] = "torchvision.transforms.CenterCrop"
allowlist["torchvision.transforms.ColorJitter"] = "torchvision.transforms.ColorJitter"
allowlist["torchvision.transforms.FiveCrop"] = "torchvision.transforms.FiveCrop"
allowlist["torchvision.transforms.Grayscale"] = "torchvision.transforms.Grayscale"
allowlist["torchvision.transforms.Pad"] = "torchvision.transforms.Pad"
allowlist["torchvision.transforms.RandomAffine"] = "torchvision.transforms.RandomAffine"
allowlist["torchvision.transforms.RandomApply"] = "torchvision.transforms.RandomApply"
allowlist["torchvision.transforms.RandomCrop"] = "torchvision.transforms.RandomCrop"
allowlist[
    "torchvision.transforms.RandomGrayscale"
] = "torchvision.transforms.RandomGrayscale"

allowlist[
    "torchvision.transforms.RandomHorizontalFlip"
] = "torchvision.transforms.RandomHorizontalFlip"
allowlist[
    "torchvision.transforms.RandomPerspective"
] = "torchvision.transforms.RandomPerspective"
allowlist[
    "torchvision.transforms.RandomResizedCrop"
] = "torchvision.transforms.RandomResizedCrop"
allowlist[
    "torchvision.transforms.RandomRotation"
] = "torchvision.transforms.RandomRotation"
allowlist[
    "torchvision.transforms.RandomSizedCrop"
] = "torchvision.transforms.RandomSizedCrop"
allowlist[
    "torchvision.transforms.RandomVerticalFlip"
] = "torchvision.transforms.RandomVerticalFlip"
allowlist["torchvision.transforms.Resize"] = "torchvision.transforms.Resize"
allowlist["torchvision.transforms.Scale"] = "torchvision.transforms.Scale"
allowlist["torchvision.transforms.TenCrop"] = "torchvision.transforms.TenCrop"
allowlist["torchvision.transforms.GaussianBlur"] = "torchvision.transforms.GaussianBlur"
allowlist["torchvision.transforms.RandomChoice"] = "torchvision.transforms.RandomChoice"
allowlist["torchvision.transforms.RandomOrder"] = "torchvision.transforms.RandomOrder"
allowlist[
    "torchvision.transforms.LinearTransformation"
] = "torchvision.transforms.LinearTransformation"
allowlist["torchvision.transforms.Normalize"] = "torchvision.transforms.Normalize"
allowlist[
    "torchvision.transforms.RandomErasing"
] = "torchvision.transforms.RandomErasing"
allowlist[
    "torchvision.transforms.ConvertImageDtype"
] = "torchvision.transforms.ConvertImageDtype"
allowlist["torchvision.transforms.ToPILImage"] = "torchvision.transforms.ToPILImage"
allowlist["torchvision.transforms.Lambda"] = "torchvision.transforms.Lambda"
