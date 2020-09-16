# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">Telerik\nAcademy</a>aims to provide
# free real-world practical\ntraining for young people who want to turn into\nskillful .NET software engineers.</p>
# </body>\n</html>"
import re

html_line = input()

title_pattern = '(?<=title>).+(?=</title)'
body_pattern = '(?<=body>).+(?=</body)'

title = re.findall(title_pattern, html_line)
y = re.findall(body_pattern, html_line)
body_split_pattern = r'[<].+?[>]|\\n'
z = re.sub(body_split_pattern, ' ', *y)
# content = ""
# for s in z:
#     if s != '' and not s.isdigit(): # removing the digits and the empty strings lefts from tags placed one after the other
#         content += s.strip() + " "

print("Title:", "".join(title))
print("Content:", z.strip())
#print("Content:", content.strip()) # .strip() to remove the last " "