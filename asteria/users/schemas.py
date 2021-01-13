from asteria.db import ma


class UserSchema(ma.Schema):
    """The UserSchema is used to define a schema for the User class. The class serializes and deserializes data for
    the User class in HTTP requests."""
    class Meta:
        """The Meta class contains meta information for UserSchema such as the parameters that get serialized."""
        fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'city_of_birth', 'email')
        ordered = True


user_schema = UserSchema()
