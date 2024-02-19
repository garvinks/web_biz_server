# Dev Env

开发环境极简配置

```shell
# 安装git
yum install git

# 查看服务器
uname -a

# 安装对应版本的miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh

sh Miniconda3-latest-Linux-x86_64.sh

# 创建虚拟环境
conda create --name conda310 python=3.10


```