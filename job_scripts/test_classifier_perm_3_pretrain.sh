#!/bin/bash
#SBATCH -t 00:15:00

#SBATCH -p gpu_shared
#SBATCH -N 1
#SBATCH --gpus=1

module load 2019
module load 2021
module load Anaconda3/2021.05 

module load CUDA/10.0.130
module load cuDNN/7.4.2-CUDA-10.0.130

source activate facenet_4

export PYTHONPATH=/home/hansen/facenet/src/

cd ~/facenet/

python src/validate_on_lfw.py \
~/datasets/perm_3/test \
~/facenet_run/models/facenet/perm_3_classifier_pretrain \
--lfw_pairs ~/datasets/pairs/perm_3_test.txt \
--distance_metric 1 \
--subtract_mean \
--use_fixed_image_standardization \
--image_name perm_3_classifier_pretrain
