# 知识图谱

构建上市公司知识图谱

## Python 版本

### 组件依赖

- Neo4J数据库

### 配置文件

- config/settings.toml

### 安装依赖库

```bash
pip install -r requirements.txt
```

#### NLP及中文分词库

- [pkuseg](https://github.com/lancopku/PKUSeg-python)
  - 功能
    - 分词
  - [分词模型](https://github.com/lancopku/pkuseg-python/releases)下载保存的默认路径是 ~/.pkuseg/
    - 新闻领域分词模型
    - 网络领域分词模型
    - 医药领域分词模型
    - 旅游领域分词模型
    - 混合领域分词模型
    - MSRA分词模型
    - CTB8分词模型
    - WEIBO分词模型
    - 词性标注模型
  - [词性标签的详细含义](https://github.com/lancopku/pkuseg-python/blob/master/tags.txt)
- [pyhanlp](https://github.com/hankcs/pyhanlp)
  - 功能
    - 分词
    - NER
  - 分词算法
    - CRF
    - NSHORT
  - [词性标签的详细含义](http://www.hankcs.com/nlp/part-of-speech-tagging.html#h2-8)
  - [自定义词典](https://github.com/hankcs/HanLP#%E5%9F%BA%E6%9C%AC%E6%A0%BC%E5%BC%8F)
  - 说明
    - 命名实体识别 还可以
    - 实体关系抽取 不准确
- [Jiagu](https://github.com/ownthink/Jiagu)
- [结巴中文分词](https://github.com/fxsjy/jieba)
- [THULAC](https://github.com/thunlp/THULAC-Python)一个高效的中文词法分析工具包
- [Stanford CoreNLP](https://github.com/Lynten/stanford-corenlp)

### 运行

```bash
python src/app.py
```

### 注意事项

#### 基于Mac开发遇到的问题

- 无法安装pyhanlp

    使用**`virtualenv`**，通过**`pip`**安装**`pyhanlp`**；由于**`jpype1`**依赖库无法安装导致失败；
    后来使用**`conda`**的虚拟环境，解决如下：

    ```bash
    conda install -n <env> -c conda-forge jpype1
    ```