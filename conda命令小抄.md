```shell
# 查看当前有哪些虚拟环境
conda env list
conda info -e

# 更新当前conda
conda update conda

# 更新所有包
conda update --all

# 创建虚拟环境
conda create -n [name] python=X.X
conda create -n test python=3.8        
创建名字为test的虚拟环境, python版本为3.8, 一般虚拟环境默认存储在 .../anaconda/envs/

# 激活/关闭虚拟环境
conda activate [name]
conda deactivate

# 安装 package 到虚拟环境[name]中
conda install -n [name] [package]

# 退出环境[name]后, 删除环境[name]
conda remove -n [name] --all

# 删除环境[name]中某个 package
conda remove -n [name] [package]

# 重置环境
# 查看历史环境
conda list --revisions

conda install --revision REV_NUM
```

