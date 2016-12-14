### Mac instructions

Create a conda environment

    conda create --name dl27 --clone py27
    source activate dl27
    
Install Theano

    pip install Theano
    conda install pydot-ng
    
Install TensorFlow

    conda install -c conda-forge tensorflow
    pip install --upgrade protobuf=3.0.0b2
    
Install keras

    pip install keras
    
Configure backend in file `.keras/keras.json`

Simply change the field `backend` to either `"theano"` or `"tensorflow"`, 
and Keras will use the new configuration next time you run any Keras code.

    {
        "image_dim_ordering": "tf", 
        "epsilon": 1e-07, 
        "floatx": "float32", 
        "backend": "theano"
    }

TODO: configure GPU