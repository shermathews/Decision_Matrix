#Decision Matrix Generator

##Author
Sherman Mathews

##Description
Creates a blank decision matrix for use with google spreadsheets for an arbitrary combination of headers and dimensions.</br></br>
Matrix multiplication with an array of weights is used to determine each header's total. The highest total is the best choice.

##Instructions
	command: 	python matrix_generator.py filename
	results: 	decision-making matrix .csv file is created in script directory

##Issues
MMULT does not return an array of values in its product in Microsoft Excel (but Google Spreadsheets works)