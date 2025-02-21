# Experiments
## Cow Fleisch

### Experiment I

**GPU**: NVIDIA T1200 4GB 

**Model**: EfficientAD-S 
* teacher_out_channels: 384 
* model_size: S 
* lr: 0.0001 
* weight_decay: 1.0e-05 
* padding: false 
* pad_maps: true
* train_batch_size: 1 (as per paper)
* eval_batch_size: 1
* normalization_method: MinMax
* threshold: F1AdaptiveThreshold

#### Sample 0

* Animal_type: cow
* Class-wise arrangement in training set
* Exclusions:
  * unique directories
  * non-exclusive directories (pink tag)
  * empty box directory (blue tag)
* 36 classes: 100 images per class in **training set**: Total 3318
* 32 classes: 50 images per class in **test/normal set**
* 70 images in **test/anomaly set**
* Total test images: 964
* **validation set**: 0.4 random split ratio from test set
* 50 epochs
* **Metrics**: 
  * ImageAUROC
  * F1Score
* Early stopping, patience: 15, monitor: imageAUROC

#### Results
* Training stopped at epoch 46.
* Training took 41041.94 seconds
* Testing took 397.59 seconds
* Throughput (batch_size=1): 2.4245 FPS
* Tensorboard logs: tb_logs/EffAD-S_expI/version_0
* **Test metrics**:
  * image_AUROC: 0.9717
  * image_F1Score: 0.8547

#### Sample 1 (not considered)

* Animal_type: cow
* Mixed arrangement in training set
* Exclusions:
  * unique directories
  * non-exclusive directories (pink tag)
  * empty box directory (blue tag)
* 36 classes: <=100 images per class in **training set**: Total 3318
* 32 classes: <=50 images per class in **test/normal set**: Total 984 
* 70 images in **test/anomaly set**
* **validation set**: 0.4 random split ratio from test set
* 60 epochs
* **Metrics**: 
  * ImageAUROC
  * F1Score
* Early stopping, patience: 20, monitor: imageAUROC

#### Results
* Training stopped at epoch 27.
* Training took 24217.18 seconds
* Testing took 397.65 seconds
* Throughput (batch_size=1): 2.4242 FPS
* Tensorboard logs: tb_logs/EffAD-S_expI/version_1
* **Test metrics**:
  * image_AUROC: 0.9539
  * image_F1Score: 0.7722

#### Sample 2

eval_batch_size=16 in this experiment.
* Animal_type: cow
* Mixed arrangement in training and test set 
* Exclusions:
  * unique directories
  * non-exclusive directories (pink tag)
  * empty box directory (blue tag)
* 36 classes: <=100 images per class in **training set**: Total 3318
* 32 classes: <=50 images per class in **test/normal set**: Total 984 
* 70 images in **test/anomaly set**
* **validation set**: 0.4 random split ratio from test set
* 60 epochs
* **Metrics**: 
  * ImageAUROC
  * F1Score
* Early stopping, patience: 20, monitor: F1Score

#### Results
* Training stopped at epoch 20.
* Training took -- seconds # lost data due to system crash
* Testing took -- seconds 
* Throughput (batch_size=1): -- 
* Tensorboard logs: tb_logs/EffAD-S_expI/version_2
* **Test metrics**:
  * image_AUROC: 0.97
  * image_F1Score: 0.82


#### Sample 3

* Animal_type: cow
* Mixed arrangement in training and test set 
* Exclusions:
  * unique directories
  * non-exclusive directories (pink tag)
  * empty box directory (blue tag)
* 36 classes: <=100 images per class in **training set**: Total 3318
* 32 classes: <=50 images per class in **test/normal set**: Total 984 
* 100 images in **test/anomaly set**
* **validation set**: 0.4 random split ratio from test set
* 50 epochs
* **Metrics**: 
  * ImageAUROC
  * F1Score
* Early stopping, patience: 15, monitor: ImageAUROC

#### Results
* Training stopped at epoch 46.
* Training took 41086.31 seconds
* Testing took 395.55 seconds 
* Throughput (batch_size=1): 2.4370 FPS
* Tensorboard logs: tb_logs/EffAD-S_expI/version_3
* **Test metrics**:
  * image_AUROC: 0.9778
  * image_F1Score: 0.8062


#### Sample 4

* Animal_type: cow
* Mixed arrangement in training and test set (Random split)
* Exclusions:
  * unique dirs
  * non-exclusive classes (pink tag)
  * empty box directory (blue tag)
  * classes with 1 image.
* 34 classes
  * **training set**: 4100
  * **test/normal set**: 1775
  * **test/anomaly set**: 90
  * **validation set**: 0.4 random split ratio from test set
  
* 50 epochs
* **Metrics**: 
  * ImageAUROC
  * F1Score
* Early stopping, patience: 15, monitor: ImageAUROC

#### Results
* Training stopped at epoch 45.
* Training took 48899.97 seconds
* Testing took 454.12 seconds 
* Throughput (batch_size=1): 2-464 FPS
* Tensorboard logs: tb_logs/EffAD-S_expI/version_4
* **Test metrics**:
  * image_AUROC: 0.9571
  * image_F1Score: 0.7787


#### Sample 5

* Animal_type: cow
* Mixed arrangement in training, test and validation set (Random split)
* Exclusions:
  * unique dirs
  * non-exclusive classes (pink tag)
  * empty box directory (blue tag)
  * classes with 1 image.
* 34 classes, 10 anomaly types
  * **training set**: 4100
  * **val/normal set**: 801
  * **val/anomaly set**: 98
  * **test/normal set**: 2749
  * **test/anomaly set**: 64 (including todo)
  
* 50 epochs
* **Validation Metrics**: 
  * ImageAUROC
  * F1Score
  * F1Max
* **Test Metrics**: 
  * ImageAUROC
  * F1Score
  * AUPR
  * Precision
  * Recall
* Early stopping, patience: 15, monitor: ImageAUROC, min_delta: 1e-4
* Model checkpoint: monitor: image_AUROC

#### Results
* Training stopped at epoch .
* Training took  seconds
* Testing took seconds 
* Throughput (batch_size=1):  FPS
* Tensorboard logs: tb_logs/EffAD-S_expI/version_5
* **Test metrics**:
  * image_AUROC: 
  * image_F1Score: 
  * image_AUPR:
  * image_Precision: 
  * image_Recall:

epoch 34: 13 fn among 54
epoch 25: 9 fn among 54