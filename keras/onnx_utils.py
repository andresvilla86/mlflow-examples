
def log_model(model, artifact_path):
    import mlflow
    import mlflow.onnx
    import onnx
    import onnxmltools
    onnx_model = onnxmltools.convert_keras(model, artifact_path)
    print("onnx_model.type:",type(onnx_model))
    mlflow.onnx.log_model(onnx_model, artifact_path)
    mlflow.set_tag("onnx_version",onnx.__version__)

def score_model(model, data):
    import numpy as np
    import onnxruntime 
    sess = onnxruntime.InferenceSession(model.SerializeToString())
    input_name = sess.get_inputs()[0].name
    input_names = [iname for iname in sess.get_inputs() ]
    return sess.run(None, {input_name: data.astype(np.float32)})[0]
