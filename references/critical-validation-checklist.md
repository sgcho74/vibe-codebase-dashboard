# Critical Validation Checklist

Use this checklist to challenge AI-generated code.

## 1. Basic Correctness

- Does the code solve the stated problem?
- Are assumptions explicitly documented?
- Is the input/output contract clear?
- Are errors handled intentionally?

## 2. Edge Cases

- Empty input
- Null input
- Invalid input
- Large input
- Duplicate input
- Boundary values
- Timeout
- Retry
- Partial failure

## 3. Failure Scenarios

- External API failure
- DB connection failure
- Permission failure
- File not found
- Network interruption
- Invalid configuration
- Missing environment variable
- Data format mismatch

## 4. Security Review

- Authentication checked
- Authorization checked
- Input validation present
- Secrets not hard-coded
- Logs do not expose sensitive data
- SQL injection avoided
- Command injection avoided
- Path traversal avoided

## 5. Data Safety

- Migration rollback exists
- Destructive operations guarded
- Backup or recovery considered
- Idempotency considered
- Transaction boundary clear

## 6. Operational Readiness

- Logs are useful
- Errors are observable
- Metrics are available where needed
- Rollback path exists
- Deployment impact is clear

## 7. Human Review

- Reviewer assigned
- Owner assigned
- Review evidence captured
- Approval required for risky change
