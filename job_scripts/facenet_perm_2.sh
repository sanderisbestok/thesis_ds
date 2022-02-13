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

python src/train_softmax.py \
--logs_base_dir ~/facenet_run/logs/facenet/ \
--models_base_dir ~/facenet_run/models/facenet/ \
--data_dir $TMPDIR/sander/facenet_run/datasets/train_perm_2/ \
--image_size 160 \
--model_def models.inception_resnet_v1 \
--optimizer ADAM \
--learning_rate -1 \
--epoch_size 50 \
--max_nrof_epochs 10000 \
--keep_probability 0.8 \
--random_crop \
--random_flip \
--use_fixed_image_standardization \
--learning_rate_schedule_file data/learning_rate_schedule_classifier_casia.txt \
--weight_decay 5e-4 \
--embedding_size 512 \
--lfw_dir $TMPDIR/sander/facenet_run/datasets/val_perm_2/ \
--lfw_pairs ~/datasets/pairs/perm_2_val.txt \
--lfw_distance_metric 1 \
--lfw_subtract_mean \
--validate_every_n_epochs 11000 \
--prelogits_norm_loss_factor 5e-4 \
--gpu_memory_fraction 0.9 \
