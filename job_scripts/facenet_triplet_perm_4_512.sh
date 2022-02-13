#!/bin/bash
#SBATCH -t 12:00:00

#SBATCH -p gpu_shared
#SBATCH -N 1
#SBATCH --gpus=1

module load 2019
module load 2021
module load Anaconda3/2021.05

module load CUDA/10.0.130
module load cuDNN/7.4.2-CUDA-10.0.130

source activate facenet_4

mkdir $TMPDIR/sander
cp -r $HOME/facenet_run/ $TMPDIR/sander

export PYTHONPATH=/home/hansen/facenet/src/

cd ~/facenet/

python src/train_tripletloss.py \
--logs_base_dir ~/facenet_run/logs/facenet/ \
--models_base_dir ~/facenet_run/models/facenet/ \
--data_dir $TMPDIR/sander/facenet_run/datasets/train_perm_4/ \
--image_size 160 \
--model_def models.inception_resnet_v1 \
--optimizer ADAM \
--learning_rate 0.01 \
--weight_decay 1e-4 \
--lfw_dir $TMPDIR/sander/facenet_run/datasets/val_perm_4/ \
--lfw_pairs ~/datasets/pairs/perm_4_val.txt \
--gpu_memory_fraction 0.9 \
--max_nrof_epochs 10000 \
--epoch_size 10 \
--keep_probability 0.8 \
--embedding_size 512 \
--random_crop \
--random_flip \
