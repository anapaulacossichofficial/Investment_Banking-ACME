public class ACME_CompetitiveIntelligenceAction {

public class Request {
    @InvocableVariable(required=true label='Base Institution Name' description='Always pass ACME_Banking as the value here. This represents our own institution, not a peer.')
    public String baseInstitutionName;

    @InvocableVariable(required=false label='Selected Peers' description='List of peer institution names mentioned by the user for comparison, such as QUANTUM INVESTMENTS or GLOBALTRUST CAPITAL. Never include ACME_Banking in this list. If the user does not specify any peer, leave this list empty rather than guessing a name.')
    public List<String> selectedPeers;
    }

    public class Response {
        @InvocableVariable(label='Competitive Intelligence Result')
        public String result;
    }

    @InvocableMethod(label='Get Competitive Intelligence' description='Fetches competitive intelligence data from ACME external API')
    public static List<Response> getIntelligence(List<Request> requests) {
        List<Response> responses = new List<Response>();

        for (Request req : requests) {
            Response res = new Response();
            try {
                HttpRequest httpReq = new HttpRequest();
                httpReq.setEndpoint('callout:ACME_Competitive_Intelligence/competitive-intelligence');
                httpReq.setMethod('POST');
                httpReq.setHeader('Content-Type', 'application/json');
                httpReq.setTimeout(20000);

                Map<String, Object> bodyMap = new Map<String, Object>();
                bodyMap.put('base_institution_name', req.baseInstitutionName);
                if (req.selectedPeers != null && !req.selectedPeers.isEmpty()) {
                    bodyMap.put('selected_peers', req.selectedPeers);
                }
                httpReq.setBody(JSON.serialize(bodyMap));

                Http http = new Http();
                HttpResponse httpRes = http.send(httpReq);

                if (httpRes.getStatusCode() == 200) {
                    res.result = httpRes.getBody();
                } else {
                    res.result = 'Error: HTTP ' + httpRes.getStatusCode() + ' - ' + httpRes.getBody();
                }
            } catch (Exception e) {
                res.result = 'Error calling external service: ' + e.getMessage();
            }
            responses.add(res);
        }

        return responses;
    }
}