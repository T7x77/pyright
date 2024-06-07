from typing import TypeVar

from requests_oauthlib import OAuth2Session

_OAuth2SessionT = TypeVar("_OAuth2SessionT", bound=OAuth2Session)

def slack_compliance_fix(session: _OAuth2SessionT) -> _OAuth2SessionT: ...
