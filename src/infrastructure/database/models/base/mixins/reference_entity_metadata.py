from infrastructure.database.models.base.mixins.basic_audit import BasicAuditMixin
from infrastructure.database.models.base.mixins.soft_archive import SoftArchiveMixin


class ReferenceEntityMetadataMixin(BasicAuditMixin, SoftArchiveMixin):
    """Metadata for reference entities."""
    pass
