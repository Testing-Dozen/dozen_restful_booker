from pytest_schema import schema
import requests

url = "https://automationintesting.online/message/"


def test_message_api_creats_new_messages():
    response = requests.post(url, json={
        'description': 'Hello, is there any discounts?',
        'email': 'jane@email.com',
        'name': 'Jane',
        'phone': '12345678900',
        'subject': 'Any discounts?',
    })
    assert response.status_code == 201
    print(response.text)


def test_message_sergei_and_mii(base_url):
    load = {"name": "", "email": "", "phone": "", "subject": "", "description": "hi, how are you"}
    response = requests.post(f"{base_url}/message/", json=load)
    assert response.status_code == 400
    assert schema(expected_error).is_valid(response.json())
    assert "size must be between 20 and 2000" in response.json()["fieldErrors"]


def test_message_sergei_and_mii_2(base_url):
    load = {"messageid": 2, "name": "Jay Jay Jay Jay ", "email": "jeejee@example.com", "phone": "+12883456789",
            "subject": "important",
            "description": "Hello World, this is us "}
    response = requests.post(f"{base_url}/message/", json=load)
    assert response.ok
    assert response.json()["messageid"] is not 2


expected_error = {"error": str, "errorCode": int, "errorMessage": str,
                  "fieldErrors": list}

error_message_cleaned_to_dict_for_readability = {
    "errorMessage": {
        "description": "[Size.message.description,Size.description,Size.java.lang.String,Size], default message [description],2000,20]; default message [size must be between 20 and 2000]",
        "name": "[NotBlank.message.name,NotBlank.name,NotBlank.java.lang.String,NotBlank], default message [name]]; default message [must not be blank]",
        "subject_1": "[NotBlank.message.subject,NotBlank.subject,NotBlank.java.lang.String,NotBlank], default message [subject]]; default message [must not be blank]",
        "subject_2": "[Size.message.subject,Size.subject,Size.java.lang.String,Size], default message [subject],100,5]; default message [size must be between 5 and 100]",
        "phone_1": "[NotBlank.message.phone,NotBlank.phone,NotBlank.java.lang.String,NotBlank],default message [phone]]; default message [must not be blank]",
        "phone_2": "[Size.message.phone,Size.phone,Size.java.lang.String,Size], default message [phone],21,11]; default message [size must be between 11 and 21]",
        "email": "[NotBlank.message.email,NotBlank.email,NotBlank.java.lang.String,NotBlank], default message [email]]; default message [must not be blank]"}
}

full_error_message = {'error': 'BAD_REQUEST',
                      'errorCode': 400,
                      'errorMessage': 'Validation failed for argument [0] in public '
                                      'org.springframework.http.ResponseEntity<com.automationintesting.model.db.Message> '
                                      'com.automationintesting.api.MessageController.createMessage(com.automationintesting.model.db.Message) '
                                      'throws java.sql.SQLException with 7 errors: [Field error in '
                                      "object 'message' on field 'phone': rejected value []; codes "
                                      '[NotBlank.message.phone,NotBlank.phone,NotBlank.java.lang.String,NotBlank]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.phone,phone]; arguments []; default message '
                                      '[phone]]; default message [must not be blank]] [Field error '
                                      "in object 'message' on field 'name': rejected value []; "
                                      'codes '
                                      '[NotBlank.message.name,NotBlank.name,NotBlank.java.lang.String,NotBlank]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.name,name]; arguments []; default message '
                                      '[name]]; default message [must not be blank]] [Field error '
                                      "in object 'message' on field 'description': rejected value "
                                      '[hi, how are you]; codes '
                                      '[Size.message.description,Size.description,Size.java.lang.String,Size]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.description,description]; arguments []; '
                                      'default message [description],2000,20]; default message '
                                      '[size must be between 20 and 2000]] [Field error in object '
                                      "'message' on field 'subject': rejected value []; codes "
                                      '[Size.message.subject,Size.subject,Size.java.lang.String,Size]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.subject,subject]; arguments []; default '
                                      'message [subject],100,5]; default message [size must be '
                                      "between 5 and 100]] [Field error in object 'message' on "
                                      "field 'subject': rejected value []; codes "
                                      '[NotBlank.message.subject,NotBlank.subject,NotBlank.java.lang.String,NotBlank]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.subject,subject]; arguments []; default '
                                      'message [subject]]; default message [must not be blank]] '
                                      "[Field error in object 'message' on field 'phone': rejected "
                                      'value []; codes '
                                      '[Size.message.phone,Size.phone,Size.java.lang.String,Size]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.phone,phone]; arguments []; default message '
                                      '[phone],21,11]; default message [size must be between 11 and '
                                      "21]] [Field error in object 'message' on field 'email': "
                                      'rejected value []; codes '
                                      '[NotBlank.message.email,NotBlank.email,NotBlank.java.lang.String,NotBlank]; '
                                      'arguments '
                                      '[org.springframework.context.support.DefaultMessageSourceResolvable: '
                                      'codes [message.email,email]; arguments []; default message '
                                      '[email]]; default message [must not be blank]] ',
                      'fieldErrors': ['must not be blank',
                                      'must not be blank',
                                      'size must be between 20 and 2000',
                                      'size must be between 5 and 100',
                                      'must not be blank',
                                      'size must be between 11 and 21',
                                      'must not be blank']}
