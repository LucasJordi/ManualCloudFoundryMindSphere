import markdown

import pdfkit

with open('README.md', 'r', encoding="utf8") as f:
    text = f.read()
    html = markdown.markdown(text)

with open('Manual_Cloud_Foundry(MindSphere).html', 'w',encoding="utf8") as f:
    f.write(html)


### Para transformar html em pdf executar comando wkhtmltopdf --enable-local-file-access Manual_Cloud_Foundry(MindSphere).html Manual_Cloud_Foundry(MindSphere).pdf