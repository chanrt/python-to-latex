from settings import Settings


html_open = '<html lang="en-US">'
head_open = '<head>'
title = '<title> Equation </title>'
mathjax = '<script type="text/javascript" async \
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>'
meta = '<meta charset="utf-8" /> \
  <meta http-equiv="X-UA-Compatible" content="IE=edge" /> \
  <meta name="viewport" content="width=device-width, initial-scale=1" />'
head_close = '</head>'

head = html_open + head_open + title + mathjax + head_close

if Settings.get_dark_mode():
    body = '<body style="background: black; color: white;">'
else:
    body = '<body style="background: white; color: black;">'

left_padding = '<h1 style="text-align: center;">Equation</h1> <br> \\[ '
right_padding = ' \\] <br> <p style="text-align: center;"> Fork me at <a href="https://www.github.com/chanrt">GitHub</a> </p>'

footer = "</body> </html>"
