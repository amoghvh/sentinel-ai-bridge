# sentinel-ai-bridge

Sentinel AI Bridge

Sentinel AI Bridge is a high-performance, security-first privacy middleware and proxy gateway designed to sit between enterprise applications and upstream Large Language Model (LLM) providers (Anthropic, Google, xAI).

The platform intercepts incoming prompts and outgoing completions to guarantee zero-leakage of Personally Identifiable Information (PII) and maintain a cryptographic, tamper-evident audit log for compliance governance (GDPR, HIPAA, and SOC2).

<img width="421" height="638" alt="image" src="https://github.com/user-attachments/assets/9ece1518-41b2-4a5c-8fd7-1ae2dbd47ef3" />


🛠️ Tech Stack & Production Primaries

    Gateway Core: Python 3.11+ / FastAPI (Asynchronous, non-blocking network I/O)

    PII Inspection Engine: Microsoft Presidio Analyzer + SpaCy (Hybrid statistical NER + custom regex rule matching)

    Token Tokenization Mapping: Redis (In-memory key-value store with strict TTL expiration policies)

    Audit Persistence Engine: PostgreSQL / TimescaleDB (Time-series optimization for rapid compliance log aggregation)

    Security & Cryptography: PyCryptodome (HMAC-SHA256 log signing, AES-256 state encryption)

🚀 Security Features & System Guarantees
1. Zero-Trust In-Flight Redaction

The engine tokenizes sensitive data classifications at the ingestion boundary before network dispatch:

    Direct Identifiers: Names, Email Addresses, Phone Numbers, SSN/National IDs, Passwords/API Keys.

    Indirect Identifiers: IP Addresses, Cryptographic Hashes, Financial Account Details.

2. Salted Reversible Masking

Instead of dropping data destructively, Sentinel replaces entities with deterministic tokens matched to the active request context session:

    Input: “Can you draft an email to amogh.hosamani@email.com confirming his balance of $5,000?”

    Upstream Egress: “Can you draft an email to [REDACTED_EMAIL_4f1a] confirming his balance of [REDACTED_MONEY_9b2c]?”

3. Non-Repudiation Audit Logging

Every interaction generates a immutable audit line in a secure JSONL storage schema. Log files are signed sequentially using an externalized cryptographic key to guarantee logs cannot be altered retroactively by unauthorized system actors.

📉 Enterprise Production Constraints

    Sub-Millisecond Latency Overhead: Security proxies cannot act as choke points. By offloading regex compilations to pre-cached C-bindings and executing local NER pipelines asynchronously alongside memory mapped token mapping, Sentinel limits total processing overhead to less than 8ms per request transaction.

    Ephemeral Cache Life Cycles: Redaction tokens stored within the Redis instance are coupled to strict Time-To-Live (TTL) properties. Context boundaries are purged from local operational cache 15 minutes after request closure to minimize memory surface vectors.
