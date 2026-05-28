from rest_framework import serializers

from .models import (
    IngestionBatch,
    EmissionRecord,
    AuditEvent,
    ParseError,
)

# Ingestion batch serializer
class IngestionBatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngestionBatch

        fields = "__all__"

# Emission record serializer
class EmissionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmissionRecord

        fields = "__all__"

# Audit event serializer
class AuditEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditEvent

        fields = "__all__"

# Parse error serializer
class ParseErrorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParseError

        fields = "__all__"
