from infrastructure.database.base_classes import OrmEntityBase
from cassandra.cqlengine import columns
from uuid import uuid4

class TranslationRequestResultOrmEntity(OrmEntityBase):

    task_id: columns.UUID(primary_key=True, default=uuid4)
    step: columns.Text
    result_url: columns.Text