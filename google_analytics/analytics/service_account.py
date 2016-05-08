from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials


def get_access_token():
    """ Get token for apis into SCOPE """
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            settings.SERVICE_ACCOUNT_PKCS12_FILE_PATH,
            settings.SCOPE,
        )
        return credentials.get_access_token().access_token
    except Exception, e:
        return None
