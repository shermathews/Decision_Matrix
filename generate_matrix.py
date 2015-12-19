"""creates a decision-making matrix and saves to csv"""

from matrix import Matrix
import csv
import sys

def main():
	try:
		fname = sys.argv[1]
	except:
		print "Improper command entry. Please retry."
		print "Proper command is 'python create_matrix.py filename'"
		quit()
	try:
		#get inputs for decision matrix
		print "please enter the headers (i.e.: x y z)"
		x_axis = raw_input().split()
		print "please enter the dimensions (i.e.: width weight height)"
		y_axis = raw_input().split()
		
		#generates decision matrix
		matrix = Matrix(len(x_axis), len(y_axis), x_axis, y_axis)
		matrix.populate()
	except:
		print "Failed to populate Matrix. Please ensure your headers and dimensions are in the correct format."
		quit()
	#exports to csv
	try:
		f = open(fname + ".csv", "wb")
		writer = csv.writer(f)
		for value in matrix.data:
			writer.writerow(value)
		f.close()
		print "Saved Matrix as %s.csv" % (fname)
	except:
		print "Failed to save file. Perhaps an instance of the same name is open."
		quit()
		
if __name__ == '__main__':
    main()

