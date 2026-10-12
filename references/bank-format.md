# Lecture2Exam bank format (schemaVersion 1)

The bank folder contains `bank.json`, `questions.json`, optional `sources/`, and app-managed `records/`. A portable import package is one JSON object with `bank` and `questions`; the files remain separate within a working bank. Share source documents separately when needed.

## Bank metadata and compatibility defaults

Bank authoring supplies metadata and a reusable question pool. Current schemaVersion 1 also requires `exam`; this is a compatibility block, not an instruction to derive a paper from bank counts. Preserve this block on updates. For a new bank, initialize the chosen destination through the app's `create` command, which supplies generic defaults. The example below shows those defaults; do not substitute a course's authored question counts, scores, duration, or source quotas.

The user configures the actual paper in Lecture2Exam. The app stores user settings and named presets in learning records, and snapshots a paper only when the user starts an exam.

```json
{
  "schemaVersion": 1,
  "id": "course-midterm",
  "name": "课程期中题库",
  "course": "COURSE101",
  "description": "按课程材料组织的可复用题目池",
  "groups": [{"id": "chapter-1", "label": "第一章"}],
  "sources": [{
    "id": "notes-1", "file": "chapter1.md", "kind": "md",
    "groupId": "chapter-1", "order": 1, "examEligible": true
  }],
  "exam": {
    "durationMinutes": 60,
    "sampling": "random",
    "sections": [
      {"type": "mcq", "count": 20, "points": 4},
      {"type": "tf", "count": 20, "points": 1}
    ],
    "coverage": []
  },
  "mastery": {"wrongThreshold": 3, "correctStreak": 2}
}
```

- `id` identifies the learning bank, not its folder name. Preserve it on revision. Separate courses or independent records should use different IDs.
- Source kinds: `pdf`, `ppt`, `pptx`, `doc`, `docx`, `md`, `ipynb`, `txt`. `file` is relative to `sources/`, never absolute or containing `..`.
- Groups appear in configured order. Source `order` determines material ordering. Questions sort within a source by a numeric locator prefix, then stable ID; use zero-padded ordinal IDs when section-only locators need a definite pedagogical order.
- `examEligible` is source metadata used by compatibility defaults; preserve it for existing sources and set it to `true` for new sources unless explicitly excluded. The app's group selection determines the sources in the user's configured paper.
- Legacy `exam.sections` use `mcq` (single choice), `multi` (multiple choice), and `tf` (true/false). User-selected types, counts and points are independent of bank pool counts; total score is computed from the user's exam configuration.
- Legacy `sampling:"random"` selects remaining questions randomly. `balanced` distributes remaining places among sources with the smallest current count per question type. Legacy `coverage` applies per-source `minimum` and optional `maximum` quotas. Preserve these existing fields during bank authoring; do not turn source question counts into quotas. The app clears legacy quotas when applying user-selected exam settings.
- Empty banks and banks that cannot fill the legacy default paper remain valid practice banks. The app checks exam feasibility against the configuration the user selects.

## Question example

```json
{
  "id": "chapter-01-mcq-001",
  "type": "mcq",
  "sourceId": "notes-1",
  "locator": {"kind": "line", "value": "12–18"},
  "topic": "Descriptive statistics",
  "difficulty": "foundational",
  "prompt": "Which statistic measures the sample center?",
  "options": [
    {"id": "mean", "text": "Sample mean"},
    {"id": "variance", "text": "Sample variance"},
    {"id": "range", "text": "Sample range"},
    {"id": "count", "text": "Number of variables"}
  ],
  "answerId": "mean",
  "explanationZh": "样本均值用于描述中心位置；其他选项不描述中心。",
  "knowledgeZh": "样本中心位置"
}
```

`questions.json` is an array of these objects. `topic` and `difficulty` are optional. IDs start with an ASCII letter or digit, then use letters, digits, `.`, `_`, `-`, at most 128 characters. IDs cannot be `__proto__`, `constructor`, or `prototype`. Each question has 2–8 unique options. For `mcq` and `tf`, `answerId` references one correct option. For `multi`, omit `answerId` and use `answerIds`: an array of at least two distinct valid option IDs. Option order and answer order do not affect grading. All correct options must be selected; partial, extra, or wrong selections earn zero points. In practice the learner selects options, then explicitly submits the answer; exams save each toggle and grade on paper submission. For `tf`, use exactly `true` and `false` option IDs (display text can follow the requested language).

Locators use `{kind,value}` with a nonempty string value: `page` (PDF), `slide` (PowerPoint), `section` (Word or headings), `line` (text/Markdown), `cell` (notebook). A value may include a precise heading/range such as `3.2 模型假设 · 段落 2` or `7 · markdown · 偏差与方差`. Optional extra provenance metadata is retained in snapshots.

JSON formula example: `"prompt": "What does \\(R^2\\) measure?"`. Do not use raw unescaped backslashes. App renders escaped text and offline KaTeX; it does not interpret arbitrary HTML or execute JavaScript in bank data.

## Records and migration

`records/progress.json` holds `{revision,state}`, including practice sessions, mastery, favorites, active exam, and authoritative history snapshots. `records/exams/<exam-id>.json` also stores each complete historical paper separately for inspection. They are written together using a recoverable pending-save journal. The app keeps prior complete JSON as `.bak`.

Question updates do not rewrite saved exam snapshots. Active exams also use snapshots of their questions, scoring weights, and absolute deadline. Retired question IDs are removed from current training collections after reload; old papers remain viewable. Changed question text/answers invalidate cached practice responses. Prefer a new question ID for substantive changes so cumulative mastery is not inherited by a different concept.

App-exported records use `{schemaVersion:1,bankId,state}`. The bank ID must match. Legacy raw `version:1` records can be imported only when all referenced question IDs exist in the current bank; the user must confirm the correct course because legacy files do not identify a bank. Never infer course identity from overlapping IDs. Legacy records lack old question snapshots; active-exam recovery uses current questions and configured scoring. Score-only historical records remain score-only.

## Multiple-choice example

```json
{
  "id": "chapter-01-multi-001",
  "type": "multi",
  "sourceId": "notes-1",
  "locator": {"kind": "line", "value": "20–28"},
  "prompt": "Which values are even? Select all that apply.",
  "options": [{"id":"two","text":"2"}, {"id":"three","text":"3"}, {"id":"four","text":"4"}],
  "answerIds": ["two", "four"],
  "explanationZh": "2 和 4 都能被 2 整除。",
  "knowledgeZh": "偶数"
}
```

Adding `multi` questions expands the reusable pool; it does not require changing `exam.sections`. The user can enable multiple-choice questions and choose their exam count and points in the app. Legacy source coverage minima/maxima also support `multi`, but bank authoring preserves them. Records use `selectedIds` for multiple-choice practice answers and arrays of option IDs in exam `answers`; single-choice and true/false records keep their existing string fields. Multi-question fingerprints include the sorted correct answer set. Historical papers preserve both question types and original scoring.
