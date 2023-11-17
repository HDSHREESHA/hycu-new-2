from typing import Optional

from rcsdk.schema import (
    ConfigBackupRequest,
    ConfigBackupResponse,
    ExclusionRule,
    HycuLayout,
    HycuLayoutColumn,
    HycuLayoutDropdown,
    HycuLayoutDropdownItem,
    HycuLayoutSwitch,
    build_hycu_layout_schema,
)

from .schema import AuthContext, RootContext


def handle_config_backup(
    req: ConfigBackupRequest,
    ctx: RootContext,
    auth_ctx: Optional[AuthContext],
) -> ConfigBackupResponse:
    """Return backup configuration settings for the given resource."""
    match ctx.name:
        case "root:0":
            return ConfigBackupResponse(
                possibleExcludes=[
                    ExclusionRule(
                        ctx={"exclude": "root:0"},
                        id="root:0",
                        name="Root 0",
                        subResources=[
                            ExclusionRule(
                                ctx={"exclude": "rsrc:0"},
                                id="rsrc:0",
                                name="Root 0 / Resource 1",
                                subResources=[
                                    ExclusionRule(
                                        ctx={"exclude": "rsrc:2"},
                                        id="rsrc:2",
                                        name="Root 0 / Resource 1 / Resource 3",
                                    ),
                                    ExclusionRule(
                                        ctx={"exclude": "rsrc:3"},
                                        id="rsrc:3",
                                        name="Root 0 / Resource 1 / Resource 4",
                                    ),
                                ],
                            ),
                            ExclusionRule(
                                ctx={"exclude": "rsrc:1"},
                                id="rsrc:1",
                                name="Root 0 / Resource 1",
                            ),
                        ],
                    ),
                ],
                possibleOptions=build_hycu_layout_schema(
                    layout=HycuLayout(
                        [
                            HycuLayoutColumn(
                                [
                                    HycuLayoutDropdown(
                                        id="exportFormat",
                                        label="Export format",
                                        items=[
                                            HycuLayoutDropdownItem("Export format 1", "exportValue1"),
                                            HycuLayoutDropdownItem("Export format 2", "exportValue2"),
                                            HycuLayoutDropdownItem("Export format 3", "exportValue3"),
                                        ],
                                        validate_required=True,
                                    ),
                                    HycuLayoutSwitch(
                                        id="offload",
                                        label="Offload",
                                        tooltip=(
                                            "Offload trades increased storage and CPU cost"
                                            " for faster database performance during backup."
                                        ),
                                    ),
                                ]
                            )
                        ]
                    ),
                    payload={
                        "options": {
                            "offload": "offload",
                            "exportFormat": "exportFormat",
                            "test": "Not an input field Id",
                        },
                    },
                ),
            )

        case "root:1":
            return ConfigBackupResponse(
                possibleExcludes=[
                    ExclusionRule(
                        ctx={"exclude": "root:1"},
                        id="root:1",
                        name="Root 1",
                    ),
                ],
            )

        case _:
            return ConfigBackupResponse()
