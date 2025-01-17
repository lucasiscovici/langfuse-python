# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ModelUsageUnit(str, enum.Enum):
    CHARACTERS = "CHARACTERS"
    TOKENS = "TOKENS"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    IMAGES = "IMAGES"

    def visit(
        self,
        characters: typing.Callable[[], T_Result],
        tokens: typing.Callable[[], T_Result],
        milliseconds: typing.Callable[[], T_Result],
        seconds: typing.Callable[[], T_Result],
        images: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelUsageUnit.CHARACTERS:
            return characters()
        if self is ModelUsageUnit.TOKENS:
            return tokens()
        if self is ModelUsageUnit.MILLISECONDS:
            return milliseconds()
        if self is ModelUsageUnit.SECONDS:
            return seconds()
        if self is ModelUsageUnit.IMAGES:
            return images()
