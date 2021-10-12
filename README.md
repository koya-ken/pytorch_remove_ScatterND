# pytorch_remove_ScatterND

pytorchのスライス代入操作をonnxに変換する際にScatterNDならないようにするサンプル。  
スライスしたtensorにそのまま代入してしまうとScatterNDになるため、計算結果をcatで新しいtensorにする。

# python version

Python 3.8.11

# setup

```
pip install -r requirements.txt
```

# usage

```
python convertonnx.py
```

scatternd_model.onnxとcat_model.onnxが作成されるのでNetronなどで確認。  

# src

## scatterndmodel.py

ScatterNDになるような演算を含むモデル  

## catmodel.py

ScatterNDを使わずscatterndmodelと同じ結果になるようにしたモデル  

# Netron

## ScatterNdModel
![scatternd model](images/scatternd.png)  

## CatModel
![cat model](images/catmodel.png)  