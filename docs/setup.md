conda create -n ontoGen python=3.10 -y
conda activate ontoGen
pip install transformers datasets accelerate
pip install scikit-learn pandas
pip install tqdm
pip install sentencepiece

conda env export > environment.yml
conda env create -f environment.yml