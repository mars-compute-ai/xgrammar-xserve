from typing import TYPE_CHECKING, Any

from . import exception, load_binding, structural_tag, testing
from .builtin_structural_tag import (
    get_builtin_structural_tag,
    get_model_structural_tag,
    normalize_tool_choice,
    register_model_structural_tag,
)
from .compiler import CompiledGrammar, GrammarCompiler
from .config import (
    get_max_recursion_depth,
    get_serialization_version,
    max_recursion_depth,
    set_max_recursion_depth,
)
from .exception import (
    DeserializeFormatError,
    DeserializeVersionError,
    InvalidJSONError,
    InvalidStructuralTagError,
)
from .grammar import Grammar, StructuralTagItem
from .matcher import (
    BatchGrammarMatcher,
    GrammarMatcher,
    allocate_token_bitmask,
    apply_token_bitmask_inplace,
    bitmask_dtype,
    get_bitmask_shape,
    reset_token_bitmask,
)
from .structural_tag import StructuralTag
from .tokenizer_info import TokenizerInfo, VocabType

if TYPE_CHECKING:
    from .contrib import hf


def __getattr__(name: str) -> Any:
    if name == "hf":
        from .contrib import hf

        globals()[name] = hf
        return hf
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "exception",
    "structural_tag",
    "testing",
    "CompiledGrammar",
    "GrammarCompiler",
    "get_max_recursion_depth",
    "get_serialization_version",
    "max_recursion_depth",
    "set_max_recursion_depth",
    "hf",
    "DeserializeFormatError",
    "DeserializeVersionError",
    "InvalidJSONError",
    "InvalidStructuralTagError",
    "Grammar",
    "StructuralTagItem",
    "BatchGrammarMatcher",
    "GrammarMatcher",
    "allocate_token_bitmask",
    "apply_token_bitmask_inplace",
    "bitmask_dtype",
    "get_bitmask_shape",
    "reset_token_bitmask",
    "StructuralTag",
    "TokenizerInfo",
    "VocabType",
    "get_model_structural_tag",
    "normalize_tool_choice",
    "register_model_structural_tag",
    "get_builtin_structural_tag",
]
