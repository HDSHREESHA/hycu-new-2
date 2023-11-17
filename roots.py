from typing import Optional

import rcsdk.skeleton.utils as skel_utils
from rcsdk.schema import CloudLocation, CloudType, Label, Location, RootResource, RootsRequest, RootsResponse

from .schema import AuthContext, ResourceGroup, RootContext


def handle_roots(req: RootsRequest, auth_ctx: Optional[AuthContext]) -> RootsResponse:
    """Return a list of top-level resources."""
    return RootsResponse(resources=_list_root_resources())


def _list_root_resources() -> list[RootResource]:
    return [
        RootResource(
            id="root:0",
            name="Root 0",
            type="Root Resource",
            hasSubresources=True,
            canBackup=True,
            backupSeqGroup=0,
            restoreSeqGroup=0,
            ctx=skel_utils.build_json_object(RootContext(name="root:0")),
            displayCtx=dict(Description="Root resource number one", Color="Green"),
            # Example: Resource in a cloud without a region.
            location=Location(cloud=CloudLocation(type=CloudType.AMAZON)),
        ),
        RootResource(
            id="root:1",
            name="Root 1",
            type="Root Resource",
            hasSubresources=False,
            canBackup=True,
            backupSeqGroup=0,
            restoreSeqGroup=0,
            ctx=skel_utils.build_json_object(RootContext(name="root:1", group=ResourceGroup.A)),
            displayCtx=dict(Description="Root resource number two", Color="Blue"),
            # Example: multiple labels with the same key.
            labels=[Label(key="key1", value="value1"), Label(key="key1", value="value2")],
        ),
        RootResource(
            id="root:2",
            name="Root 2",
            type="Root Resource",
            hasSubresources=False,
            canBackup=False,
            backupSeqGroup=0,
            restoreSeqGroup=0,
            ctx=skel_utils.build_json_object(RootContext(name="root:2")),
            displayCtx=dict(Description="Root resource number three", Color="White"),
            # Example: label with maximum length key (255 characters)
            labels=[Label(key=("_123456789" * 26)[:255], value="long-key-value")],
            # Example: Resource in a cloud with location
            location=Location(cloud=CloudLocation(type=CloudType.GOOGLE, region="us-west1")),
        ),
    ]
