from typing import Any

logger: Any
POSITIONAL_WARNING: str
POSITIONAL_EXCEPTION: str
POSITIONAL_IGNORE: str
POSITIONAL_SET: Any
positional_parameters_enforcement = POSITIONAL_WARNING

def positional(max_positional_args: Any): ...
def scopes_to_string(scopes: Any): ...
def string_to_scopes(scopes: Any): ...
def parse_unique_urlencoded(content: Any): ...
def update_query_params(uri: Any, params: Any): ...
def validate_file(filename: Any) -> None: ...
