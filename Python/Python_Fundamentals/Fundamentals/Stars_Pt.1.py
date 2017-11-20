def draw_stars(num):
	for item in num:
		try: 
			item = int(item)
			print "*" * item
		except ValueError:
			letter = item[0:1]
			print letter.lower() * len(item)

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)