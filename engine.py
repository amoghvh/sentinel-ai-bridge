import uuid
from datetime import datetime
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

class SentinelEngine:
    def __init__(self):
        # We initialize these once to keep the API fast and dependable
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def scan_and_redact(self, text: str):
        # 1. Detect PII (Names, Phones, Emails, Locations, etc.)
        results = self.analyzer.analyze(
            text=text, 
            language='en',
            entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS", "LOCATION", "CREDIT_CARD"]
        )

        # 2. Extract types found for the audit log
        found_types = list(set([res.entity_type for res in results]))

        # 3. Apply the 'Standard Professional' Redaction
        anonymized_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results,
            operators={"DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"})}
        )

        return {
            "sanitized_text": anonymized_result.text,
            "entities_found": found_types,
            "audit_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat()
        }

# For testing locally
if __name__ == "__main__":
    engine = SentinelEngine()
    print(engine.scan_and_redact("My name is Amogh and my email is test@example.com"))