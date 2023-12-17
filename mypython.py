import matplotlib.pyplot as plt


def my_func(k):
	print(k + 1000)
	print("hiya!")


# This code would run anytime the file is imported or loaded
my_func(3)


def hello_world():
	print("Hello world!")


# This code is only run when the file itself is run
# The code below runs only in mypython.py, not in any files that import mypython.py
if __name__ == "__main__":
	hello_world()

	plt.plot([1, 2, 3], [1, 3, 6])
	plt.show()
