import logging
from typing import Optional, Dict

logger = logging.getLogger("ScopeResolver")


class ScopeResolver:
    """Locks account/contact scope before retrieval execution.

    This component enforces deterministic scope resolution for the local demo
    and prevents cross-account leakage in Meeting Prep workflows.
    """

    def __init__(self):
        self._known_accounts = {
            "quantum": {"account_id": "ACC-QUANTUM-001", "account_name": "Quantum"},
            "acme": {"account_id": "ACC-ACME-001", "account_name": "ACME"},
            "orion": {"account_id": "ACC-ORION-001", "account_name": "Orion"}
        }

    def resolve_scope(self, account_name: str, contact_name: Optional[str] = None) -> Dict:
        if not account_name or not account_name.strip():
            raise ValueError("ACCOUNT_SCOPE_NOT_FOUND: Account name is mandatory for scoping.")

        normalized_account = account_name.strip().lower()
        account_record = self._known_accounts.get(normalized_account)

        if not account_record:
            logger.warning("Scope resolution failed: account not found (%s)", account_name)
            return {
                "scope_status": "not_found",
                "account_id": None,
                "account_name": account_name.strip(),
                "contact_id": None,
                "contact_name": contact_name.strip() if contact_name else None,
                "scope_level": "unresolved",
                "cross_account_leakage_prevented": True,
            }

        resolved = {
            "scope_status": "locked",
            "account_id": account_record["account_id"],
            "account_name": account_record["account_name"],
            "contact_id": f"CON-{contact_name.strip().upper()}-001" if contact_name and contact_name.strip() else None,
            "contact_name": contact_name.strip() if contact_name and contact_name.strip() else None,
            "scope_level": "account_contact" if contact_name and contact_name.strip() else "account_only",
            "cross_account_leakage_prevented": True,
        }

        logger.info("Scope locked successfully for account=%s", resolved["account_name"])
        return resolved

    def validate_boundary(self, record_account_id: str, locked_account_id: str) -> bool:
        if not locked_account_id:
            logger.warning("Boundary validation failed: locked_account_id is empty")
            return False

        if record_account_id != locked_account_id:
            logger.warning(
                "Cross-account leakage blocked: record_account_id=%s locked_account_id=%s",
                record_account_id,
                locked_account_id,
            )
            return False

        return True