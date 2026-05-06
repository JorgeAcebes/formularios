# Physics Cheat Sheets

A comprehensive collection of physics and mathematics cheat sheets, summaries, and notes.

Depending on your needs, choose one of the following approaches to use this repository:

## 1. I just want the PDFs (No compilation needed)

If you simply want to read or print the notes without dealing with LaTeX code, use the pre-compiled versions:

* Navigate to the folder of the specific subject you need.
* Locate the .pdf file that shares the same name as the folder.
* Example: For High Energy Physics, go to "Altas Energías" and open "Altas Energías.pdf".

## 2. I want to compile or modify the LaTeX code

If you wish to edit the content or manually compile the source files, follow these instructions.

### Repository Structure
Each subject is organized into its own isolated directory. The standard structure is:


```
Subject Name/
├── main.tex         # The root file. THIS is the file you must compile.
├── sections/        # Contains the individual .tex files for each chapter/topic.
├── ...              # Auxiliary images, diagrams, or tables used in the document.
└── Subject Name.pdf # The final compiled output.
```

### Requirements
To compile locally, you need a LaTeX distribution installed (TeX Live, MiKTeX, or MacTeX).

### Compilation Methods

#### Option A: Local Compilation
1. Navigate to the desired subject folder in your terminal.
2. Compile the main.tex file using pdflatex.

```text
cd "Subject Name"
pdflatex main.tex
```

#### Option B: Overleaf
1. Create a new "Blank Project" in Overleaf.
2. Upload the entire content of the subject folder (including main.tex and the sections/ directory).
3. In the project settings, ensure main.tex is selected as the "Main document".
4. Click "Recompile".

## Disclaimer
No warranties provided. While efforts were made to ensure formulaic integrity, typographical inaccuracies may exist. The author claims no responsibility for the material's suitability or correctness.

## License
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](LICENSE)

The project is licensed under the [CC BY-NC 4.0 License](LICENSE). See `LICENSE` for details.
