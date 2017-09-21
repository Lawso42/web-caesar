from flask import Flask
from caesar import rotate_string, rotate_character, rotate_string_13, alphabet_position 

app = Flask(__name__)
app.config['DEBUG'] = True


page_header = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width; 540px;
                font 16px sans-serif;
                border-radius:10px;
            }}
            textarea {{
                margin: 10px 0;
                width:540px;
                height: 120px;
            }}
        </style>
    </head>
    </html>
    '''
form = '''
    <form method = "post"> 
    
    <label>Rotate By:</label><input type ="text" name="rot" value=0 />
    
    <br>
    <textarea name="text">{0}</textarea> 
    <input type = "submit" />
    <br></form>

        
    

'''

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    from flask import Flask, request
    #rot = request.args.get("rot")
    #text = request.args.get("text")
    rot = request.form["rot"]
    rot = int(rot)  
    text = request.form["text"]

    new_text = ""
    
    new_text = new_text + rotate_string(text, rot)
    return '''<form method = "post"> 
    
    <label>Rotate By:</label><input type ="text" name="rot" value=0 />
    
   
    <textarea name="text">{}</textarea> 
    <input type = "submit" />
    <br></form>'''.format(new_text)


app.run()