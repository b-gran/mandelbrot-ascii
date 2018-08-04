GRID_WIDTH = 160
GRID_HEIGHT = 40

MANDELBROT_MIN_X = -2.5
MANDELBROT_MAX_X = 1

MANDELBROT_MIN_Y = -1
MANDELBROT_MAX_Y = 1

PALETTE = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]

MAX_ITERATION = len(PALETTE) - 1


def transform_grid_to_mandelbrot(grid_coordinate):
	"""
	Converts grid coordinates to Mandelbrot coordinates.
	(row, column) -> (mandelbrot x, mandelbrot y)
	:return: (number, number)
	"""
	[row, column] = grid_coordinate

	x = (column / GRID_WIDTH) * (MANDELBROT_MAX_X - MANDELBROT_MIN_X) + MANDELBROT_MIN_X
	y = (row / GRID_HEIGHT) * (MANDELBROT_MAX_Y - MANDELBROT_MIN_Y) + MANDELBROT_MIN_Y

	return (x, y)


def draw_grid(characters_by_location):
	"""
	Array< Array<characters> >
	[
	    [ 0, A, B, $, ... ],
	    [ 0, A, B, $, ... ],
	    ...
	]
	:param characters_by_location:
	"""

	first_lines = characters_by_location[:-1]
	for line in first_lines:
		draw_line(line)
		print_newline()

	last_line = characters_by_location[-1]
	draw_line(last_line)


def draw_line(line_of_grid):
	for symbol in line_of_grid:
		print(symbol, end="")


def print_newline():
	print("")


def generate_fractal():
	grid = []
	for row in range(GRID_HEIGHT):
		grid.append([])
		for col in range(GRID_WIDTH):
			grid_position = (row, col)
			[x0, y0] = transform_grid_to_mandelbrot(grid_position)
			C = 2

			x = 0
			y = 0
			iteration = 0

			while x ** 2 + y ** 2 < C ** 2 and iteration < MAX_ITERATION:
				xtemp = x ** 2 - y ** 2 + x0
				y = 2 * x * y + y0
				x = xtemp
				iteration = iteration + 1

			symbol = PALETTE[iteration]
			grid[row].append(symbol)

	draw_grid(grid)


generate_fractal()
