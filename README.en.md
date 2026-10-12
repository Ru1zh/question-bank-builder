[中文（默认）](https://github.com/Ru1zh/question-bank-builder/blob/main/README.md) · [English](https://github.com/Ru1zh/question-bank-builder/blob/main/README.en.md)

# question-bank-builder

Create and revise source-grounded course banks for **Lecture2Exam** from PDF, PowerPoint, Word, Markdown, Jupyter and text materials. Supports single-choice, multiple-choice and true/false questions. Codex uses the skill to author questions; the companion local app runs practice/exams and stores learning records without a model API.

Use with [Lecture2Exam](https://github.com/Ru1zh/Lecture2Exam/blob/main/README.en.md): generate a bank in Codex, then open it in the app for practice and exams.

## Use

Place this folder in your skills directory or supply its `SKILL.md` path in Codex. Before generating a bank, specify course materials, bank name, coverage, question counts, question-type split, question/explanation languages and destination folder, such as `~/Documents/Lecture2Exam-banks/course-bank/`.

The generated bank contains reusable questions, answers, explanations and source locators. When you want an exam, choose its scope, types, sampled counts, points and duration in Lecture2Exam, then generate the paper.

Create an empty bank in the app and populate it with the skill, or generate a bank first and open its folder or import its JSON package. Updating an existing bank preserves learning records. Exported bank packages exclude personal records and original materials.

Multiple-choice questions require all correct options to be selected. Missing, extra or wrong selections earn no points.

## Optional: command-line validation and export

```sh
python3 scripts/bank_tool.py --app /path/to/Lecture2Exam validate /path/to/bank
python3 scripts/bank_tool.py --app /path/to/Lecture2Exam export /path/to/bank --output /path/to/course-bank.json
```

Use `--app` to specify the Lecture2Exam installation, or set `LECTURE2EXAM_HOME`. You can omit this argument when the app is in a nearby `Lecture2Exam` folder.

More details: [SKILL.md](https://github.com/Ru1zh/question-bank-builder/blob/main/SKILL.md) · [Bank data format](https://github.com/Ru1zh/question-bank-builder/blob/main/references/bank-format.md).

[MIT License](https://github.com/Ru1zh/question-bank-builder/blob/main/LICENSE).
