import numpy as np

data = np.loadtxt('./train_dir/myself/face_feature.txt')
print(data)
print(data.shape)
print(data.dtype)
data_mean = np.average(data,axis=0)
print(data_mean)
#np.savetxt('./train_dir/myself/face_feature_mean.txt',data_mean,'%10.5f')