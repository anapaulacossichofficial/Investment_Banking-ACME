"""
FastAPI wrapper for CompetitiveIntelligenceAgent / CompetitiveIntelligenceRetriever.
Strictly follows competitive_intelligence_contract.yaml (input/output contract, 
runtime_methods_allowed, fallback_behavior, forbidden_assumptions).
"""

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import os

from agents.competitive_intelligence_agent import CompetitiveIntelligenceAgent

app = FastAPI(
    title="ACME Competitive Intelligence Service",
    description="Exposes fixture-grounded Peer Benchmarking and Strategic Comparison per contract.",
    version="1.0.2",
)

API_KEY = os.environ.get("CI_API_KEY", "9epuB5VwC6yAQikMDxnWRVb9_1Sbk4k-hunJVnEBD0Q")


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


class CompetitiveIntelligenceRequest(BaseModel):
    base_institution_name: str = Field(..., description="Required. e.g. ACME_Banking")
    selected_peers: Optional[List[str]] = Field(default=None, description="Optional list of peer institutions")


class MetricItem(BaseModel):
    metric_name: str
    metric_value: str
    peer_institution: str
    source_id: Optional[str] = None


class SourceTraceItem(BaseModel):
    source_id: str
    source_title: Optional[str] = None


class CompetitiveIntelligenceResponse(BaseModel):
    peer_benchmarking_metrics: List[MetricItem]
    strategic_insights: List[str]
    source_trace: List[SourceTraceItem]
    empty_state_reason: Optional[str] = None


@app.post("/competitive-intelligence", response_model=CompetitiveIntelligenceResponse)
def competitive_intelligence(payload: CompetitiveIntelligenceRequest, x_api_key: str = Header(...)):
    verify_api_key(x_api_key)

    agent = CompetitiveIntelligenceAgent(base_institution=payload.base_institution_name)

    if not payload.selected_peers:
        return CompetitiveIntelligenceResponse(
            peer_benchmarking_metrics=[],
            strategic_insights=[],
            source_trace=[],
            empty_state_reason="No peer selected. Structured empty-state briefing returned.",
        )

    all_metrics: List[MetricItem] = []
    all_insights: List[str] = []
    all_sources: List[SourceTraceItem] = []
    seen_source_ids: set[str] = set()

    for peer in payload.selected_peers:
        metrics_dict = agent.retriever.get_metrics(
            base_institution_name=payload.base_institution_name, peer_name=peer
        )
        if not metrics_dict:
            all_insights.append(f"No approved metrics are available for peer '{peer}'.")
            continue

        source_ids_by_metric = agent.retriever.get_metric_source_ids(
            base_institution_name=payload.base_institution_name, peer_name=peer
        )

        for metric_name, metric_value in metrics_dict.items():
            all_metrics.append(
                MetricItem(
                    metric_name=metric_name,
                    metric_value=str(metric_value),
                    peer_institution=peer,
                    source_id=source_ids_by_metric.get(metric_name),
                )
            )

        insight = agent.retriever.get_insight(
            base_institution_name=payload.base_institution_name, peer_name=peer
        )
        if insight:
            takeaway = insight.get("takeaway", "")
            if takeaway:
                all_insights.append(takeaway)

            source_id = insight.get("source_id")
            if source_id and str(source_id) not in seen_source_ids:
                formatted_sources = agent.retriever.get_sources([str(source_id)])
                for formatted in formatted_sources:
                    all_sources.append(
                        SourceTraceItem(source_id=str(source_id), source_title=formatted)
                    )
                seen_source_ids.add(str(source_id))

    return CompetitiveIntelligenceResponse(
        peer_benchmarking_metrics=all_metrics,
        strategic_insights=all_insights,
        source_trace=all_sources,
        empty_state_reason=None if all_metrics else "No approved metrics available for any selected peer.",
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}