import streamlit as st


def apply_bankiq_style() -> None:
    st.markdown(
        """
        <style>
        :root {
            --navy: #102A43;
            --navy-dark: #0F172A;
            --blue: #1E3A8A;
            --teal: #0B6E8E;
            --teal-light: #E8F4F7;
            --ink: #172033;
            --muted: #64748B;
            --line: #E2E8F0;
            --surface: #FFFFFF;
            --background: #F8FAFC;
            --warning-bg: #FFF8E8;
            --warning-line: #F1D28A;
            --warning-text: #6E4C12;
        }

        .stApp {
            background: var(--background);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        section[data-testid="stSidebar"] {
            background: #F1F5F9;
            border-right: 1px solid var(--line);
            min-width: 320px;
            max-width: 360px;
        }

        .enterprise-header {
            background: linear-gradient(
                135deg,
                var(--navy-dark),
                var(--blue)
            );
            color: #FFFFFF;
            padding: 28px 34px;
            border-radius: 14px;
            margin-bottom: 24px;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.14);
        }

        .enterprise-header h1 {
            color: #FFFFFF !important;
            font-size: 26px;
            font-weight: 750;
            margin: 0 0 8px 0;
            line-height: 1.2;
        }

        .enterprise-header p {
            color: #CBD5E1;
            font-size: 14px;
            margin: 0;
        }

        .scope-card,
        .metric-card,
        .peer-card,
        .insight-card {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
        }

        .scope-card {
            border-left: 5px solid var(--teal);
            padding: 12px 16px;
            margin: 4px 0 20px 0;
            color: var(--ink);
        }

        .peer-card {
            padding: 14px 16px;
            margin: 8px 0 12px 0;
        }

        .peer-card-title {
            color: var(--navy);
            font-size: 1.05rem;
            font-weight: 800;
        }

        .insight-card {
            border-left: 5px solid var(--teal);
            padding: 16px;
            margin: 8px 0 16px 0;
            color: var(--ink);
        }

        .insight-card strong {
            color: var(--teal);
        }

        .source-card {
            background: var(--teal-light);
            border: 1px solid #B9DCE5;
            border-radius: 8px;
            padding: 9px 12px;
            margin: 6px 0;
            color: var(--navy);
            font-size: 13px;
        }

        .guardrail-card {
            background: var(--warning-bg);
            border: 1px solid var(--warning-line);
            border-radius: 10px;
            padding: 14px 16px;
            margin-top: 18px;
            color: var(--warning-text);
            font-size: 13px;
        }

        div[data-testid="metric-container"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 10px;
            padding: 12px 16px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        }

        div[data-testid="stDataFrame"],
        div[data-testid="stCodeBlock"] {
            border: 1px solid var(--line);
            border-radius: 10px;
            overflow: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )