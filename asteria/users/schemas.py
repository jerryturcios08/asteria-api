from asteria.db import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')


user_schema = UserSchema()
