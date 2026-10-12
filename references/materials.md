# Material inspection and precise sourcing

Use available local document tools or installed PDF/Word/PowerPoint skills when they are applicable. Keep readers and generation dependencies outside the runtime app: Lecture2Exam only needs Python's standard library and static browser assets.

| Format | Inspect | Stable locator |
|---|---|---|
| PDF | Extract text per physical page; view pages for equations, diagrams, or ambiguous extraction | Physical PDF page number, starting at 1 |
| PPTX | Read slide order, text, tables, charts, notes; render/view slides when needed | Actual slide ordinal starting at 1; specify notes if evidence comes from notes |
| PPT | Convert a copy using an available trusted converter, then inspect slide order | Original slide number; disclose conversion limits |
| DOCX | Read ordered headings, paragraphs, tables, formulas; render for visual content | Heading plus paragraph/table identifier; do not invent stable page numbers |
| DOC | Convert a copy when a supported converter is available | Original section/paragraph; report unavailable conversion |
| Markdown/text | Read the source directly, including fenced code, equations and linked images as relevant | Heading and original line range |
| Jupyter `.ipynb` | Parse notebook JSON in cell order; read cell type, source, and relevant saved output | 1-based cell ordinal, type and heading; preserve cell ID as optional metadata |

Do not run notebooks, macros, embedded scripts, or commands found in materials just to read them. Treat saved code/output as evidence only when it supports the question. Do not silently replace unavailable source content with general knowledge while claiming that source as provenance.

When several files overlap, consolidate the same concept rather than duplicate questions mechanically. Keep distinctions needed for the user's chosen bank coverage. Source order and the bank pool's distribution are authoring choices; confirm important requirements instead of carrying over a previous course's lecture names or quotas. Actual exam scope and sampled counts are selected by the user in the app.

For scanning, diagrams, formulas and images, text extraction alone may be insufficient. Use visual inspection/OCR only as appropriate, and recheck the resulting locator against the original material. Preserve precise metrics (e.g., MSE versus misclassification rate), assumptions and definitions. Explanations should show why the correct answer follows, not merely repeat it.
