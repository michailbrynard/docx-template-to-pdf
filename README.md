# docx-template-to-pdf

Bulk-generate PDFs from a DOCX template and CSV data. Uses [docxtpl](https://docxtpl.readthedocs.io/) to render Jinja2 placeholders in a `.docx` template and [LibreOffice](https://www.libreoffice.org/) to convert the result to PDF.

## Prerequisites

- Python 3.6+
- [LibreOffice](https://www.libreoffice.org/download/download/) installed and available on your `PATH` (or at `/Applications/LibreOffice.app` on macOS)

## Installation

```bash
pip install docxtpl
```

## Usage

### 1. Create a DOCX template

Create a file called `template-example.docx` in Word (or any editor that saves `.docx`). Inside the document use Jinja2-style placeholders such as:

```
Dear {{ FirstName }} {{ LastName }},

Your account number is {{ AccountNo }}.
```

### 2. Create a CSV data file

Create a file called `context.csv` with a header row matching the placeholder names:

```csv
FirstName,LastName,AccountNo
Alice,Smith,1001
Bob,Jones,1002
```

### 3. Run the script

```bash
python app.py
```

By default `app.py` looks for `template-example.docx` and `context.csv` in the current directory. For each row in the CSV it will:

1. Render the template with that row's data.
2. Save a `.docx` file named using the output template (e.g. `Test Document - Alice - Alice.docx`).
3. Convert the `.docx` to PDF in the same directory.

### Using as a library

You can also import the helper function directly:

```python
from app import docx_template_to_pdf

context = {"FirstName": "Alice", "LastName": "Smith", "AccountNo": "1001"}
docx_template_to_pdf(
    context=context,
    template_path="template-example.docx",
    output_file_name_template="Output - {FirstName}.docx",
)
```

## Project structure

```
├── app.py              # Main entry point
├── common/
│   └── docx2pdf.py     # LibreOffice DOCX-to-PDF conversion helper
├── README.md
└── .gitignore
```

## License

See repository for license details.
