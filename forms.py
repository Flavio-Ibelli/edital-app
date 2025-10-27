from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Função', choices=[('user', 'Usuário'), ('admin', 'Administrador')], default='user')
    submit = SubmitField('Registrar')

class EditalForm(FlaskForm):
    titulo = StringField('Título do Edital', validators=[DataRequired()])
    numero = StringField('Número do Edital', validators=[DataRequired()])
    orgao = StringField('Órgão', validators=[DataRequired()])
    modalidade = SelectField('Modalidade', choices=[
        ('pregao_eletronico', 'Pregão Eletrônico'),
        ('concorrencia', 'Concorrência'),
        ('tomada_precos', 'Tomada de Preços'),
        ('convite', 'Convite'),
        ('concurso', 'Concurso'),
        ('leilao', 'Leilão')
    ], validators=[DataRequired()])
    objeto = TextAreaField('Objeto', validators=[DataRequired()])
    valor_estimado = StringField('Valor Estimado')
    data_abertura = StringField('Data de Abertura', validators=[DataRequired()])
    hora_abertura = StringField('Hora de Abertura', validators=[DataRequired()])
    local_abertura = TextAreaField('Local de Abertura')
    endereco_retirada = TextAreaField('Endereço para Retirada do Edital')
    informacoes_adicionais = TextAreaField('Informações Adicionais')
    arquivo_anexo = FileField('Arquivo Anexo')
    submit = SubmitField('Gerar Edital')
