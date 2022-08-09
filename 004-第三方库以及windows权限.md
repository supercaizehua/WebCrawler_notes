1. 使用国内源加速 pip 安装第三方库

    ```shell
    # 国外
    pip install 第三方库名称
    
    # 豆瓣源
    pip install -i https://pypi.doubanio.com/simple/ 第三方库名称
    ```



**PS: 如果前面使用了 conda, 就不是按 pip 来安装了, 需要先进入对应的虚拟环境, 然后使用 conda install 来安装对应的库**![image-20220809204016948](assets/image-20220809204016948.png)







2. windows权限问题解决方法

    1. 使用管理员身份开启terminal

    2. ```shell
        pip install --user 第三方库名称
        ```

        
