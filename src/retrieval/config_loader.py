from __future__ import annotations
from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = BASE_DIR / "config"
PROMPTS_DIR = BASE_DIR / "prompts"


DEFAULTS = {
    "data_source_strategy": {
        "decision": {
            "primary_recommendation": "controlled_grounding_layer",
            "architecture_role": "local_demo",
            "status": "default_safe_mode",
        }
    },
    "retrieval_policy": {
        "retrieval": {
            "objective": "produce_grounded_meeting_prep_bundle",
            "filters": {
                "require_account_scope": True,
                "require_contact_scope_when_provided": True,
                "require_relevance_threshold": True,
                "min_relevance_score": 0.75,
                "max_chunks": 6,
                "max_structured_records_per_type": 10,
                "exclude_unscoped_documents": True,
            },
            "ranking": {
                "prefer_account_specific_docs": True,
                "prefer_recent_interactions": True,
                "prefer_primary_relationship_material": True,
                "prefer_high_confidence_sources": True,
            },
        }
    },
    "citation_policy": {
        "citation_policy": {
            "require_citations_for_material_claims": True,
            "require_source_metadata": True,
            "require_traceable_snippets": True,
            "allow_multiple_citations_per_claim": True,
        }
    },
    "guardrail_policy": {
        "guardrail_policy": {
            "require_scope_lock": True,
            "prevent_prompt_injection": True,
            "disallow_unsourced_claims": True,
            "disallow_cross_account_leakage": True,
        }
    },
    "fallback_policy": {
        "fallback_policy": {
            "enabled": True,
            "scenarios": {
                "no_evidence": {"action": "abstain"},
                "partial_evidence": {"action": "answer_with_gap_callout"},
                "missing_account_scope": {"action": "request_scope_clarification"},
                "contact_not_found": {"action": "continue_with_account_level_brief_if_allowed"},
                "unsupported_question": {"action": "redirect_to_supported_scope"},
            },
        }
    },
    "observability_policy": {
        "observability_policy": {
            "tracing": {
                "trace_requests": True,
                "trace_agent_handoffs": True,
                "trace_retrieval_events": True,
                "trace_citation_generation": True,
                "trace_fallback_events": True,
            },
            "metrics": {
                "retrieval_latency": True,
                "citation_coverage_rate": True,
                "fallback_rate": True,
                "hallucination_rejection_rate": True,
                "guardrail_event_rate": True,
            },
        }
    },
    "agent_profile": {
        "agents": {
            "supervisor": {
                "role": "intent_router_and_scope_controller",
                "allowed_handoffs": ["meeting_prep_agent"],
            },
            "meeting_prep_agent": {
                "role": "knowledge_grounded_meeting_preparation",
                "allowed_tools": [
                    "crm_retriever",
                    "knowledge_retriever",
                    "citation_builder",
                    "source_trace",
                ],
            },
        }
    },
}


DEFAULT_PROMPTS = {
    "meeting_prep_system": """You are the Meeting Prep Agent...""",
    "meeting_prep_user": """Prepare a meeting briefing for the following scoped request...""",
    "supervisor_router": """You are the Supervisor Router...""",
}


def _safe_load(path: Path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def deep_merge(base, override):
    if not isinstance(base, dict) or not isinstance(override, dict):
        return override if override is not None else base
    merged = dict(base)
    for k, v in override.items():
        merged[k] = deep_merge(base.get(k), v)
    return merged


def load_yaml_config(name: str):
    path = CONFIG_DIR / f"{name}.yaml"
    loaded = _safe_load(path)
    default = DEFAULTS.get(name, {})
    if loaded is None:
        return default
    return deep_merge(default, loaded)


def load_prompt(name: str):
    path = PROMPTS_DIR / f"{name}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return DEFAULT_PROMPTS.get(name, "")


class ConfigLoader:
    """Convenience wrapper around YAML and prompt loading."""

    def get_data_source_strategy(self):
        return load_yaml_config("data_source_strategy")

    def get_retrieval_policy(self):
        return load_yaml_config("retrieval_policy")

    def get_citation_policy(self):
        return load_yaml_config("citation_policy")

    def get_guardrail_policy(self):
        return load_yaml_config("guardrail_policy")

    def get_fallback_policy(self):
        return load_yaml_config("fallback_policy")

    def get_observability_policy(self):
        return load_yaml_config("observability_policy")

    def get_agent_profile(self):
        return load_yaml_config("agent_profile")

    def get_prompt(self, name: str):
        return load_prompt(name)