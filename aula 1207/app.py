from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def index():
 return redirect(url_for('registrarUsuario'))
@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if username and email and password:
            flash(f'Usuário {username} cadastrado com sucesso!', 'success')
        return redirect(url_for('registrarUsuario'))
    return render_template('formulario.html')
if __name__ == '__main__':
    app.run(debug=True)