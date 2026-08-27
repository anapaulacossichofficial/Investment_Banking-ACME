ACME_CompetitiveIntelligenceAction.Request req = new ACME_CompetitiveIntelligenceAction.Request();
req.baseInstitutionName = 'ACME_Banking';
req.selectedPeers = new List<String>{'GLOBALTRUST CAPITAL'};
List<ACME_CompetitiveIntelligenceAction.Response> res = ACME_CompetitiveIntelligenceAction.getIntelligence(
    new List<ACME_CompetitiveIntelligenceAction.Request>{req}
);
System.debug('>>> RESULTADO DO CALLOUT: ' + res[0].result);