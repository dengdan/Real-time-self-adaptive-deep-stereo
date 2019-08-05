python Train.py \
  --trainingSet datasets/flyingthings3d_monkaa_scene_flow.csv\
  --imageShape 320 512\
  --validationSet datasets/Stereo2015.csv\
  --output /data/temp/models/MadNet\
  --lossWeights 1 1 1 1 1 1 1\
  --batchSize 1
