## 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- `True`

- `False`

- `True`

## 다음의 HTTP status code의 의미를 간략하게 작성하시오.

- `200` : OK, 요청이 성공적으로 전달됨.

- `400` : Bad Request, 서버가 요청을 이해할 수 없음.

- `401` : Unauthorized, 인증되지 않은 요청(식별되지 않은 유저)

- `403` : Forbidden, 접근할 수 없는 클라이언트의 요청(서버는 클라이언트가 누구인지 알고있음)

- `404` : Not Found, 존재하지 않는 경로

- `500` : Internal Server Error, 알 수 없는 서버 오류

## 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('__all__')
```

## Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

웹 API를 시작하기 위해 가장 먼저 필요하며, 클라이언트의 요청에 응답을 json등의 형태로 제공하는 것
