
import re
text = "apple, banana ; orange | grape"
result = re.split(r"\s*[,;|]\s*", text)
print(result)
