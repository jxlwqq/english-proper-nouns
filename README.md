# English Proper nouns

#### 来源

[Wiktionary](https://en.wiktionary.org/w/index.php?title=Category:English_proper_nouns)

Wiktionary 声明收录了 61,765 条英语专用名词，实际爬取量为 61,711 条，具体原因为止，应该是 Wiktionary 志愿者的统计错误。

#### 数据

数据位于 `./data` 目录，有 SQL 和 CSV 两个格式。

#### 脚本

脚本位于 `./script` 目录，依赖详见 `requirements.txt` 文件，按以下命令执行即可：

```bash
cd ./script
python wiktionary.py
```
若要对数据进行存储或处理，请在脚本文件 `wiktionary.py` 第 `18` 行处：
```python
# Processing data here
```
进行修改。