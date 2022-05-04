from typing import Optional


def validate_search_length(search_string: str) -> Optional[str]:
    if len(search_string) < 3:
        return '⟷ Too short.'

    if len(search_string) > 90:
        return '⟷ Too long.'
