from flask import Flask,request,render_template
import os
import time
from openai import OpenAI



app = Flask(__name__)

openai_api_key = os.getenv["OPENAI_API_TOKEN"]
model = OpenAI(api_key=openai_api_key)


r = ""
first_time = 1

#
@app.route("/",methods=["GET","POST"])
def index():
  return (render_template("index.html"))


#main
@app.route("/main",methods=["GET","POST"])
def mian():
  global r,first_time
  if first_time == 1:
    r=request.form.get()
  return (render_template("main.html",r = r))


"""
#image_gpt
@app.route("/image_gpt",methods=["GET","POST"])
def image_gpt():
  return(render_template("/image_gpt.html"))


#image_result
@app.route("/image_result",methods=["GET","POST"])
def image_result():
  q = request.form.get("q")
  r = replicate.run(
   "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",

    input={"prompt": inputs,}
  )
  time.sleep(10)
  return(render_template("image_gpt.html",r = r[0]))
  print(r)
"""
  

#text_gpt
@app.route("/text_gpt",methods=["GET","POST"])
def text_gpt():
  return(render_template("/text_gpt.html")) 


#text_result
@app.route("/text_result",methods=["GET","POST"])
def text_result():
  q = request.form.get("q")
  r = model.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"user",
            "content": q
        }
    ]
  )
  time.sleep(5)
  return(render_template("text_gpt.html",r = r.choices[0].message.content))
  

#end
@app.route("/end",methods=["GET","POST"])
def end():
  first_time = 1
  return(render_template("/image_gpt.html"))

#new box



if __name__ == "__main__":
  app.run()
