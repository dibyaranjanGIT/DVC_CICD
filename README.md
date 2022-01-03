# Commands Used

```buildoutcfg
conda create -n env_name python=3.7
```

```buildoutcfg
pip install dvc
```

```buildoutcfg
git init
```

```buildoutcfg
dvc init
```

```buildoutcfg
dvc repro
```

### To see the dependency in file
```buildoutcfg
dvc dag
```

### To install the requirements
```buildoutcfg
pip install -r requirements.txt
```

### Create a setup file
```python
from setuptools import setup

with open("README.md","r", encoding="UTF-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="dibyaranjanGIT",
    description="A small description",
    long_description=long_description,
    url="https://github.com/dibyaranjanGIT/DVC_CICD",
    packages=["src"],
    python_requires=">3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
```

### Create a config file
```yaml
data_source: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

artifacts:
  artifcats_dir: artifacts
  raw_local_dir: local_dir
  raw_local_file: data.csv

```