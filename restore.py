from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.schema import OperationStatus, RestoreRequest, RestoreResponse

from .schema import AuthContext, ContextKind, ResourceContext, RestoreContext, RootContext


def handle_restore(
    req: RestoreRequest,
    ctx: RootContext | ResourceContext,
    auth_ctx: Optional[AuthContext],
) -> RestoreResponse:
    """Restore a resource."""
    rsp_ctx = RestoreContext(
        taskUuid=req.taskUuid,
    )
    return RestoreResponse(
        status=OperationStatus.PENDING if ctx.kind == ContextKind.ROOT else OperationStatus.DONE,
        taskUuid=req.taskUuid,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )
