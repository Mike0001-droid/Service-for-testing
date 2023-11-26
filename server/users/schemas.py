from rest_framework.schemas import AutoSchema, ManualSchema
import coreapi
import coreschema

    
class UserSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='name',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Имя пользователя')
                ),
                coreapi.Field(
                    name='surname',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Фамилия пользователя')
                ),
                coreapi.Field(
                    name='gender',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Пол пользователя')
                ),
                coreapi.Field(
                    name='age',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Возраст пользователя')
                ),
                coreapi.Field(
                    name='email',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Email пользователя')
                ),
                coreapi.Field(
                    name='password',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Пароль пользователя')
                ),
                coreapi.Field(
                    name='new_password',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Новый пароль пользователя')
                )
        ]