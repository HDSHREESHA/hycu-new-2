from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.errors import APIValidationError
from rcsdk.schema import OperationStatus, StatusRequest, StatusResponse

from .schema import AuthContext, BackupContext, CleanupContext, RestoreContext


def handle_status_of_backup_task(
    req: StatusRequest,
    ctx: BackupContext,
    auth_ctx: Optional[AuthContext],
) -> StatusResponse:
    """Handle status request with backup context."""
    _check_task_uuid(req, ctx)
    rsp_ctx = BackupContext(
        taskUuid=req.taskUuid,
        count=ctx.count + 1,  # FIXME: Remove, used only for example flow.
    )
    return StatusResponse(
        taskUuid=req.taskUuid,
        status=OperationStatus.RUNNING if rsp_ctx.count < 2 else OperationStatus.DONE,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )


def handle_status_of_restore_task(
    req: StatusRequest,
    ctx: RestoreContext,
    auth_ctx: Optional[AuthContext],
) -> StatusResponse:
    """Handle status request with restore context."""
    _check_task_uuid(req, ctx)
    rsp_ctx = RestoreContext(
        taskUuid=req.taskUuid,
        count=ctx.count + 1,  # FIXME: Remove, used only for example flow.
    )
    return StatusResponse(
        taskUuid=req.taskUuid,
        status=OperationStatus.RUNNING if rsp_ctx.count < 2 else OperationStatus.DONE,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )


def handle_status_of_cleanup_task(
    req: StatusRequest,
    ctx: CleanupContext,
    auth_ctx: Optional[AuthContext],
) -> StatusResponse:
    """Handle status request with restore context."""
    _check_task_uuid(req, ctx)
    rsp_ctx = CleanupContext(
        taskUuid=req.taskUuid,
        count=ctx.count + 1,  # FIXME: Remove, used only for example flow.
    )
    return StatusResponse(
        taskUuid=req.taskUuid,
        status=OperationStatus.RUNNING if rsp_ctx.count < 2 else OperationStatus.DONE,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )


def _check_task_uuid(req: StatusRequest, ctx: BackupContext | RestoreContext | CleanupContext) -> None:
    """Check that the taskUuid in the request matches what we had in our context."""
    if req.taskUuid != ctx.taskUuid:
        raise APIValidationError(f"Mismatched taskUuid {req.taskUuid} != {ctx.taskUuid}")
