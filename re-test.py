import re

X = "This    is a tist."

m = re.findall("s.{2}", X)

print(m)