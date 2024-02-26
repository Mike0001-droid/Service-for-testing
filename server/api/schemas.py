from rest_framework.schemas import AutoSchema, ManualSchema
import coreapi
import coreschema

class AttemptSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='attempt',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID попытки')
                ),
                coreapi.Field(
                    name='patternAnswer',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='Массив id шаблонов')
                ),
                coreapi.Field(
                    name='test',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID теста')
                ),
                coreapi.Field(
                    name='question',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID вопроса')
                ),
        ]
    
class ScoreSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='user_id',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID юзера')
                ),
                coreapi.Field(
                    name='answer_id',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID ответа')
                )
        ]
