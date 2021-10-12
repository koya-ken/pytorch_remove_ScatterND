import torch
from catmodel import CatModel
from scatterndmodel import ScatterNdModel

cat_model = CatModel()
cat_model = cat_model.eval()
verbose = False
batch_size = 3

dummy_input = torch.ones(batch_size,3,1)
torch.onnx.export(cat_model, dummy_input, "cat_model.onnx", opset_version=11, verbose=verbose)

scatternd_model = ScatterNdModel()
scatternd_model = scatternd_model.eval()
torch.onnx.export(scatternd_model, dummy_input, "scatternd_model.onnx", opset_version=11, verbose=verbose)

cat_model_output = cat_model(dummy_input)
scatternd_model_output = scatternd_model(dummy_input)

print("cat_model_output:",cat_model_output.shape)
print(cat_model_output.flatten())
print("scatternd_model_output:",scatternd_model_output.shape)
print(scatternd_model_output.flatten())
