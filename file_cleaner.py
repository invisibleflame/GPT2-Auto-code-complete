import os
import time
from curtsies.fmtfuncs import red,green, bold, cyan,yellow

for dirpath, dirname, filename in os.walk("data"):
	for f in filename:
		file_path = os.path.join(dirpath, f)

		if file_path.endswith(".py"):
			print(f"keeping {file_path}")
		else:
			os.remove(file_path)
