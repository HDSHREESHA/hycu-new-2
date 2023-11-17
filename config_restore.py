from typing import Optional

from rcsdk.schema import (
    ConfigRestoreRequest,
    ConfigRestoreResponse,
    HycuLayout,
    HycuLayoutColumn,
    HycuLayoutSwitch,
    build_hycu_layout_schema,
)

from .schema import AuthContext, RootContext


def handle_config_restore(
    req: ConfigRestoreRequest,
    ctx: RootContext,
    auth_ctx: Optional[AuthContext],
) -> ConfigRestoreResponse:
    """Return restore configuration settings for the given resource."""
    match ctx.name:
        case "root:0":
            return ConfigRestoreResponse(
                possibleOptions=build_hycu_layout_schema(
                    layout=HycuLayout(
                        [
                            HycuLayoutColumn(
                                [
                                    HycuLayoutSwitch(
                                        id="offload",
                                        label="Offload",
                                        tooltip=(
                                            "Offload trades increased storage and CPU cost"
                                            " for faster database performance during restore."
                                        ),
                                    ),
                                ]
                            )
                        ]
                    ),
                    payload={
                        "options": {
                            "offload": "offload",
                        },
                    },
                ),
            )

        case _:
            return ConfigRestoreResponse()
