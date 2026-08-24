ACME_CompetitiveIntelligenceAction.Request r = new ACME_CompetitiveIntelligenceAction.Request();
r.baseInstitutionName = 'ACME_Banking';
r.selectedPeers = new List<String>{'QUANTUM INVESTMENTS', 'GLOBALTRUST CAPITAL'};
List<ACME_CompetitiveIntelligenceAction.Response> res = ACME_CompetitiveIntelligenceAction.getIntelligence(new List<ACME_CompetitiveIntelligenceAction.Request>{r});
System.debug(res[0].result);
