from typing import Optional

from rcsdk.errors import APIValidationError
from rcsdk.schema import RestoreScenario, ScenariosRestoreRequest, ScenariosRestoreResponse

from .schema import AuthContext, RootContext


def handle_scenarios_restore(
    req: ScenariosRestoreRequest,
    ctx: RootContext,
    auth_ctx: Optional[AuthContext],
) -> ScenariosRestoreResponse:
    """Return restore scenarios for the given resource."""
    rsp = ScenariosRestoreResponse(restoreScenarios=[])
    for kind in req.types:
        match kind:
            case "Root Resource":
                rsp.restoreScenarios.append(
                    RestoreScenario(
                        type=kind,
                        name=kind,
                        description="Restore the root resource.",
                    )
                )

            case "Resource":
                rsp.restoreScenarios.append(
                    RestoreScenario(
                        type=kind,
                        name=kind,
                        description="Restore a sub-resource.",
                    )
                )

            case _:
                raise APIValidationError(f"Unknown resource type '{kind}")

    return rsp
