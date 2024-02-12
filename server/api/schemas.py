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
                    schema=coreschema.String(description='ID Попытки')
                ),
                coreapi.Field(
                    name='test',
                    location='form',
                    required=False,
                    schema=coreschema.Number(description='ID Теста')
                ),
                coreapi.Field(
                    name='answers',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='ID Ответа')
                )
        ]
    
class ScoreSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='answer',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='ID ответа')
                )
        ]