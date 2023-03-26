# Chat-with-Elysia2.0

## base on chatGLM-6B and vits

### 本项目开源，严禁商用

- 本项目基于清华大学开源模型chatGLM-6B以及vits框架

  - chatGLM-6B模型为清华大学开源，使用时请注意查看对应的使用需知，严格遵守使用规定

    - 模型下载链接 [点击这里](https://huggingface.co/THUDM) 请仔细阅读说明根据自己的硬件配置下载对应模型
    - 模型下载后请将模型及响应的文件放置在./chatglm-model路径下

  - vits模型下载地址：[点击这里](https://pan.quark.cn/s/d6bc5d8829a6) 提取码：tyM6

    - 下载后请将模型以及配置文件放在./model-vits路径下

      本模型来自up主“saya睡大觉中”，严禁商用

- 自行部署项目时，使用下面命令以安装模块，注意：pip安装的torch可能为cpu版本，请按照torch官网的安装方式安装对应的cuda版本，如果出现模块兼容性问题，请使用python3.9.6

 ```shell
  pip install -r requirements.txt
 ```

- 硬件需求
  - 大于等于16GB内存
  - 可选：英伟达显存6GB以上显卡，最好显存8GB以上显卡
  - 注：使用cpu进行部署时需要32位gcc编译器，部署细节与方法具体问题请自行查阅清华大学ChatGLM项目对应的issue以及网上搜索

- 本项目开发时使用的是python嵌入式包开发，所以方便打包成“懒人包”，懒人包下载地址：

​		[点击这里](https://pan.quark.cn/s/bbd0b4b13902) 提取码：8iRw，解压后便可以直接使用

