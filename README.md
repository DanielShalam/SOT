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

## Few-shot classification results

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
### Clustering on the sphere
We provide the code to reproduce the synthetic experiment as described in the paper.
This can be beneficial to experiment with the SOT on controlled data and can be used as a benchmark.
    
To run the experiment with the default arguments, simply run the script:

        synthetic_exp/eval_unit.py
        
The script includes a variety of parameters that control the structure of the data as well as additional plot configurations.

### Few-Shot Classification

<details><summary>Dataset </summary>
<p>
    
Work in progress...
    
</p>
</details>

<details><summary>Running PT-MAP-SOT<sub>p</sub> </summary>
<p>

Work in progress...

</p>
</details>

<details><summary>Running PT-MAP-SOT<sub>t</sub> </summary>
<p>
    
Work in progress...

</p>
</details>

<details><summary>Pretrained Models </summary>
<p>

All pretrained weights and features for the PT-MAP-SOT<sub>p</sub> expriment can be downloaded from the [PT-MAP repository](https://github.com/yhu01/PT-MAP)

</p>
</details>

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
