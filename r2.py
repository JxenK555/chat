

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	a_word = 0
	a_sticker = 0
	a_image = 0
	v_word = 0
	v_sticker = 0
	v_image = 0
	for line in lines:
		s =  line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == 'Sticker':
				a_sticker += 1
			elif s[2] == 'Image':
				a_image += 1
			else:
				for m in s[2:]:
					a_word += len(m)
		elif name == 'Viki':
			if s[2] == 'Sticker':
				v_sticker += 1
			elif s[2] == 'Image':
				v_image += 1
			else:
				for m in s[2]:
					v_word += len(m)

	print('Allen sent', a_word, 'words')
	print('Allen sent', a_image, 'image')
	print('Allen sent', a_sticker, 'sticker')

	print('Viki sent', v_word, 'words')
	print('Viki sent', v_image, 'image')
	print('Viki sent', v_sticker, 'sticker')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Viki.txt')
	lines = convert(lines)