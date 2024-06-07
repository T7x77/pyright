from _typeshed import Incomplete

INDEX_NAME: str
INDEX_URL: Incomplete
TOKEN_USERNAME: str
log: Incomplete

def resolve_repository_name(repo_name): ...
def resolve_index_name(index_name): ...
def get_config_header(client, registry): ...
def split_repo_name(repo_name): ...
def get_credential_store(authconfig, registry): ...

class AuthConfig(dict[str, Incomplete]):
    def __init__(self, dct, credstore_env: Incomplete | None = None) -> None: ...
    @classmethod
    def parse_auth(cls, entries, raise_on_error: bool = False): ...
    @classmethod
    def load_config(cls, config_path, config_dict, credstore_env: Incomplete | None = None): ...
    @property
    def auths(self): ...
    @property
    def creds_store(self): ...
    @property
    def cred_helpers(self): ...
    @property
    def is_empty(self): ...
    def resolve_authconfig(self, registry: Incomplete | None = None): ...
    def get_credential_store(self, registry): ...
    def get_all_credentials(self): ...
    def add_auth(self, reg, data) -> None: ...

def resolve_authconfig(authconfig, registry: Incomplete | None = None, credstore_env: Incomplete | None = None): ...
def convert_to_hostname(url): ...
def decode_auth(auth): ...
def encode_header(auth): ...
def parse_auth(entries, raise_on_error: bool = False): ...
def load_config(
    config_path: Incomplete | None = None, config_dict: Incomplete | None = None, credstore_env: Incomplete | None = None
): ...