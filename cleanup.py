from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.schema import CleanupRequest, CleanupResponse, OperationStatus

from .schema import AuthContext, CleanupContext, RootContext


def handle_cleanup(req: CleanupRequest, ctx: RootContext, auth_ctx: Optional[AuthContext]) -> CleanupResponse:
    """Clean up before deleting a backup."""
    rsp_ctx = CleanupContext(
        taskUuid=req.taskUuid,
    )
    return CleanupResponse(
        taskUuid=req.taskUuid,
        status=OperationStatus.PENDING,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )
