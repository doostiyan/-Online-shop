from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6B4C4B6747327366434B456D56434876322F4435623172756F726F59672F47496B4146776C5664794E49453D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
