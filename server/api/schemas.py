from rest_framework.schemas import AutoSchema, ManualSchema
import coreapi
import coreschema

class AttemptSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='attemptID',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='ID попытки')
                ),
                coreapi.Field(
                    name='patternAnswer',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='ID шаблона')
                ),
                coreapi.Field(
                    name='test',
                    location='form',
                    required=False,
                    schema=coreschema.Number(description='ID теста')
                ),
                coreapi.Field(
                    name='question',
                    location='form',
                    required=False,
                    schema=coreschema.String(description='ID вопроса')
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