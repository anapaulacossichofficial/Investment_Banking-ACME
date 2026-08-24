ACME_CompetitiveIntelligenceAction.Request r = new ACME_CompetitiveIntelligenceAction.Request();
r.query = 'ACME Corp';
List<ACME_CompetitiveIntelligenceAction.Response> res = ACME_CompetitiveIntelligenceAction.getIntelligence(new List<ACME_CompetitiveIntelligenceAction.Request>{r});
System.debug(res[0].result);
