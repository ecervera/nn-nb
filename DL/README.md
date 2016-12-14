Create a conda environment

    conda create --name dl27 --clone py27
    source activate dl27
    
Install Theano

    pip install Theano
    conda install pydot-ng
    
Install keras

    pip install keras
    
Configure Theano backend in file .keras/keras.json

    {
        "image_dim_ordering": "tf", 
        "epsilon": 1e-07, 
        "floatx": "float32", 
        "backend": "theano"
    }
