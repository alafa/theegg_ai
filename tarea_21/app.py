import sys
import time


def get_irreducible_fraction(input_num):

	# Encontrar cuantos decimales tiene
	decimal_part = str(input_num).split('.')[1]
	if decimal_part == '0':
		decimal_places = 0
	else:
		decimal_places = len(decimal_part)

	# Partes candidatas a la fracción final
	top_fraction = int(input_num * 10**decimal_places)
	bottom_fraction = int(10**decimal_places)

	# Iterar hasta no encontrar ningún MCD mayor que 1
	gcd = None
	while gcd != 1:
		gcd = get_greatest_common_divisor(top_fraction, bottom_fraction)
		top_fraction = int(top_fraction / gcd)
		bottom_fraction = int(bottom_fraction / gcd)
		
	print("{}/{}".format(top_fraction, bottom_fraction))
	
# Función para encontrar el MCD de dos números
def get_greatest_common_divisor(num1, num2):

	# Función para encontrar divisodres de un número
	def get_divisors_of_num(num):
		return [i for i in range(2, num + 1) if num % i == 0]
		
	num1_divisors = get_divisors_of_num(num1)
	num2_divisors = get_divisors_of_num(num2)

	# Recorrer los dividores de num1 empezando por el final (por el más grande)
	for i in range(len(num1_divisors)-1, -1, -1):
		# Buscar a ver si el divisor está entre los de num2
		if num1_divisors[i] in num2_divisors:
			return num1_divisors[i]

	# No ha encontrado ningúno en común.
	return 1
	

# Pedir al usuario un número y devolverlo
def get_num_from_std_input():

	print("Please enter a float number:")
	input = sys.stdin.readline()
		
	try:
		input_num = float(input)
		return input_num
		
	except:
		print("ERROR: {} not valid. Argument needs to be a number".format(input))
		time.sleep(2)
		return None


			
if __name__ == "__main__":
	
	input_num = None

	# Iterar hasta conseguir un número válido
	while input_num is None:

		input_num = get_num_from_std_input()
		get_irreducible_fraction(input_num)
