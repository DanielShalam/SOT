# SOT: The Self-Optimal-Transport Feature Transform

This repository provides the official PyTorch implementation and pretrained models for **SOT** (The **S**elf-**O**ptimal-**T**ransport), as described in the paper [The Self-Optimal-Transport Feature Transform](https://arxiv.org/abs/2204.03065).

![SOT](./sot_workflow.png?raw=true)

The Self-Optimal-Transport (SOT) feature transform is designed to upgrade the set of features of a data instance to facilitate downstream matching or grouping related tasks. 

The transformed set encodes a rich representation of high order relations between the instance features. Distances  between transformed features capture their **direct** original similarity and their **third party** 'agreement' regarding similarity to other features in the set. 

A particular min-cost-max-flow fractional matching problem, whose entropy regularized version can be approximated by an optimal transport (OT) optimization, results in our transductive transform which is efficient, differentiable, equivariant, parameterless and probabilistically interpretable.

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-cifar-fs-5)](https://paperswithcode.com/sota/few-shot-image-classification-on-cifar-fs-5?p=the-self-optimal-transport-feature-transform)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-cifar-fs-5-1)](https://paperswithcode.com/sota/few-shot-image-classification-on-cifar-fs-5-1?p=the-self-optimal-transport-feature-transform)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-cub-200-5-1)](https://paperswithcode.com/sota/few-shot-image-classification-on-cub-200-5-1?p=the-self-optimal-transport-feature-transform)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-cub-200-5)](https://paperswithcode.com/sota/few-shot-image-classification-on-cub-200-5?p=the-self-optimal-transport-feature-transform)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-mini-2)](https://paperswithcode.com/sota/few-shot-image-classification-on-mini-2?p=the-self-optimal-transport-feature-transform)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/the-self-optimal-transport-feature-transform/few-shot-image-classification-on-mini-3)](https://paperswithcode.com/sota/few-shot-image-classification-on-mini-3?p=the-self-optimal-transport-feature-transform)

## Few-Shot Classification Results

| Dataset       | Method                 | 5-Way 1-Shot  | 5-Way 5-Shot  |
| ------------- |-------------           | ------------- | ------------- |
| MiniImagenet  | PTMAP-SOT<sub>p</sub>  | 83.19         | 89.56         |
|    | PTMAP-SOT<sub>t</sub>  | 84.18         | 90.51         |
|    | PTMAP-SF-SOT           | 85.59         | 91.34         |
|   |            |   |   |
| CIFAR-FS      | PTMAP-SOT<sub>p</sub>  | 87.37         | 91.12         |
|        | PTMAP-SF-SOT           | 89.94         | 92.83         |
|   |            |   |   |
| CUB           | PTMAP-SOT<sub>p</sub>  | 91.90         | 94.63         |
|            | PTMAP-SF-SOT           | 95.80         | 97.12         |

## Running instructions
We provide the code for training and evaluating PT-MAP and ProtoNet with and without SOT.
Note that the results from the paper are not reproducible here. 
To fully reproduce the results, use the SOT as shown here, in the original repositories.

### Training
You can choose between ProtoNet/PT-MAP and their SOT variations.

To train ProtoNet with SOT on miniimagenet, run:

```
python train.py --data_path <./datasets/miniimagenet/> --backbone WRN --method proto_sot --ot_reg 0.1 --max_epochs 200 --train_way 5 --scheduler step --step_size 40 --lr 0.0002  --augment false
```

You can also fine-tune a network by specify:
```
--backbone <model name> --pretrained_path <./path>
```

We use wandb to log the training by adding:
```
--wandb true --project <project_name> --entity <wandb_entity>
```

### Evaluation
Run the same you used for training with:
```
--eval --pretrained_path <./path>
```
You can choose the number of episodes by modify
```
--test_episodes
```


## Citation

<p>

#### If you find this repository useful in your research, please cite:

    @article{shalam2022self,
      title={The Self-Optimal-Transport Feature Transform},
      author={Shalam, Daniel and Korman, Simon},
      journal={arXiv preprint arXiv:2204.03065},
      year={2022}
    }

</p>

## Acknowledgment
[Leveraging the Feature Distribution in Transfer-based Few-Shot Learning](https://github.com/yhu01/PT-MAP)

[S2M2 Charting the Right Manifold: Manifold Mixup for Few-shot Learning](https://arxiv.org/pdf/1907.12087.pdf)

[Few-Shot Learning via Embedding Adaptation with Set-to-Set Functions](https://arxiv.org/pdf/1812.03664.pdf)
