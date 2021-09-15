from datetime import timedelta
from core.value_objects.id import ID
from infrastructure.configs.main import CassandraDatabase, GlobalConfig, get_cnf
from infrastructure.database.base_classes import OrmEntityBase
from infrastructure.configs.translation_request import (
    TRANSLATION_PRIVATE_TASKS, EXPIRED_DURATION
)

from cassandra.cqlengine import ValidationError, columns

config: GlobalConfig = get_cnf()
database_config: CassandraDatabase = config.CASSANDRA_DATABASE

class TranslationRequestOrmEntity(OrmEntityBase):

    __table_name__ = database_config.TABLES['translation_request']['name']

    creator_id = columns.UUID(default=None)
    task_type = columns.Text(required=True, primary_key=True)
    creator_type = columns.Text(required=True)
    status = columns.Text(required=True, primary_key=True)
    current_step = columns.Text(required=True, primary_key=True)
    expired_date = columns.DateTime(primary_key=True)

    def validate(self):
        
        super(TranslationRequestOrmEntity, self).validate()
        
        if self.task_type in TRANSLATION_PRIVATE_TASKS and not self.creator_id:

            raise ValidationError('Creator cannot be None')

        if self.created_at is not None and self.expired_date is None:

            self.expired_date = self.created_at + timedelta(seconds=EXPIRED_DURATION)
