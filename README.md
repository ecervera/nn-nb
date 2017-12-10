[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ecervera/nn-nb/master?filepath=index.ipynb)
# Neural Networks Notebooks

Examples and exercises with [scikit-learn](http://scikit-learn.org/stable/) and [keras](https://keras.io).

* Linear Perceptron
* Multilayer Perceptron
* Deep Learning

## Prerequisites

* Python 2.7.x
* [scikit-learn](http://scikit-learn.org/stable/install.html#installing-the-latest-release)
* [Jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html)

### Basic Installation

We recommend using Miniconda and creating an environment:

* [Conda quick install](http://conda.pydata.org/docs/install/quick.html)
* `conda create --name py27 python=2.7`
* `source activate py27`
* `conda install scikit-learn`
* `conda install jupyter`
* `conda install matplotlib pil`

### Packages for Deep Learning

* `conda install -c conda-forge tensorflow=0.11.0`
* `conda install -c conda-forge keras=1.0.7`

#### Switching from Theano to Tensorflow 

The Keras package will automatically install and use Theano 0.8.2 as its tensor manipulation library. Follow [these instructions](https://keras.io/backend/) to configure the Keras backend.

## Usage

Download, run `jupyter notebook index.ipynb` in the root folder, and enjoy!
