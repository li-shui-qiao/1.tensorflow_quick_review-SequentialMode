# Sequential Mode
库函数导入:
```
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Flatten 
```
* 我们需要用到tensorflow的[Sequential](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)模型和[layers](https://www.tensorflow.org/api_docs/python/tf/keras/layers)里的Dense和Flatten  
* 更多详细介绍和功能可进入官网查看： https://www.tensorflow.org

## 创建顺序模型  
首先确定好每层神经元数量和神经层数Dense的第一个参数为神经元个数：
* 第一种创建model方法：
```
'''
one way to create model
'''
model1 = Sequential([
    Dense(255, activation='relu', input_shape=(4096,)),
    Dense(64, activation='relu'),
    Dense(2,activation='softmax')
])
```
* 第二种创建model方法：
```
'''
another way to create model
'''
model2 = Sequential()
model2.add(Dense(255, activation='relu',input_shape=(4096,)))
model2.add(Dense(64, activation='relu'))
model2.add(Dense(2, activation='softmax'))
```
* 以上两种方法都创建了一个三层神经元模型，第一层有255个神经元单位，第二层有64，  
最后有一个两个神经元的输出层，把输入数据区输出类似“是”或“否”两种情况
* 注意input_shape已经是最好的数据，如果我们使用一组未处理数据需要使用[Flatten](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten)函数展开：
```
'''
to flatten the image
'''
Flatten(input_shape=(64,64))
```
