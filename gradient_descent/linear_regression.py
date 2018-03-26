
import csv

def run():
	points = genfromtxt("data.csv")
	print points
	print len(points)
	initial_b = 0 # initial y-percept guess
	initial_m = 0 # initial slope guess
	num_iters = 1000
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, num_iters)


def genfromtxt(csv_file):
	with open(csv_file, 'r') as f:
		data = [row for row in csv.reader(f.read().splitlines())]
	return data


def compute_error_for_line_given_points():
	totalError = 0
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y - (m*x + b)) ** 2
	return totalError / float(len(points))


def gradient_descent_runner(points, starting_b, starting_m, num_iters):
	# TO DO: add learning rate
	b = starting_b
	m = starting_m
	for i in range(num_iters):
		b, m = step_gradient(b, m, points)
	return [b, m]


def step_gradient(b_current, m_current, points):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		b_gradient += -(2/N) * (y - ((m_current*x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current*x) + b_current))
	new_b = b_current - b_gradient
	new_m = m_current - m_gradient
	return [new_b, new_m]

if __name__ == '__main__':
	run()
