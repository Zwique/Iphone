from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this in production

# Fixed passcode
PASSCODE = "1111"
FLAG = "uacCTF{iph0n3_brut3f0rc3_succ3ss}"

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    flag = ""
    
    if request.method == 'POST':
        user_input = request.form.get('passcode')
        
        if user_input == PASSCODE:
            message = "Correct! You've unlocked the phone."
            flag = FLAG  # Show flag when unlocked
        else:
            message = "Incorrect! Try again."
    
    return render_template('index.html', message=message, flag=flag)

if __name__ == '__main__':
    app.run(debug=True)

