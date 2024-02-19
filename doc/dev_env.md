# Dev Env

开发环境极简配置

```shell
# 安装git
yum install git

# 查看服务器
uname -a

# 配置VIM
echo "set number" >> ~/.vimrc \
    && echo "syntax on" >> ~/.vimrc \
    && echo "set showmode" >> ~/.vimrc \
    && echo "set encoding=utf-8" >> ~/.vimrc \
    && echo "set cursorline" >> ~/.vimrc \
    && echo "set ruler" >> ~/.vimrc \
    && echo "set hlsearch" >> ~/.vimrc \
    && echo "set visualbell" >> ~/.vimrc

# 安装对应版本的miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh

sh Miniconda3-latest-Linux-x86_64.sh

# 创建虚拟环境
conda create --name conda310 python=3.10

conda activate conda310
conda deactivate

# 配置开发环境
pip install pipreqs
pipreqs ./ --force

pip install -r requirements.txt
```