from flask_security.forms import LoginForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, HiddenField, ValidationError

from flask import request, jsonify, helpers, abort, session, flash

from flask_security.utils import config_value, get_message, hash_password, \
    localize_callback, url_for_security, validate_redirect_url, \
    verify_and_update_password
from database import models
from app.security import security, user_datastore


class ValidatorMixin(object):
    def __call__(self, form, field):
        if self.message and self.message.isupper():
            self.message = get_message(self.message)[0]
        return super(ValidatorMixin, self).__call__(form, field)

class Required(ValidatorMixin, validators.DataRequired):
    pass


class ExtendedLoginForm(LoginForm):


    def validate(self):
        if not super(ExtendedLoginForm, self).validate():
            return False

        self.user = user_datastore.get_user(self.email.data)

        if self.user is None:
            self.email.errors.append(get_message('USER_DOES_NOT_EXIST')[0])
            # Reduce timing variation between existing and non-existung users
            hash_password(self.password.data)
            return False
        if not self.user.password:
            self.password.errors.append(get_message('PASSWORD_NOT_SET')[0])
            # Reduce timing variation between existing and non-existung users
            hash_password(self.password.data)
            return False
        if not verify_and_update_password(self.password.data, self.user):
            self.password.errors.append(get_message('INVALID_PASSWORD')[0])
            return False
        if not self.user.is_active:
            self.email.errors.append(get_message('DISABLED_ACCOUNT')[0])
            return False
        return True

