from flask import Flask, render_template, request, redirect, url_for, make_response, session
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def cocozinho():
    user = 'guigas priquito'
    tema = request.form.get('escuro')
    colapso = make_response('')


    return render_template('index.html', user = user, tema = tema)

@app.route('/esportes')
def naocara():
    return render_template('esportes.html')

@app.route('/lazer')
def blocodenotas():
    return render_template('lazer.html')

@app.route('/entretenimento')
def taerradokenji():
    return render_template('entretenimento.html')

if __name__ == '__main__':
    app.run(debug=True)
