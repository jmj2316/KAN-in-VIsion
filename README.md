# KAN in Vision
This repository contains the code used for 

'Demonstrating the Efficacy of Kolmogorov-Arnold Networks in Vision Tasks'

In deep learning, the Kolmogorov-Arnold Network (KAN) has emerged as a potential alternative to multilayer projections (MLPs). However, its applicability to vision tasks has not been extensively validated. In our study, we demonstrated the effectiveness of KAN for vision tasks through multiple trials on the MNIST, CIFAR10, and CIFAR100 datasets, using a training batch size of 32. Our results showed that while KAN outperformed the original MLP-Mixer on CIFAR10 and CIFAR100, it performed slightly worse than the state-of-the-art ResNet-18. These findings suggest that KAN holds significant promise for vision tasks, and further modifications could enhance its performance in future evaluations.Our contributions are threefold: first, we showcase the efficiency of KAN-based algorithms for visual tasks; second, we provide extensive empirical assessments across various vision benchmarks, comparing KAN's performance with MLP-Mixer, CNNs, and Vision Transformers (ViT); and third, we pioneer the use of natural KAN layers in visual tasks, addressing a gap in previous research. This paper lays the foundation for future studies on KANs, highlighting their potential as a reliable alternative for image classification tasks.
[Read more about paper here.](https://arxiv.org/abs/2406.14916)

### Model Performance Comparison

| Model         | GPU Usage (gb) | MNIST   | CIFAR10 | CIFAR100 |
|---------------|----------------|---------|---------|----------|
| KKAN (Small)  | 1.8119         | 98.90%  | -       | -        |
| Conv & KAN    | -              | 98.75%  | -       | -        |
| MLP Mixer-5   | 1.5            | -       | 60.26%  | 34.81%   |
| ViT-10/4      | 14.7           | -       | 57.53%  | 30.80%   |
| ResNet-18     | 0.6            | -       | 86.29%  | 59.15%   |
| Ours          | -              | 98.16%  | 66.93%  | 35.49%   |

## Acknowledgments
I express my deepest gratitude to Donggyu Hyeon for inspiring us with the idea of the Kolmogorov Arnold network. His insights have significantly contributed to the advancement of our project.

## Citation
```bibtex
@article{cheon2024demonstratingefficacykolmogorovarnoldnetworks,
      title={Demonstrating the Efficacy of Kolmogorov-Arnold Networks in Vision Tasks}, 
      author={Minjong Cheon},
      year={2024},
      eprint={2406.14916},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2406.14916}, 
}
```
