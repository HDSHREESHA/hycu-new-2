from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.schema import Resource, ResourcesRequest, ResourcesResponse

from .schema import AuthContext, ResourceContext, ResourceGroup, RootContext


def handle_resources(
    req: ResourcesRequest, ctx: RootContext | ResourceContext, auth_ctx: Optional[AuthContext]
) -> ResourcesResponse:
    """Return a list of resources subordinate to 'ctx'"""
    return ResourcesResponse(resources=_list_resources(ctx))


def _list_resources(parent_ctx: RootContext | ResourceContext) -> list[Resource]:
    match parent_ctx.name:
        case "root:0":
            return [
                Resource(
                    name="Root 0 / Resource 0",
                    type="Resource",
                    hasSubresources=True,
                    canBackup=True,
                    backupSeqGroup=1,
                    restoreSeqGroup=1,
                    ctx=skel_utils.build_json_object(
                        ResourceContext(
                            parent_name=parent_ctx.name,
                            parent_group=parent_ctx.group,
                            name="rsrc:0",
                            group=ResourceGroup.B,
                        )
                    ),
                ),
                Resource(
                    name="Root 0 / Resource 1",
                    type="Resource",
                    hasSubresources=False,
                    canBackup=False,
                    backupSeqGroup=1,
                    restoreSeqGroup=1,
                    ctx=skel_utils.build_json_object(
                        ResourceContext(
                            parent_name=parent_ctx.name,
                            parent_group=parent_ctx.group,
                            name="rsrc:1",
                            group=ResourceGroup.A,
                        )
                    ),
                ),
            ]

        case "rsrc:0":
            return [
                Resource(
                    name="Root 0 /Resource 1/ Resource 3",
                    type="Resource",
                    hasSubresources=False,
                    canBackup=True,
                    backupSeqGroup=3,
                    restoreSeqGroup=3,
                    ctx=skel_utils.build_json_object(
                        ResourceContext(
                            parent_name=parent_ctx.name,
                            parent_group=parent_ctx.group,
                            name="rsrc:2",
                            group=ResourceGroup.A,
                        )
                    ),
                ),
                Resource(
                    name="Root 0 / Resource 1 / Resource 4",
                    type="Resource",
                    hasSubresources=False,
                    canBackup=True,
                    backupSeqGroup=4,
                    restoreSeqGroup=5,
                    ctx=skel_utils.build_json_object(
                        ResourceContext(
                            parent_name=parent_ctx.name,
                            parent_group=parent_ctx.group,
                            name="rsrc:3",
                            group=ResourceGroup.B,
                        )
                    ),
                ),
            ]

        case _:
            return []
