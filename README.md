
# Research on Quality Enhancement of Old Photos Based on Deep Learning

## 📖 项目概述

声明：本项目为本人于武汉大学印刷工程学士学位毕业设计的记录，部分模型代码并不完整，模型参数请于各个模型原文下载。

老旧照片作为历史和记忆的重要载体，具有不可替代的历史价值。然而，由于时间流逝、保存方式和环境等因素，老旧照片常会出现破损、分辨率降低、褪色等多种退化问题。因此，发展有效的老旧照片质量增强技术显得尤为重要。

本项目致力于研究基于深度学习的老旧照片质量增强算法，针对老旧照片存在的主要缺陷（如分辨率过低导致的画面模糊问题），系统性地探索和实现多种先进的图像超分辨率修复技术，旨在为历史照片的数字化保护提供有效的技术解决方案。

## 🎯 主要研究内容

### 1. 经典超分算法复现与研究
- **SRCNN (Super-Resolution Convolutional Neural Network)**: 复现基于深度学习的经典图像超分辨率算法 
- **SRGAN (Super-Resolution Generative Adversarial Network)**: 复现基于生成对抗网络的图像超分辨率算法 
- 在自行搭建的环境中对算法进行训练与测试，深入分析各算法的优缺点

### 2. 先进修复模型构建
- **GFPGAN (Generative Facial Prior Generative Adversarial Network)**: 构建基于生成面部先验的生成对抗网络图像超分算法
- 实现针对老旧照片的端到端修复模型，有效处理人脸区域的细节恢复

### 3. 综合对比实验
- 在合成数据集与真实老旧照片数据集上进行全面测试
- 与SRCNN、SRGAN等经典算法进行对比实验
- 采用客观评价指标（PSNR、SSIM）与主观评价指标（MOS）进行综合评估

## 🚀 技术特点

- **面部先验优化**: 利用GFPGAN的面部先验知识，特别优化人脸区域的修复效果
- **综合评价体系**: 结合主客观评价指标，全面评估算法性能
- **实用性强**: 专注于真实老旧照片的修复需求，具有实际应用价值

## 📊 性能指标

| 算法 | PSNR ↑ | SSIM ↑ | MOS ↑ |
|------|--------|--------|-------|
| SRCNN | 27.78 | 0.76 | 2.9 |
| SRGAN | 30.44 | 0.85 | 3.4 |
| GFPGAN | 32.26 | 0.86 | 3.8 |


## 📝 引用

如果您觉得本项目对您的研究有所帮助，请引用：

```bibtex
@misc{oldphotoDL2023,
  title={Research on Quality Enhancement of Old Photos Based on Deep Learning},
  author={HU Zhibo},
  year={2023},
  howpublished={\url{https://github.com/2009wusheng/Research-on-quality-enhancement-of-old-photos-based-on-deep-learning}}
}
```

## 📧 联系我们

如有任何问题或建议，请通过以下方式联系：
- 📮 Email: [24135698g@connect.polyu.hk]

**让记忆重现光彩，让历史永不褪色。** ✨
