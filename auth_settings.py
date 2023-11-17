from rcsdk.schema import (
    HycuLayout,
    HycuLayoutColumn,
    HycuLayoutPassword,
    HycuLayoutText,
    SchemasAuthResponse,
    build_hycu_layout_schema,
)
from rcsdk.skeleton.utils import build_json_object

from .schema import AuthContext


def handle_schemas_auth() -> SchemasAuthResponse:
    """Return authentication settings for this plugin."""
    layout = build_hycu_layout_schema(
        layout=HycuLayout(
            [
                HycuLayoutColumn(
                    [
                        HycuLayoutText(
                            id="instanceUrl",
                            label="URL",
                            placeholder="https://example.com/instance",
                            validate_required=True,
                        ),
                        HycuLayoutText(
                            id="instanceUser",
                            label="User",
                            validate_required=True,
                            validate_text_length=(4, 64),
                        ),
                        HycuLayoutPassword(
                            id="instancePassword",
                            label="Password",
                            validate_required=True,
                        ),
                    ]
                ),
            ]
        ),
        payload=build_json_object(
            AuthContext(
                instanceUrl="instanceUrl",
                instanceUser="instanceUser",
                instancePassword_secret="instancePassword",
            )
        ),
    )

    return SchemasAuthResponse(schemaType=layout.schemaType, schema=layout.schema)
