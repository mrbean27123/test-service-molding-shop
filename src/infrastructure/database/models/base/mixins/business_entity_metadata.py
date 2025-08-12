from infrastructure.database.models.base.mixins.audit import AuditMixin
from infrastructure.database.models.base.mixins.optimistic_locking import OptimisticLockingMixin
from infrastructure.database.models.base.mixins.soft_delete import SoftDeleteMixin


class BusinessEntityMetadataMixin(AuditMixin, SoftDeleteMixin, OptimisticLockingMixin):
    """
    Complete metadata for business-critical entities.

    Includes full audit trail, soft delete and optimistic locking mechanisms.
    """
    pass
