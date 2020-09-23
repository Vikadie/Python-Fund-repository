def title_tag(title):
    tagged = f"<h1>\n   {title}\n</h1>"
    print(tagged)


def article_tag(article):
    tagged = f"<article>\n   {article}\n</article>"
    print(tagged)


def div_tag(comment):
    tagged = f"<div>\n   {comment}\n</div>"
    print(tagged)


title = input()
title_tag(title)
article = input()
article_tag(article)
comment = input()

while comment != "end of comments":
    div_tag(comment)
    comment = input()