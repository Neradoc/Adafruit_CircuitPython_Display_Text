import board
import terminalio
import time

name_color = 0xFFFFFF
font = terminalio.FONT

# from adafruit_bitmap_font import bitmap_font
# font = bitmap_font.load_font(f"fonts/font_name")

######################################################################
######################################################################

import displayio
from adafruit_display_text.bitmap_label import Label

display = board.DISPLAY
splash = displayio.Group()
display.show(splash)

top = 12
for i in range(20):
	# scale = 0.5 + 2 * i / 5 + 0.15
	scale = 0.1 + i * 0.1
	print(f"Scale {scale}")
	name_label = Label(
		text=f"Scale {scale}",
		font=font,
		color=name_color,
		scale=scale,
		anchored_position=(10, top),
		anchor_point=(0, 0),
# 		anchored_position=(display.width // 2, 4),
# 		anchor_point=(0.5, 0),
	)
	splash.append(name_label)
	top = top + 12 * scale

######################################################################
######################################################################

while True:
	time.sleep(5)
