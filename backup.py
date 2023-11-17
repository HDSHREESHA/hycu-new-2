from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.schema import BackupRequest, BackupResponse, OperationStatus
from rcsdk.utils.gcp.gcp import parse_gs_path, path_to_gs_uri

from .schema import AuthContext, BackupContext, ContextKind, ResourceContext, RootContext

def handle_backup(
    req: BackupRequest,
    ctx: RootContext | ResourceContext,
    auth_ctx: Optional[AuthContext],
) -> BackupResponse:
    """Backup a resource."""
    rsp_ctx = BackupContext(
        taskUuid=req.taskUuid,
    )

    bucket_name, root_folder = parse_gs_path(req.storage.url)
    folder_path = f"{root_folder}/{req.taskUuid}" if root_folder else req.taskUuid
    working_path = path_to_gs_uri(f"{bucket_name}/{folder_path}")

    return BackupResponse(
        status=OperationStatus.PENDING if ctx.kind == ContextKind.ROOT else OperationStatus.DONE,
        taskUuid=req.taskUuid,
        workingPath=working_path,
        ctx=skel_utils.build_json_object(rsp_ctx),
    )
