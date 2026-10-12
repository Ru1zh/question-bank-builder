[中文](https://github.com/Ru1zh/question-bank-builder/blob/main/README.md) · [English](https://github.com/Ru1zh/question-bank-builder/blob/main/README.en.md)

# question-bank-builder

为 **Lecture2Exam** 准备和更新有材料依据的课程题库。支持 PDF、PPT/PPTX、Word、Markdown、Jupyter 与文本材料，以及单选、多选、判断题。由 Codex 使用 skill 出题；配套应用在本地运行练习、考试和做题记录。

搭配 [Lecture2Exam](https://github.com/Ru1zh/Lecture2Exam/blob/main/README.md) 使用：在 Codex 中生成题库，再到应用中练习和考试。

## 使用

将本文件夹放到自己的 skills 目录，或在 Codex 中提供 `SKILL.md` 路径。生成前，请指定课程材料、题库名称、覆盖范围、题量、题型比例、题目／解析语言和存放位置，例如 `~/Documents/Lecture2Exam-banks/课程题库/`。

生成的题库包含可复用的题目、答案、解析和来源。需要考试时，在 Lecture2Exam 中选择范围、题型、抽题数量、每题分值和时长，再生成试卷。

可以先在应用创建空题库，再让 skill 填充；也可以先由 skill 生成，再在应用打开题库文件夹或导入题库 JSON 包。更新已有题库会保留做题记录；导出的题库包不包含个人记录或原始材料。

多选题需要选择所有正确选项，漏选、多选或错选均不得分。

## 可选：命令行校验与导出

```sh
python3 scripts/bank_tool.py --app /path/to/Lecture2Exam validate /path/to/bank
python3 scripts/bank_tool.py --app /path/to/Lecture2Exam export /path/to/bank --output /path/to/course-bank.json
```

`--app` 指定 Lecture2Exam 的安装位置，也可使用 `LECTURE2EXAM_HOME`；如果应用位于附近的 `Lecture2Exam` 文件夹，可省略此参数。

详细说明：[SKILL.md](https://github.com/Ru1zh/question-bank-builder/blob/main/SKILL.md) · [题库数据格式](https://github.com/Ru1zh/question-bank-builder/blob/main/references/bank-format.md)。

[MIT License](https://github.com/Ru1zh/question-bank-builder/blob/main/LICENSE)。
