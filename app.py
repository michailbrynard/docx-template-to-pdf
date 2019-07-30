from docxtpl import DocxTemplate
import csv
from common.docx2pdf import LibreOfficeError, convert_to
import os

def docx_template_to_pdf(context: dict, template_path: str, output_file_name_template: str):
	doc = DocxTemplate(template_path)
	doc.render(context)
	file_name=output_file_name_template.format(**row)
	doc.save(file_name)
	result = convert_to(os.getcwd(),file_name)

if __name__ == '__main__':
	output_file_name_template = 'Test Document - {TestVariable1} - {TestVariable1}.docx'
	template_path = 'template-example.docx'

	with open('context.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			docx_template_to_pdf(row, template_path, output_file_name_template)

