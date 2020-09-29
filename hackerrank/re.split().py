regex_pattern = r"[\.\,]"	# Do not delete 'r'.

import re

x = re.split(regex_pattern, input())

print("\n".join(x))