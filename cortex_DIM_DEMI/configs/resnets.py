"""Configurations for ResNets

resblock layers take a list of layers. repeat is the number of repititions (2 = twice).
final_act is the activation after combining the residual.
See convnets.py for more details.

"""

from cortex_DIM_DEMI.nn_modules.resnet import ResNet, FoldedResNet


_resnet19_32x32 = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(64, 3, 2, 1), bn=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=2),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='flatten'),
        dict(layer='linear', args=(1024,), bn=True, act='ReLU')
    ],
    local_task_idx=(2, -1),
    classifier_idx=dict(local=2, conv=5, fc=7, glob=-1)
)

_foldresnet19_32x32 = dict(
    Module=FoldedResNet,
    crop_size=8,
    layers=[
        dict(layer='unfold'),
        dict(layer='conv', args=(64, 3, 2, 1), bn=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=2),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='fold'),
        dict(layer='flatten'),
        dict(layer='linear', args=(1024,), bn=True, act='ReLU')
    ],
    local_task_idx=(7, -1),
    classifier_idx=dict(conv=7, fc=9, glob=-1)
)

_resnet37_32x32 = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(64, 3, 2, 1), bn=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=3),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=5),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=2),
        dict(layer='flatten'),
        dict(layer='linear', args=(1024,), bn=True, act='ReLU')
    ],
    local_task_idx=(2, -1),
    classifier_idx=dict(local=2, conv=5, fc=7, glob=-1)
)

# This network was used in the CIFAR10 CPC comparison results.
_foldresnet37_32x32 = dict(
    Module=FoldedResNet,
    crop_size=8,
    layers=[
        dict(layer='unfold'),
        dict(layer='conv', args=(64, 3, 2, 1), bn=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=2),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=0),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=5),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 2, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=0),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(256, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256, 3, 1, 1), bn=True, act='ReLU'),
                     dict(layer='conv', args=(256 * 4, 1, 1, 0), bn=True)],
             final_act='ReLU',
             repeat=2),
        dict(layer='fold'),
        dict(layer='flatten'),
        dict(layer='linear', args=(1024,), bn=True, act='ReLU')
    ],
    local_task_idx=(7, -1),
    classifier_idx=dict(conv=7, fc=9, glob=-1)
)

# Phil's networks

_philish_resnet_32x32 = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(32, 3, 1, 0), bias=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(64, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 2, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 2, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='flatten')],
    local_task_idx=(4, -1),
    classifier_idx=dict(conv=6, glob=-1)
)


_philish_resnet_32x32_wide = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(256, 3, 1, 0), bias=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='flatten', ln=True)],
    local_task_idx=(4, -1),
    classifier_idx=dict(conv=6, glob=-1)
)


_philish_resnet_32x32_mega = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(256, 3, 1, 0), bias=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='flatten')],
    local_task_idx=(4, -1),
    classifier_idx=dict(conv=6, glob=-1)
)


_philish_resnet_64x64 = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(32, 3, 1, 0), bias=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(64, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(128, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(128, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 2, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 2, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(64, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(64, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='flatten', ln=True)],
    local_task_idx=(6, -1),
    classifier_idx=dict(conv=8, glob=-1)
)


_philish_resnet_64x64_wide = dict(
    Module=ResNet,
    layers=[
        dict(layer='conv', args=(256, 3, 1, 0), bias=True, act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(512, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(512, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 4, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 4, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 2, 2, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='resblock',
             layers=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU'),
                     dict(layer='conv', args=(1024, 1, 1, 0), bn=True, act='ReLU')],
             downsample=[dict(layer='conv', args=(1024, 3, 1, 0), bn=True, act='ReLU')],
             final_act='ReLU'),
        dict(layer='flatten', ln=True)],
    local_task_idx=(6, -1),
    classifier_idx=dict(conv=8, glob=-1)
)


configs = dict(
    resnet19_32x32=_resnet19_32x32,
    resnet34_32x32=_resnet37_32x32,
    foldresnet19_32x32=_foldresnet19_32x32,
    foldresnet34_32x32=_foldresnet37_32x32,
    philish_resnet_64x64=_philish_resnet_64x64,
    philish_resnet_64x64_wide=_philish_resnet_64x64_wide,
    philish_resnet_32x32=_philish_resnet_32x32,
    philish_resnet_32x32_wide=_philish_resnet_32x32_wide
)