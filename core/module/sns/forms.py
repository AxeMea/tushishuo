from wtforms import Form, TextField,validators

class RegisterForm(Form):
	 email = TextField('email',[validators.Required()])
	 first_name = TextField('first_name',[validators.Required()])
	 last_name = TextField('last_name',  [validators.Required()])
	 password = TextField('password',  [validators.Required()])


class LoginForm(Form):
	 email = TextField('email', [validators.Required()])
	 password = TextField('password',[validators.Required()])
	
