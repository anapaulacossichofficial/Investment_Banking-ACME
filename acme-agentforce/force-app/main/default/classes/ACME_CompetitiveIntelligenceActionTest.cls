@IsTest
public class ACME_CompetitiveIntelligenceActionTest {

    private class ExternalCalloutMock implements HttpCalloutMock {
        public HTTPResponse respond(HTTPRequest req) {
            HttpResponse res = new HttpResponse();
            res.setHeader('Content-Type', 'application/json');
            res.setBody('{"company":"QUANTUM INVESTMENTS","market_risk":"High","competitors":["GlobalTrust"]}');
            res.setStatusCode(200);
            return res;
        }
    }

    @IsTest
    static void testGetIntelligenceReturnsResult() {
        Test.setMock(HttpCalloutMock.class, new ExternalCalloutMock());

        ACME_CompetitiveIntelligenceAction.Request req = new ACME_CompetitiveIntelligenceAction.Request();
        req.baseInstitutionName = 'QUANTUM INVESTMENTS';
        req.selectedPeers = new List<String>{ 'GlobalTrust' };

        List<ACME_CompetitiveIntelligenceAction.Request> requests =
            new List<ACME_CompetitiveIntelligenceAction.Request>{ req };

        Test.startTest();
        List<ACME_CompetitiveIntelligenceAction.Response> results =
            ACME_CompetitiveIntelligenceAction.getIntelligence(requests);
        Test.stopTest();

        System.assertEquals(1, results.size(), 'Deve retornar exatamente um output.');
        System.assertNotEquals(null, results[0].result, 'O resultado nao pode ser nulo.');
        System.assert(results[0].result.contains('High'), 'Esperava market_risk High no resultado.');
    }
}
