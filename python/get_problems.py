import sys

root_url = 'https://leetcode.com/problemset/algorithms/'
next_problem = './next.txt'

def read_file(path):
	with open(path) as f:
		result = f.readlines()
	f.close()
	return result

def write_file(path , s):
	f = open(path, 'w')
	f.write(s)
	f.close()

def main(argv):
	if argv:
		num_p = int(argv[0])
		nex = read_file(next_problem)
		if nex:
			num_nex = int(nex[0])
			if num_p < num_nex:
				print "Already Have Problem %d " % num_p
			else:
				print "Getting Problem %d " % num_p
				###
					#Get
				###
				write_file(next_problem, num_p + 1)
		else:
			print "Getting Problem %d " % num_p

			write_file(next_problem, str(num_p + 1))
		print nex
	else:
		nex = read_file(next_problem)
		print "Getting next problemset."
		print nex
		print "No parameter"

if __name__ == '__main__':
	main(sys.argv[1:])