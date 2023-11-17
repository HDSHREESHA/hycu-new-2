# from rcsdk.constants import FeatureType
from rcsdk.constants import AuthType
from rcsdk.logging import logger
from rcsdk.schema import Capabilities, Manifest
from rcsdk.skeleton.utils import build_plugin_manifest

import plugin


def handle_version() -> Manifest:
    """Return a Manifest object that describes the plugin."""
    return build_plugin_manifest(
        logger,
        plugin
    )
