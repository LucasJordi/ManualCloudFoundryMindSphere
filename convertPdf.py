import markdown



with open('README.md', 'r', encoding="utf8") as f:
    text = f.read()
    html = markdown.markdown(text)

with open('Manual_Cloud_Foundry(MindSphere).html', 'w',encoding="utf8") as f:
    f.write(""" <style  type="text/css">
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;1,100&display=swap');
body{
  font-family: 'Roboto', sans-serif;;
  font-size: 14px;
  line-height: 1.5;
  background-color: var(--color-canvas-default);
  margin-left:5%;
  word-wrap: break-word;    
}
h1{
  margin-top:2%;
  text-align:center;
}
h2{
  margin-top:5%
}
a{    
  text-decoration: none;
}
li{
  margin-bottom:2%;
  margin-top:2%
}
ol{
  margin-bottom:5%
}
figure{
  margin-bottom:5%;
  margin-top:5%;
  width:80%
}
figcaption{
  font-size:12px;
  font-weight:bold
}
img{
  width:80%
}
</style>"""+html)


### Para transformar html em pdf executar comando wkhtmltopdf --enable-local-file-access Manual_Cloud_Foundry(MindSphere).html Manual_Cloud_Foundry(MindSphere).pdf