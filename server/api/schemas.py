from rest_framework.schemas import AutoSchema, ManualSchema
import coreapi
import coreschema

class AttemptSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='number',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Номер попытки')
                ),
                coreapi.Field(
                    name='user',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='Имя пользователя')
                ),
                coreapi.Field(
                    name='test',
                    location='form',
                    required=False,
                    schema=coreschema.Number(description='ID Теста')
                ),
                coreapi.Field(
                    name='subtest',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='ID Субтеста')
                ),
                coreapi.Field(
                    name='answer',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='ID Ответа')
                )
        ]