from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from dataclasses_json import Undefined, dataclass_json
from rcsdk.schema import OPTIONAL_ENUM, REQUIRED_ENUM

# NOTE: This module *must* expose a dataclass named AuthContext
# FIXME: Import the specific authenication context for your plugin.
#        Use the GenericAuthContext if your plugin does not require authentication.
# from rcsdk.schema import GenericAuthContext as AuthContext
# from rcsdk.schema import AwsAuthContext as AuthContext
# from rcsdk.schema import GcAuthContext as AuthContext

# Reference AuthContext to avoid warnings from linters.
# FIXME: Uncomment this if the plugin uses custom auth settings.
# _ = AuthContext


# FIXME: If you're using custom auth settings, define the schema here.
#        Otherwuise, remove this class.
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=True, kw_only=True)
class AuthContext:
    instanceUrl: str
    instanceUser: str
    instancePassword_secret: str


# A unique identifier for this plugin. This identifier is used in the
# ContextKind enumeration to make its values unique and specific to this plugin.
PLUGIN_IDENTIFIER: str = "mondaydotcom"


class ContextKind(str, Enum):
    ROOT = "root@" + PLUGIN_IDENTIFIER
    RESOURCE = "resource@" + PLUGIN_IDENTIFIER
    BACKUP = "backup@" + PLUGIN_IDENTIFIER
    RESTORE = "restore@" + PLUGIN_IDENTIFIER
    CLEANUP = "cleanup@" + PLUGIN_IDENTIFIER


class ResourceGroup(str, Enum):
    A = "Group-A"
    B = "Group-B"


@dataclass_json
@dataclass(kw_only=True)
class RootContext:
    """Context used in responses to /api/roots"""

    # Mandatory fields
    kind: str = field(init=False, default=ContextKind.ROOT)

    # Plugin-specific fields
    name: str  # FIXME: This field is just an example
    group: Optional[ResourceGroup] = field(default=None, metadata=OPTIONAL_ENUM(ResourceGroup))


@dataclass_json
@dataclass(kw_only=True)
class ResourceContext:
    """Context used in responses to /api/resources"""

    # Mandatory fields
    kind: str = field(init=False, default=ContextKind.RESOURCE)

    # Plugin-specific fields
    parent_name: str  # FIXME: This field is just an example
    parent_group: Optional[ResourceGroup] = field(default=None, metadata=OPTIONAL_ENUM(ResourceGroup))
    name: str  # FIXME: This field is just an example
    group: ResourceGroup = field(metadata=REQUIRED_ENUM(ResourceGroup))


@dataclass_json
@dataclass(kw_only=True)
class BackupContext:
    """Context used in responses to /api/backup"""

    # Mandatory fields
    kind: str = field(init=False, default=ContextKind.BACKUP)
    taskUuid: str

    # Plugin-specific fields
    # TODO: Add specific fields here
    count: int = 0  # FIXME: This field is used only for the example flow


@dataclass_json
@dataclass(kw_only=True)
class RestoreContext:
    """Context used in responses to /api/restore"""

    # Mandatory fields
    kind: str = field(init=False, default=ContextKind.RESTORE)
    taskUuid: str

    # Plugin-specific fields
    # TODO: Add specific fields here
    count: int = 0  # FIXME: This field is used only for the example flow


@dataclass_json
@dataclass(kw_only=True)
class CleanupContext:
    """Context used in responses to /api/cleanup"""

    # Mandatory fields
    kind: str = field(init=False, default=ContextKind.CLEANUP)
    taskUuid: str

    # Plugin-specific fields
    # TODO: Add specific fields here
    count: int = 0  # FIXME: This field is used only for the example flow
